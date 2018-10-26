#coding: utf-8
from LineTimeline import *
import time

client = LineTimeline("EycE94wjyyvtrPVW6602.Imt35sCtPAdGTtGLUShYqG.cMfu43swSxwhj67QwBMKHa+AvgSVYv5kZgs/GRQhpi0=")

while True:
    feed = client.getFeed()
    for x in feed["result"]["feeds"]:
        if x["post"]["postInfo"]["liked"] == False:
            client.likePost(x["post"]["postInfo"]["postId"])
    time.sleep(60)
