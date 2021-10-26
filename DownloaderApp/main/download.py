import os
import re
import urllib.request
from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import YouTube
from werkzeug.utils import redirect


def Query(query):

    
    searchQuery = re.sub(r"\s+", '+', query)
    response= urllib.request.urlopen("https://www.youtube.com/results?search_query="+searchQuery)
    video_ids= re.findall(r'watch\?v=(\S{11})', response.read().decode())
    try:
        topresult = "https://youtu.be/"+video_ids[0]
    except(Exception,IndexError):
        return
    
    audio= YouTube(topresult).streams.get_audio_only().download(output_path='./DownloaderApp/TempStorage')
    print(audio)
    print(audio[:-4])
    clip= AudioFileClip(audio)
    clip.write_audiofile(audio[:-4]+".mp3")
    os.remove(audio)
    clip.close()
       
        
 
 
  

 
   
   
   

