from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def DoctorInterface(request):
    try:
        admin=request.session['admin']
        return render(request,"Doctor.html",{'msg':''})
    except Exception as e:
        return render(request,"Adminlogin.html",{'result':'','msg':''})


@xframe_options_exempt
def DisplayAllDoctor(request):
    try:
        db,cmd=Pool.ConnectionPooling()       
        q="Select D.*,(select S.specialization from specialization S where S.specializationid=D.speciality) as tspecialization  From doctorregistration D"
        cmd.execute(q)   
        records=cmd.fetchall()        
        db.commit()
        return render(request,"DisplayAllDoctor.html",{'result':records})
    except Exception as e:
        print(e)
        return render(request,"DisplayAllDoctor.html",{'result':{ }})

@xframe_options_exempt
def DoctorSubmit(request):
    try:
        db,cmd=Pool.ConnectionPooling()       
        Doctorname=request.POST['drs'] 
        Dob=request.POST['drdob']
        Gender=request.POST['drg']
        Mobileno=request.POST['drmo']
        Emailaddress=request.POST['drem']
        Speciality=request.POST['spl']
        Profilepicturefile=request.FILES['drimg']
        q="insert into doctorregistration(Doctorname,Dob,Gender,Mobileno,Emailaddress,Speciality,Profilepicture)values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(Doctorname,Dob,Gender,Mobileno,Emailaddress,Speciality,Profilepicturefile.name)
        cmd.execute(q)
        db.commit()    
        F=open("f:/medassist/assets/"+Profilepicturefile.name,mode="wb")
        for chunk in Profilepicturefile.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request,"Doctor.html",{'msg':'Record Submitted'})

    except Exception as e:
        print(e)
        return render(request,"Doctor.html",{'msg':'Fail to submit Record'})

@xframe_options_exempt
def Updatedoctor(request):
    try:
        db,cmd=Pool.ConnectionPooling()       
        Doctorname=request.GET['drcs'] 
        Doctorid=request.GET['drcid']   
        print("hello",Doctorname,Doctorid)          
        q="update doctorregistration set Doctorname='{0}' where Doctorid={1}".format(Doctorname,Doctorid)
        cmd.execute(q)        
        db.commit()  
        db.close()     
        return JsonResponse({'result':True,},safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'result':False,},safe=False)

@xframe_options_exempt
def Deletedoctor(request):
    try:
        db,cmd=Pool.ConnectionPooling()       
        Doctorid=request.GET['drcid']           
        q="delete from doctorregistration where Doctorid={0}".format(Doctorid)
        cmd.execute(q)        
        db.commit()  
        db.close()     
        return JsonResponse({'result':True,},safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'result':False,},safe=False)

@xframe_options_exempt
def EditDoctorIcon(request):
    try:
        db,cmd=Pool.ConnectionPooling()       
        Doctorid=request.POST['drid']
        Profilepicturefile=request.FILES['drimg']
        q="update doctorregistration set where Profilepicture={0} Doctorid={1}".format(Profilepicturefile.name,Doctorid)
        cmd.execute(q)        
        db.commit()
        F=open("f:/medassist/assets/"+Profilepicturefile.name,mode="wb")
        for chunk in Profilepicturefile.chunks():
            F.write(chunk)
        F.close()
        db.close()   
        return JsonResponse({'result':True,},safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'result':False,},safe=False)



        





