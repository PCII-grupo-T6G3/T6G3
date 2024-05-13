# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:25:05 2024

@author: afons
"""

from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.Event import Event
from classes.Participant import Participant
from classes.Registration import Registration
from classes.Type import Type
from classes.Venue import Venue
from classes.Feedback import Feedback
from classes.Userlogin import Userlogin

app = Flask(__name__)

Event.read(filename + 'project.db')
Participant.read(filename + 'project.db')
Registration.read(filename + 'project.db')
Type.read(filename + 'project.db')
Venue.read(filename + 'project.db')
Feedback.read(filename + 'project.db')
Userlogin.read(filename + 'project.db')
prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_subform as gfsubsub
import subs_productFoto as productFotosub


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

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


@app.route("/productform", methods=["post","get"])
def productFoto():
    submenu = request.args.get("subm")
    cname = 'Product'
    return productFotosub.productFoto(app,cname,submenu)

@app.route("/order/mapa", methods=["post","get"])
def ordermapa():

    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu)



    
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()