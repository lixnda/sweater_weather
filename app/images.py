from PIL import Image
from io import BytesIO
import requests
import numpy as np
import cv2
import math
import json
import random

def load_img(url):
    data = requests.get(url)
    img = Image.open(BytesIO(data.content)).convert("RGB")
    rgb = np.array(img)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv

def extract_hsv(hsv):
    h = hsv[:, :, 0].mean()
    s = hsv[:, :, 1].mean()
    return h, s

def compatScore(imgA, imgB):
    h1, s1 = extract_hsv(imgA)
    h2, s2 = extract_hsv(imgB)

    #for two hues score high, opposites or adjacent colors
    #cos function used to determine this (0 and 180 apart receives high score)
    #cv2 returns hue ranging 0 to 180
    hue_difference = min(abs(h1-h2), 180-abs(h1-h2)) #hue is circular, so 0 and 359 is close
    hue_score = (math.cos(2*math.radians(hue_difference*2))+1)/2 #output ranges from [0,1]

    sat_difference = abs(s1-s2)
    sat_score = 1 - (sat_difference/255)

    score = sat_score*0.6 + hue_score*0.4
    return score, sat_score, hue_score

def findMatch(queryA, queryB):
    nameA = queryA.replace(" ", "_")
    filenameA = f"{nameA}.json"
    nameB = queryB.replace(" ", "_")
    filenameB = f"{nameB}.json"

    top_match = ""
    top_score = 0
    dB_link = ""
    hue_score = 0
    sat_score = 0

    index = random.randint(0, 99)

    with open(filenameA, "r") as file:
        data = json.load(file)
        while not("Depop" in (data["images_results"][index]["source"])):
            index = random.randint(0, 99)
        pieceA_link =  data["images_results"][index]["original"]
        pieceA = load_img(pieceA_link)
        dA_link = data["images_results"][index]["link"]
        print(pieceA_link)
        print(dA_link)

    with open(filenameB, "r") as file:
        data = json.load(file)
        for i in range(0, 99):
            if "Depop" in (data["images_results"][i]["source"]):
                pieceB_link = data["images_results"][i]["original"]
                print(pieceB_link)
                pieceB = load_img(pieceB_link)
                score, sat, hue = compatScore(pieceA, pieceB)
                if score>top_score:
                    top_score = score
                    top_match = pieceB_link
                    sat_score = sat
                    hue_score = hue
                    dB_link = data["images_results"][i]["link"]
                print(score)
    print(f"original: {pieceA_link}")
    print(f"matched: {pieceB_link}")
    print(f"sat: {sat_score}")
    print(f"hue: {hue_score}")
    return pieceA_link, top_match, dA_link, dB_link, sat_score, hue_score
