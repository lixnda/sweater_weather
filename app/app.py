import random
import os
from flask import Flask, render_template, request, session, redirect
import api
import images
import json

"""
Assignment Information:
    Assignment:     Individual Project
    Team ID:        LC4 - 16
    Author:         Linda Zheng, zheng955@purdue.edu
    Date:           12/08/2025

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

app = Flask(__name__)

app.secret_key = os.urandom(32)

#main screen. if user hasnt entered a place, then redirects them to /location
@app.route("/", methods=['GET', 'POST'])
def home():
    if 'place' in session:
        print(session['lat'])
        print(session['lon'])
        print(session['place'])

        json_weather = api.weatherData((session['lat']), (session['lon']))
        #print(json_weather)
        weather = (json_weather["weather"][0]["main"])
        current_temp = (json_weather["main"]["temp"])
        feels_like = (json_weather["main"]["feels_like"])
        min_temp = (json_weather["main"]["temp_min"])
        max_temp = (json_weather["main"]["temp_max"])
        print(weather, current_temp, feels_like, min_temp, max_temp, sep="|")

        style = session["style"]

        #api calls to ensure json of clothing are in directory
        api.get_images("depop women jackets y2k")
            
        api.get_images("depop women pants y2k")
        api.get_images("depop women sweaters y2k")

        api.get_images("depop women tshirts y2k")
        api.get_images("depop shorts and skirts y2k")


        if(current_temp>80):
            top, bottom, linkT, linkB, sat_score, hue_score  =  images.findMatch("depop women tshirts y2k", "depop shorts and skirts y2k")
        elif(current_temp>70):
            top, bottom, linkT, linkB, sat_score, hue_score =  images.findMatch("depop women tshirts y2k", "depop women pants y2k")
        elif(current_temp>50):
            top, bottom, linkT, linkB, sat_score, hue_score =  images.findMatch("depop women sweaters y2k", "depop women pants y2k")
        else:
            top, bottom, linkT, linkB, sat_score, hue_score =  images.findMatch("depop women jackets y2k", "depop women pants y2k")

        hue_score = round(hue_score*100, 2)
        sat_score = round(sat_score*100, 2)
        return render_template("home.html", place=session['place'], temp=current_temp, weather=weather, feels_like=feels_like, min_temp=min_temp, max_temp=max_temp, bottom=bottom, top=top, linkT=linkT, linkB=linkB, sat_score=sat_score, hue_score=hue_score)
    else:
        return redirect('/location')

#gets user input for location. saved in session so loction is saved even after reload
@app.route("/location", methods=['GET', 'POST'])
def location():
    #if user submits form
    if request.method == 'POST':
        location = request.form.get('place')
        session['userPlace'] = location
        json_place = api.coordinates(location)

        #error getting data, if api call is past limit for example
        if json_place is None:
            return render_template("location.html")
        
        #no matching place names
        if len(json_place) == 0:
            print("Enter New Place")
            return render_template("location.html")
        
        #chooses index 0 even if multiple options for simplicity
        else:
            session['lat'] = float(json_place[0]['lat'])
            session['lon'] = float(json_place[0]['lon'])
            session['place'] = json_place[0]['name']
            session["style"] = "feminine"
            return redirect("/")

    return render_template("location.html")

'''
@app.route("/updateStyle", methods=["POST"])
def update_session():
    style = request.form.get("style", "feminine")
    session["style"] = style
    print(style)
    return redirect("/")
'''

if __name__ == '__main__':
    app.debug = True
    app.run()
