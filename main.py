#------------------------Python youtube shorts bot---------------------#

# Imports
import urllib.request
import re
import upload
from random import randrange
import pafy
import pytube
from pytube import YouTube
from mhyt import yt_download
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

#------------------------global variables------------------------#
global url


#-----------account auth-----------#


#------topic selection--------#

search_keyword = "minecraftshorts"


#--------yt-searcher--------#

html = urllib.request.urlopen(
    "https://www.youtube.com/results?search_query=" + search_keyword + "&sp=EgIYAQ%253D%253D")
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())


def getURL():
    global url
    url = "https://www.youtube.com/watch?v=" + video_ids[randrange(10)]
    print(url)
    video = pafy.new(url)
    print(video.length)
    if(video.length >= 300):
        getURL()
    else:
        print("Task Done")


getURL()


#---------------------download logic------------------------#


yt_download(url,
            r"C:\Users\Monish Meher\Desktop\download.mp4", format='bestvideo')

#-------------------------------video cutter change aspect ratio----------------------------------#

# genrating timestaps
video = pafy.new(url)
t1 = randrange(video.length)
if(t1 > 30):
    t2 = t1 - 30
elif(t1 < 30):
    t2 = t1 + 30

if(t1 > t2):
    t0 = t2
    t2 = t1
    t1 = t0

print(t1, t2)


# trim clip
ffmpeg_extract_subclip(r"C:\Users\Monish Meher\Desktop\download.mp4",
                       t1, t2, targetname=r"C:\Users\Monish Meher\Desktop\test.mp4")


#
clip = VideoFileClip(r"C:\Users\Monish Meher\Desktop\test.mp4")
print(clip.w)
print(clip.h)

#---------------------------------------upload logic----------------------------------------------------#

PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "SIGN IN"))
    )
    element.click()
except:
    driver.quit()


try:
    nextElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-vQzf8d"))
    )
    nextElement.click()
except:
    driver.quit()


try:
    passElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type=password]"))
    )
    passElement.send_keys("Meher@123")
except:
    driver.quit()
