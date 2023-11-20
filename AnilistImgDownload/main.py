import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()


def processUrl(urls):
    i = 0
    for url in urls:
        r = requests.get(url)
        soup = BS(r.content, 'lxml')
        print(i, url)
        i += 1
        
        img = soup.find('img', {'class': 'image'})
        src = img.get('src')

        download_image(url, src)

def download_image(url, src):
    image = requests.get(src)

    name = url.split('/')[-1]
    format = src.split('.')[-1]
    fileName = f"{name}.{format}"
    folder_name = "Images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    filePath = os.path.join(folder_name, fileName)
    with open(filePath, 'wb') as f:
        f.write(image.content)
    print(filePath)


def main():
    url = 'https://anilist.co/'
    username = "anmoldobariya987@gmail.com"
    password = os.getenv('PASSWD')

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(url)
    time.sleep(3)
    
    # Click on the "Sign In" button
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="nav"]/div[2]/div/a[3]')
    sign_in_button.click()
    time.sleep(2)
    
    # Enter username and password
    username_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/form/input[1]')
    username_input.send_keys(username)
    time.sleep(0.25)
    password_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/form/input[2]')
    password_input.send_keys(password)

    input("Please solve the CAPTCHA and press Enter when it's done...")

    print('Login successful')
    
    # Click on the "Profile" button
    profile_button = driver.find_element(By.XPATH, '//*[@id="nav"]/div[2]/div[1]/a[2]')
    profile_button.click()
    time.sleep(2)
    
    # Click on the "Favorites" button
    favorites_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[2]/div/a[4]')
    favorites_button.click()
    time.sleep(2)

    # Scroll the page to load all content
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)
    
    # Extract URLs of favorite items
    result_container = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/div/div[3]/div[1]')
    urls = [element.get_attribute("href") for element in result_container.find_elements(By.TAG_NAME, "a")]
    # print(urls)

    driver.quit()

    # urls = [
    #     "https://anilist.co/character/62/Zoro-Roronoa",
    #     "https://anilist.co/character/123212/Kiyotaka-Ayanokouji",
    #     "https://anilist.co/character/51347/Akeno-Himejima",
    #     "https://anilist.co/character/50389/Rias-Gremory",
    #     "https://anilist.co/character/127222/Mai-Sakurajima",
    #     "https://anilist.co/character/133676/Marin-Kitagawa",
    #     "https://anilist.co/character/124381/Zero-Two",
    #     "https://anilist.co/character/195602/Mahiru-Shiina",
    #     "https://anilist.co/character/16342/Hancock-Boa",
    #     "https://anilist.co/character/137080/Makima",
    #     "https://anilist.co/character/127691/Satoru-Gojou",
    #     "https://anilist.co/character/67065/Hachiman-Hikigaya",
    #     "https://anilist.co/character/85/Kakashi-Hatake",
    #     "https://anilist.co/character/141842/Roxanne",
    #     "https://anilist.co/character/171759/Vermeil",
    #     "https://anilist.co/character/131106/Tsukasa-Yuzaki",
    #     "https://anilist.co/character/127595/Hina-Tachibana",
    #     "https://anilist.co/character/19604/Aki-Nijou",
    #     "https://anilist.co/character/89163/Chisato-Hasegawa",
    #     "https://anilist.co/character/1555/Hinata-Hyuuga",
    #     "https://anilist.co/character/66171/Kyouko-Hori",
    #     "https://anilist.co/character/141122/Kei-Karuizawa",
    #     "https://anilist.co/character/155702/Miyako-Shikimori",
    #     "https://anilist.co/character/164986/Nagisa-Kubo",
    #     "https://anilist.co/character/120649/Kaguya-Shinomiya",
    #     "https://anilist.co/character/128106/Chizuru-Ichinose",
    #     "https://anilist.co/character/70069/Kurumi-Tokisaki",
    #     "https://anilist.co/character/127596/Rui-Tachibana",
    #     "https://anilist.co/character/89158/Mio-Naruse",
    #     "https://anilist.co/character/65259/Tooka-Yatogami",
    #     "https://anilist.co/character/147005/Ruka-Sarashina",
    #     "https://anilist.co/character/272395/Shiori-Goshiki",
    #     "https://anilist.co/character/135231/Chizuru-Tachibana",
    #     "https://anilist.co/character/135226/Kana-Kojima",
    #     "https://anilist.co/character/13392/Inaho-Kushiya",
    #     "https://anilist.co/character/43669/Kouko-Kaga",
    #     "https://anilist.co/character/153043/Kirara--Hoshino",
    #     "https://anilist.co/character/137263/Sagiri",
    #     "https://anilist.co/character/137079/Power",
    #     "https://anilist.co/character/2767/Tsunade-Senju",
    #     "https://anilist.co/character/13390/Haruko-Amaya",
    #     "https://anilist.co/character/121104/Ai-Hayasaka",
    #     "https://anilist.co/character/154224/Mami-Nanami",
    #     "https://anilist.co/character/123216/Honami-Ichinose",
    #     "https://anilist.co/character/123217/Sae-Chabashira",
    #     "https://anilist.co/character/6046/Shizuka-Marikawa",
    #     "https://anilist.co/character/904/Rangiku-Matsumoto",
    #     "https://anilist.co/character/908/Yoruichi-Shihouin",
    #     "https://anilist.co/character/187917/DuNa-Lee",
    #     "https://anilist.co/character/51337/Xenovia-Quarta",
    #     "https://anilist.co/character/51339/Irina-Shidou",
    #     "https://anilist.co/character/51341/Rossweisse",
    #     "https://anilist.co/character/141268/Yasaka",
    #     "https://anilist.co/character/183885/Aquamarine-Hoshino",
    #     "https://anilist.co/character/172759/Ai-Hoshino",
    #     "https://anilist.co/character/58341/Ravel-Phenex",
    #     "https://anilist.co/character/88080/Kuroka",
    #     "https://anilist.co/character/723/Nami",
    #     "https://anilist.co/character/61/Robin-Nico",
    #     "https://anilist.co/character/53901/Madara-Uchiha",
    #     "https://anilist.co/character/14/Itachi-Uchiha",
    #     "https://anilist.co/character/2423/Jiraiya"
    # ]

    processUrl(urls)

if __name__ == "__main__":
    main()
