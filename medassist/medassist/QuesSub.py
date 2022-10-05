from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
from django.views.decorators.clickjacking import xframe_options_exempt

def Question(request):
    return render (request,"QuestionList.html",{'msg':''})
def QuestionList(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        print("mjhgfdsdfghj")
        q="Select Q.*,(select S.subquestion from subquestion S where S.questionid=Q.questionid) From questiontable Q"     
        cmd.execute(q)
        data=cmd.fetchall()
        print(data)
        db.commit
        db.close()
        return render(request,"QuestionList.html",{'msg':''})
    except Exception as e:
        print("message",e)
def SurveyForm(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from Doctor where specializationid={0}".format('spid')
        cmd.execute(q)
        record=cmd.fetchall
        print(record)
        db.commit()
        db.close()

    except Exception as e:
        print("hii")

    
