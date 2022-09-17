from pytube import YouTube
import glob
import os.path

#유튜브 전용 인스턴스 생성
def get_mp3(URL, rank):
	yt = YouTube(URL)
	# 특정영상 다운로드
	yt.streams.filter(only_audio=True).first().download("songs")

	# 확장자 변경
	files = glob.glob("songs/*.mp4")
	for x in files:
		if not os.path.isdir(x):
			#filename = os.path.splitext(x)
			try:
				os.rename(x,"songs/" + str(rank) + '.mp3')
			except:
				pass
	print(rank, "success mp3")