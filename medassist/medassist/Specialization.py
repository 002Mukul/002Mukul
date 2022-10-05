from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def SpecializationInterface(request):
    try:
        admin=request.session['admin']
        print("ADMINS",admin)
        return render (request,"wirst.html",{'msg':''})
    except Exception as e:
        return render (request,"Adminlogin.html",{'msg':''})


@xframe_options_exempt
def displayallspecialization(request):
     try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from specialization"
        cmd.execute(q)
        records=cmd.fetchall()
        db.commit()  
        return render(request,"DisplayAllSpecialization.html",{'result':records,'msg':''})
     except Exception as e:        
        return render(request,"DisplayAllSpecialization.html",{'result':'','msg':''})

@xframe_options_exempt
def specializationsubmit(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        specialization=request.POST['specialization']
        iconfile=request.FILES['icon']
        q="insert into specialization(specialization,icon) values('{0}','{1}')".format(specialization,iconfile.name) 
        print(q)
        cmd.execute(q)
        db.commit()  
        F=open("f:/medassist/assets/"+iconfile.name,"wb")
        for chunk in iconfile.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request,"wirst.html",{'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request,"wirst.html",{'msg':'Fail to submit record'})

@xframe_options_exempt
def UpdateSpecialization(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        specialization=request.GET['specialization']
        specializationid=request.GET['specializationid']
        q="update specialization set specialization='{0}' where specializationid={1}".format(specialization,specializationid)
        cmd.execute(q)
        db.commit()         
        return JsonResponse({"result":True,}, safe=False)   
    except Exception as e:
        print(e)
        return JsonResponse({"result":False,}, safe=False)

@xframe_options_exempt
def DeleteSpecialization(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        specializationid=request.GET['specializationid']
        q="delete from  specialization where specializationid={0}".format(specializationid)
        cmd.execute(q)
        db.commit()  
        db.close()       
        return JsonResponse({"result":True,}, safe=False)   
    except Exception as e:
        print(e)
        return JsonResponse({"result":False,}, safe=False)

@xframe_options_exempt
def EditSpecialization(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        specializationid=request.POST['specializationid']
        iconfile=request.FILES['icon']
        print("hello",specializationid,iconfile.name) 
        q="update  specialization set icon='{0}' where specializationid={1}".format(iconfile.name,specializationid)
        cmd.execute(q)
        db.commit() 
        F=open("f:/medassist/assets/"+iconfile.name,"wb")
        for chunk in iconfile.chunks():
            F.write(chunk)
        F.close()  
        db.close()                   
        return JsonResponse({"result":True,}, safe=False)   
    except Exception as e:
        print(e)
        return JsonResponse({"result":False,}, safe=False)

@xframe_options_exempt
def displayallspecializationJSON(request):

    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from specialization"
        cmd.execute(q)
        records=cmd.fetchall()
        db.commit()  
        return JsonResponse({"result":records,}, safe=False)
    except Exception as e:        
        return JsonResponse({"result":{},}, safe=False)
