from pytube import YouTube
import os

urls = ['https://youtu.be/WT7EVP4pgUs?si=wANlgLCYXpRJDj1S']

for url in urls:
    yt = YouTube(url)

    stream = yt.streams.get_highest_resolution()

    print("Title:", yt.title)
    print("Duration:", yt.length, "seconds")
    print("File size:", stream.filesize/1024/1024, "mb")

    # Download the video
    folder_name = "Downloads"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    stream.download(output_path = folder_name)

    print("Download completed!")