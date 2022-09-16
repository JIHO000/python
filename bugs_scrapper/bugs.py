import re
from tkinter import E
import requests
from bs4 import BeautifulSoup

URL = f"https://music.bugs.co.kr/chart"

def get_table():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table", {"class": "list trackList byChart"}).find("tbody").find_all("tr")
    return table

def extract_song(html):
    rank = html.find("div", {"class" : "ranking"}).find("strong").get_text(strip=True).strip("\n").strip("\r")
    title = html.find("p", {"class" : "title"}).find("a").get_text(strip=True).strip("\n").strip("\r")
    try:
        artist = html.find("p", {"class" : "artist"}).find("a").get_text(strip=True).strip("\n").strip("\r")
    except:
        artist = ""
    album = html.find("a", {"class" : "album"}).get_text(strip=True).strip("\n").strip("\r")
    return {"랭킹" : rank, "곡" : title, "아티스트" : artist, "앨범" : album}

def extract_songs():
    songs = []
    count = 0
    table = get_table()
    for result in table:
        song = extract_song(result)
        songs.append(song)
    return songs
