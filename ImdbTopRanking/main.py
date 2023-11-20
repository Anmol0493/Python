from bs4 import  BeautifulSoup
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pymongo import MongoClient

load_dotenv()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

#Find the IMBD Rating Movies
try:
    url = "https://www.imdb.com/chart/top/"
    source = requests.get(url, headers=headers)
    source.raise_for_status()
    list =[]

    soup = BeautifulSoup(source.content,'html.parser')
    # print(soup)
    
    all_movies = soup.find('ul',{"class" :"ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base"})
    
    movies = all_movies.find_all('div', {'class': 'sc-14dd939d-0 fBusXE cli-children'})
    # print(movies)
    base_url = "https://www.imdb.com"

    for movie in movies:
        url = movie.find('a').get('href')
        complete_url = base_url + url
        # print(url)
        title = movie.find('h3', {"class":"ipc-title__text"}).text.split('. ')
        # print(title[0], title[1])
        details = movie.find_all('span', {"class": "sc-14dd939d-6 kHVqMR cli-title-metadata-item"})
        year = details[0].text
        run_time = details[1].text
        # print(year, run_time)
        rating = movie.find("span", {"class": "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text
        # print(rating)
        list.append({"url": complete_url, "rank": int(title[0]), "name": title[1], "year": int(year), "rating": float(rating), "run_time": run_time})
        # print(list)


    # Creating a DataFrame with the scraped data
    dataFrame = pd.DataFrame(list, columns=['rank','name','year','rating','run_time', 'url'])
    # print(dataFrame)

    dataFrame.to_csv("IMDB movies.csv" , mode='a', header=True, index=False)


    # create engine
    user=os.getenv("DB_USER")
    password=os.getenv("DB_PASS")
    host=os.getenv("DB_HOST")
    db=os.getenv("DB_NAME")

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

    table_name = 'imdb_top_rankings'
    dataFrame.to_sql(name = table_name, con = engine, if_exists = "replace", index = False)

    print("MySQL table created")
    engine.dispose()


    URI = os.getenv("Mongo_URI")
    client = MongoClient(URI)
    collection = client["IMDB_List"]["IMDB_top_rankings"]

    data_to_insert = dataFrame.to_dict(orient = "records")

    collection.insert_many(data_to_insert)
    print("MongoDB collection created")
    client.close()
    

except Exception as e:
    print(e)
