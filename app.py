# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:25:05 2024

@author: afons
"""

from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.event import Event
from classes.participant import Participant
from classes.registration import Registration
from classes.type import Type
from classes.venue import Venue
from classes.feedback import Feedback
from classes.userlogin import Userlogin

app = Flask(__name__)

Event.read(filename)
Participant.read(filename)
Registration.read(filename)
Type.read(filename)
Venue.read(filename)
Feedback.read(filename)
Userlogin.read(filename)
prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder

import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_hform as gfhsub
import subs_subform as gfsubsub
import subs_userlogin as ulsub

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"),usergroup=session.get('usergroup'))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/userlogin", methods=["post","get"])
def userlogin():
    return ulsub.userlogin()

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),usergroup=session.get('usergroup'),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

@app.route("/eventsT", methods=["post","get"])
def eventsT():
    submenu = request.args.get("subm")
    Event.read(filename)
    return render_template("eventsT.html",objlst=Event.obj,
                           ulogin=session.get("user"),usergroup=session.get('usergroup'),submenu=submenu)

@app.route("/feedbackT", methods=["post","get"])
def feedbackT():
    submenu = request.args.get("subm")
    Feedback.read(filename)
    return render_template("feedbackT.html",objlst=Feedback.obj,
                           ulogin=session.get("user"),usergroup=session.get('usergroup'),submenu=submenu,
                           Event=Event,Participant=Participant)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    submenu = request.args.get("subm")
    return gfhsub.hform(cname,submenu)
        
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    submenu = request.args.get("subm")
    return gfsubsub.subform(cname,submenu)




@app.route("/order/mapa", methods=["post","get"])
def ordermapa():
    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu)
    
if __name__ == '__main__':
        # app.run(debug=True)
        app.run()