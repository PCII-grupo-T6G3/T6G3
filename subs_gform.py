# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

"""""
from flask import render_template, request, session
from datafile import filename

prev_option = ""

def gform(cname='',submenu=""):
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
            # if cl == Event:
            #     for i in range(1,len(cl.att2)):
            #         strobj += ";" + request.form[cl.att[i]]
            #     obj = cl.from_string(strobj)
            # else:
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            
            # Criado por nós
            approval = obj.chk_validity()
            if approval == 'Approved!':
                cl.insert(getattr(obj, cl.att[0]))
                cl.last()
                return render_template("gform.html", butshow=butshow, butedit=butedit,
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),auto_number=cl.auto_number,
                                submenu=submenu, resul=approval,usergroup=session.get('usergroup'))
            else:
                cod = getattr(obj, cl.att[0])
                del cl.obj[cod]
                cl.read(filename)
                return render_template("gform.html", butshow='disabled', butedit='enabled',
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),auto_number=cl.auto_number,
                                submenu=submenu, resul=approval,usergroup=session.get('usergroup'))
            
        elif prev_option == 'edit' and option == 'save': # 100% criado por nós
            obj = cl.current()
            strobj_temp = 'temp'
            for i in range(1,len(cl.att)):
                strobj_temp += ";" + request.form[cl.att[i]]
            obj_temp = cl.from_string(strobj_temp)
            
            approval = obj_temp.chk_validity()
            if approval == 'Approved!':
                cl.obj[getattr(obj, cl.att[0])] = obj_temp
                obj_temp._code = obj._code
                del cl.obj['temp']
                cl.update(getattr(obj, cl.att[0]))
                cl.read(filename)
                obj = cl.obj[getattr(obj, cl.att[0])]
                return render_template("gform.html", butshow=butshow, butedit=butedit,
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),auto_number=cl.auto_number,
                                submenu=submenu, resul=approval,usergroup=session.get('usergroup'))
            else:
                del cl.obj['temp']
                cl.read(filename)
                return render_template("gform.html", butshow='disabled', butedit='enabled',
                                cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                ulogin=session.get("user"),auto_number=cl.auto_number,
                                submenu=submenu, resul=approval,usergroup=session.get('usergroup'))
            
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                
                # Criado por nós
                approval_r = obj.chk_removal()
                if approval_r == 'Deleted!':
                    cl.remove(obj.code)
                    if not cl.previous():
                        cl.first()
                    return render_template("gform.html", butshow=butshow, butedit=butedit,
                                    cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                    ulogin=session.get("user"),auto_number=cl.auto_number,
                                    submenu=submenu, resul=approval_r,usergroup=session.get('usergroup'))
                else:
                    return render_template("gform.html", butshow=butshow, butedit=butedit,
                                    cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                                    ulogin=session.get("user"),auto_number=cl.auto_number,
                                    submenu=submenu, resul=approval_r,usergroup=session.get('usergroup'))
                    
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
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"),usergroup=session.get('usergroup'))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        return render_template("gform.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),usergroup=session.get('usergroup'),auto_number=cl.auto_number,
                        submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)