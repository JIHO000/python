from pytube import YouTube
import glob
import os.path

#유튜브 전용 인스턴스 생성
def get_mp3(URL, rank):
	yt = YouTube(URL)
	# 특정영상 다운로드
	yt.streams.filter(only_audio=True).first().download("songs")
	yt.streams.get_highest_resolution().download("videos")
	# 확장자 변경
	files = glob.glob("songs/*.mp4")
	for x in files:
		if not os.path.isdir(x):
			filename = os.path.split(x)
			dir = filename[0]
			song_name = os.path.splitext(filename[1])[0]
			try:
				os.rename(x,dir + "/" + str(rank) + ". " + song_name + ".mp3")
			except:
				pass
	print(rank, "success mp3")

	files = glob.glob("videos/*.mp4")
	for x in files:
		if not os.path.isdir(x):
			filename = os.path.split(x)
			dir = filename[0]
			song_name = filename[1]
			try:
				os.rename(x,dir + "/" + str(rank) + ". " + song_name)
			except:
				pass
	
	print(rank, "success MV")