from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def DoctorQuestionary(request):
    try:
        admin=request.session['admin']
        return render(request,"question.html",{'msg':''})
    except Exception as e:
        return render(request,"Adminlogin.html",{'result':'','msg':''})

@xframe_options_exempt
def SubQuestionary(request):
    try:
        admin=request.session['admin']
        return render(request,"subquestion.html",{'msg':''})
    except Exception as e:
        return render(request,"Adminlogin.html",{'result':'','msg':''})


@xframe_options_exempt
def SubQuestioanrySubmit(request):
    try:            
        db,cmd=Pool.ConnectionPooling()        
        splid=request.GET['subspl']
        qid=request.GET['subque']  
        subqid=request.GET['questionid']      
        subq=request.GET['question']
        q="insert into subquestion(specializationid,questionid,subquestionnumber,subquestion)values('{0}','{1}','{2}','{3}')".format(splid,qid,subqid,subq)
        cmd.execute(q)
        db.commit()
        db.close
        return render(request,"subquestion.html",{'msg':'submitted record'})
    except Exception as e:
        print(e)
        return render(request,"subquestion.html",{'msg':'Fail to submit record'}) 

@xframe_options_exempt  
def QuestionSubmit(request):
    try:         
            db,cmd=Pool.ConnectionPooling()            
            qno=request.GET['question']
            splid=request.GET['specialization']
            Question=request.GET['Qestion']
            q="insert into questiontable(specializationid,questionno,question)values('{0}','{1}','{2}')".format(splid,qno,Question)
            cmd.execute(q)        
            db.commit()
            db.close
            return render(request,"question.html",{'msg':'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request,"question.html",{'msg':'Fail to submit Record'})

@xframe_options_exempt
def SubQuestionDisplay(request):
    try:
        db,cmd=Pool.ConnectionPooling() 
        splid=request.GET['specializationid']      
        q="select * from questiontable where specializationid={0}".format(splid)
        cmd.execute(q)   
        records=cmd.fetchall()   
        print(records)   
        db.close
        return JsonResponse({"result":records,}, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"result":records,}, safe=False)


    