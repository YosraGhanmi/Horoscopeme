from moviepy.editor import *
import random
import scripthandler
import uplaod_video_instagram

def zidaudio():
    scripthandler.scripth()
    c = VideoFileClip("vid3.mp4")
    length = 14
    audio = AudioFileClip("No copyright  Astro background music with theme  COPYRIGHT FREE background  No Copyright.mp3")
    start = random.randint(0,int(audio.duration) - length)
    audio_bg = audio.subclip(start, start + length)
    c.audio = audio_bg
    c.write_videofile('vid4.mp4', fps=24, codec="libx264", audio_codec="aac")

zidaudio()
uplaod_video_instagram.upload_insta("vid4.mp4", "#horoscope #scorpio #aries #capriscorn #tauros #piscies #balance #positive #daily #vibe #fyppp0")