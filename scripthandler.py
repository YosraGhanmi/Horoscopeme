import horoscope
from moviepy.editor import *
from moviepy.video.fx import resize

from imagehandler import vidgen


def format_paragraph(text, max_line_length=20):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    formatted_text = "\n".join(lines)
    return formatted_text

def shorter(ch):
    l=ch.split(".")
    return ".".join(l[0:2])
def scripth():
    vidgen()
    c = VideoFileClip("vid1.mp4")
    text = TextClip(format_paragraph(shorter(horoscope.horoscope_API())), fontsize=20, color="white").set_position('center', 'center').set_duration(14)
    final = CompositeVideoClip([c, text])
    final1 = final.resize((1080,1920))
    final1.write_videofile('vid3.mp4', fps=24, codec="libx264", audio_codec="aac")

scripth()
