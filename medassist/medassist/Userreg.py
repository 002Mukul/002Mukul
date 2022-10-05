from django.shortcuts import render,redirect
from . import Pool
import random
def UserRegistration(request):
    return render (request,"user.html",{'msg':''})
def UserLogin(request):
    return render (request,"signin.html",{'msg':''})
def OTPverified(request):
    btn=request.POST['btn']
    if(btn=="Login"):

        db,cmd=Pool.ConnectionPooling()
        Mobilenumber=request.POST['umb']
        q="select * from userregistration where Umobileno='{}'".format(Mobilenumber)
        cmd.execute(q)
        data=cmd.fetchone()
        if(data):
            otp=random.randint(1000,9999)
            print(otp)
            request.session['userdata']=data['Username']
            return render(request,"ConfirmOtp.html",{'otp':otp})            
        else:
            return render (request,"signin.html",{'msg':'Invalid mobile number'})
    else:
        return render(request,"signin.html",{'msg':''})    
def SubmitUser(request):
    try:      
        db,cmd=Pool.ConnectionPooling()
        username=request.POST['username']
        state=request.POST['usercity']
        usernumber=request.POST['umb']
        useremail=request.POST['useremail']
        userdob=request.POST['udob']
        usertor=request.POST['utor']
        userpasswd=request.POST['upasswd']
        q="insert into userregistration(Username,Ustate,Uemailid,Umobileno,Udob,Upassword,Utor) values('{0}','{1}','{2}',{4},'{5}','{6}')".format(username,state,useremail,usernumber,userdob,userpasswd,usertor) 
        cmd.execute(q)
        db.commit()  
        db.close()
        return render(request,"signemail.html",{'msg':'this is right user'})
    except Exception as e:
        print(e)
        return render(request,"user.html",{'msg':'Fail to submit record'})

def FrontPage(request):
    return render (request,"Frontpage.html",{'msg':''})
def Signemail(request):
    return render (request,"signemail.html",{'msg':''})
def ForgetPass(request):
    return render(request,"Forgetpass.html",{'msg':''})
def CheckMobileNumber(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        Mobilenumber=request.POST['umb']
        q="select * from userregistration where Umobileno={}".format(Mobilenumber)
        cmd.execute(q)
        data=cmd.fetchone()
        if(data):
            return render(request,"WomacSurveys.html",{'msg':''})
    except Exception as e:
        return render(request,"WomacSurveys.html",{'msg':''})
def ChkOtp(request):
    d1=request.POST['digit1']
    d2=request.POST['digit2']
    d3=request.POST['digit3']
    d4=request.POST['digit4']
    gotp=request.POST['gotp']
    iotp=d1+d2+d3+d4
    if(gotp==iotp):
        return WomacForm(request)
    else:
        return render(request,"signin.html",{'msg':''})
def WomacForm(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from doctorregistration"
        cmd.execute(q)
        data=cmd.fetchall()   
        return render(request,"WomacForm2.html",{'msg':'','Data':data,'UserName':request.session['userdata']})
    except Exception as e:
        print("message",e)

         
        



    



