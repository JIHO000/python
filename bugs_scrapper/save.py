import csv
from datetime import datetime

current_date = datetime.today().strftime("%Y%m%d%H%M%S")

def save_to_file(songs):
    file = open(f"{current_date}.csv", mode="w", encoding='utf-8-sig',newline="")
    writer = csv.writer(file)
    writer.writerow(["랭킹", "곡", "아티스트", "앨범"])
    for song in songs:
        writer.writerow(list(song.values()))
    return