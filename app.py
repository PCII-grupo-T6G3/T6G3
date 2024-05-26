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

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        group = Userlogin.obj[ulogin].usergroup
        if group != "admin":
            Userlogin.current(ulogin)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            Userlogin.remove(obj.user)
            if not Userlogin.previous():
                Userlogin.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = Userlogin(request.form["user"],request.form["usergroup"], \
                            Userlogin.set_password(request.form["password"]))
            Userlogin.insert(obj.user)
            Userlogin.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
                print(obj.password)
            Userlogin.update(obj.user)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    else:
        return render_template("index.html", ulogin=ulogin)

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