# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_hform.py

"""""
from flask import Flask, render_template, request, session

from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
from classes.userlogin import Userlogin
from classes.order2Form import Order2Form

from datetime import timedelta
from datetime import datetime

prev_option = ""

def gerah(clh):
    clh.reset()
    clh("None", CustomerOrder, diahoraselected, 9, 12)
    objh = clh.obj[clh.lst[0]]
    return objh
    

def hform(cname='',submenu=""):
    global prev_option
    global diahoraselected
    
    cname = 'Class_horario'
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cname)
        clh = eval("Horario2Form")
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "''":
            diahoraselected = datetime.today()
            
        
        elif prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(cl.auto_number,len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
            
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"

            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()

            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"

            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == "previousw":
                diahoraselected = diahoraselected + timedelta(days=-7)

            elif option == "nextw":
                diahoraselected = diahoraselected + timedelta(days=7)

            elif option == "selcel":
                codev = request.args.get("codev")
                cl.current(codev)
                obj = cl.current()
                diahoraselected = obj._diahoradate
                
                
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        
        
        objh = gerah(clh)
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        return render_template("hform.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),auto_number=cl.auto_number,
                        objh=objh,selectedcell = diahoraselected,
                        UnidadeCurric = UnidadeCurric.obj,
                        submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)

