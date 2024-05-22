# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

"""""
from flask import Flask, render_template, request, session
from classes.participant import Participant
from classes.event import Event
from classes.venue import Venue
from classes.type import Type
from classes.registration import Registration
from classes.feedback import Feedback
from classes.userlogin import Userlogin
from datafile import filename

prev_option = ""

def subform(cname="",submenu=""):
    global prev_option
    tlist = cname.split('_')
    cnames = tlist[0]
    scname = tlist[1]
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cnames)
        sbl = eval(scname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == None: # pode comprometer futuras ações
            option = ''
        if prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            
            # Criado por nós
            approval = cl.chk_validity()
            if approval == 'Approved!':
                cl.insert(getattr(obj, cl.att[0]))
                cl.last()
                return render_template("subform.html", butshow=butshow, butedit=butedit,
                            cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                            ulogin=session.get("user"),headerl=sbl.header,
                            desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number,
                            submenu=submenu, resul=approval)
            else:
                cod = getattr(obj, cl.att[0])
                del cl.obj[cod]
                cl.read(filename + 'project.db')
                return render_template("subform.html", butshow='disabled', butedit='enabled',
                            cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                            ulogin=session.get("user"),headerl=sbl.header,
                            desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number,
                            submenu=submenu, resul=approval)
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
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                for line in lines:
                    sbl.remove(line)
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
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                print(row,lines[row])
                sbl.remove(lines[row])
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
                obj = cl.current()
                strobj = getattr(obj, cl.att[0])
                for i in range(1,len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                objl = sbl.from_string(strobj)
                                
                
                # Criado por nós #!!!
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                objlst = list()
                for line in lines:
                    objlst.append(sbl.obj[line])
                approval = objl.chk_validity()
                #x = input(f'{objl}::')
                if approval == 'Approved!':
                    cod = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                    sbl.insert(cod)
                    #x = input(f'{lst_att}::')
                    return render_template("subform.html", butshow=butshow, butedit=butedit,
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),objl=objlst,headerl=sbl.header,
                                desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number,
                                submenu=submenu, resul=approval)
                else:
                    cod = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                    del sbl.obj[cod]
                    sbl.read(filename + 'project.db')
                    return render_template("subform.html", butshow='disabled', butedit='disabled_esp',
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),objl=objlst,headerl=sbl.header,
                                desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number,
                                submenu=submenu, resul=approval)
                
                
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user")) 
        prev_option = option
        obj = cl.current()
        headers = list()
        objl = list()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        else:
            for i in range(1, len(sbl.att)): 
                    headers.append(sbl.att[i][1:])        
            lines = sbl.getlines(getattr(obj, cl.att[0])) 
            for line in lines:
                objl.append(sbl.obj[line])
        return render_template("subform.html", butshow=butshow, butedit=butedit,
                    cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                    ulogin=session.get("user"),objl=objl,headerl=sbl.header,
                    desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number,
                    submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)