import csv
from datetime import datetime
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        pass
current_date = datetime.today().strftime("%Y%m%d%H%M%S")

def save_to_file(songs):
    createDirectory("MV")
    createDirectory("CSV")
    createDirectory("songs")
    createDirectory("videos")
    file = open(f"CSV/{current_date}.csv", mode="w", encoding='utf-8-sig',newline="")
    writer = csv.writer(file)
    writer.writerow(["랭킹", "곡", "아티스트", "앨범"])
    for song in songs:
        writer.writerow(list(song.values()))
    return