from pytube import YouTube
import glob
import os.path

#유튜브 전용 인스턴스 생성
par = "https://www.youtube.com/watch?v=F0B7HDiY-10"
yt = YouTube(par)
yt.streams.filter(only_audio=True).all()

# 특정영상 다운로드
yt.streams.filter(only_audio=True).first().download()

# 확장자 변경
files = glob.glob("*.mp4")
for x in files:
	if not os.path.isdir(x):
		filename = os.path.splitext(x)
		try:
			os.rename(x,filename[0] + '.mp3')
		except:
			pass