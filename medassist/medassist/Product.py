from django.shortcuts import render
from . import Pool
import random

def ProductInterface(request):
    return render(request,"Product list.html",{'msg':''})
def ProductSubmit(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        productcatagory=request.POST['product']
        iconfile=request.FILES['icon']
        q="insert into producttable(ProductC,ProductI) values('{0}','{1}')".format(productcatagory,iconfile.name) 
        print(q)
        cmd.execute(q)
        db.commit()  
        F=open("f:/medassist/assets/"+iconfile.name,"wb")
        for chunk in iconfile.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request,"Product list.html",{'msg':'Record Submitted'})
    except Exception as e:
        print('text',e)
        return render(request,"Product list.html",{'msg':'Fail to submit record'})
def StaffLogin(request):
    return render(request,"Stafflogin.html",{'msg':''})

def CheckStaffLogin(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        email=request.POST['email']
        password=request.POST['password']
        q = "select * from stafflogin where emailaddress='{0}' and password='{1}'".format(email,password)
        cmd.execute(q)
        records=cmd.fetchone  
        if(records):  
         return render(request, 'Dashboard.html', {'msg':'','data':records})
        else:
            print('hello',records)
            return render(request, 'Product list.html', {'msg': "Invalid EmailId/Password"})

    except Exception as e:
        print(e)
        return render(request, 'AdminLogin.html', {'msg': 'Server Error'})
def LoginOption(request):
    return render(request,'Frontpage.html',{'msg':''})
def UserInterface(request):
    return render(request,"Userreg.html",{'msg':''})
def UserSubmit(request):

    try:
        db,cmd=Pool.ConnectionPooling()
        name=request.POST['username']
        email=request.POST['useremail']
        number=request.POST['umb']
        dob=request.POST['udob']
        password=request.POST['upasswd']
        q="insert into Usertable(Username,Useremail,Usermobile,Userdob,Userpassword) values('{0}','{1}',{2},'{3}','{4}')".format(name,email,number,dob,password)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request,"Userreg.html",{'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request,"userreg.html",{'msg':'Record not submitted'})
def CheckUser(request):    
    btn=request.POST['btn']
    if(btn=="Login"):
        db,cmd=Pool.ConnectionPooling()
        Mobilenumber=request.POST['umb']
        print(Mobilenumber)
        q="select * from Usertable where Usermobile='{}'".format(Mobilenumber)
        cmd.execute(q)
        data=cmd.fetchone()
        if(data):   
            q="select * from producttable"
            cmd.execute(q)
            records=cmd.fetchall()
            print(records) 
            return render(request,"CartScreen.html",{'msg':'','Result':records})            
        else:
            return render (request,"LoginM.html",{'msg':'Invalid mobile number'})
    else:
        return render(request,"LoginM.html",{'msg':''})
def Loginm(request):
    return render(request,"LoginM.html",{'msg':''})
def Addcart(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        prid=request.GET['proid']
        print(prid)
        prata=request.GET['prcata']
        print(prata)
        pricn=request.GET['pricon']
        print(pricn)
        q="insert into carttable(productid,productname,picofproduct) values('{0}','{1}',{2},)".format(prid,prata,pricn)
        cmd.execute(q)
        result=cmd.fetchall()
        print(result)
        db.commit()
        db.close()
        return render(request,"CartScrren.html",{'msg':''})
    except Exception as e:
        return render(request,"CartScreen.html",{'msg','Not added to your cart'})
def ShowItem(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from addcarttable"
        cmd.execut(q)
        records=cmd.fetchall()
        return render(request,"show.html",{'result':records})
    except Exception as e:
        return render(request,"Cartscreen.html",{'msg':''})




    
































