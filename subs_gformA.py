from flask import Flask, render_template, request, session
from classes.event import Event
from classes.participant import Participant
from classes.registration import Registration
from classes.type import Type
from classes.venue import Venue
from classes.feedback import Feedback
from classes.userlogin import Userlogin
from datafile import filename
prev_option = ""

def gformA(cname='',submenu=""):
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            
            # Criado por nós
            approval = obj.chk_validity()
            print(approval)
            if approval == 'Approved!':
                cl.insert(getattr(obj, cl.att[0]))
                cl.last()
                return render_template("gformA.html", butshow=butshow, butedit=butedit,
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),auto_number=cl.auto_number,
                                submenu=submenu, resul=approval,usergroup=session.get('usergroup'))
            else:
                cod = getattr(obj, cl.att[0])
                del cl.obj[cod]
                cl.read(filename + 'business.db')
                return render_template("gformA.html", butshow='disabled', butedit='enabled',
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),auto_number=cl.auto_number,
                                submenu=submenu, resul=approval,usergroup=session.get('usergroup'))
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
           
                
                if (cl.auto_number == 1):
                    strobj = "None"
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"),usergroup=session.get('usergroup'))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        return render_template("gformA.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),usergroup=session.get('usergroup'), auto_number=cl.auto_number,
                        submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)
