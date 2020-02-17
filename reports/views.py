from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.

now = timezone.now()

@csrf_exempt
def Post_report(request,user_id):
    if request.method == 'POST':
        msg = request.body.decode('utf-8')
        textm = json.loads(msg)
        robj = ReportersTable.objects.get(id = user_id)
        rep = ReportsTable(text = textm['text'], date = timezone.now().strftime('%Y-%m-%d'), reporter = robj)
        rep.save()
        myJson = {"response" : "done"}
        return JsonResponse(myJson)

def Get_for_update(request,user_id):
    ls = []
    ls1 = []
    if request.method == 'GET':
        ls = ReportsTable.objects.filter(reporter = user_id)
        for rep in ls:
            mjs = {"id" : rep.id , "text" : rep.text , "date" : str(rep.date)}
            ls1.append(mjs)
        myJson = {"response"  : ls1}
        return JsonResponse(myJson)
    
def Visit_reporter(request):
    print(" ##### ", request.user)
    print(" ****** ",type(request.user))
    ls = []
    ls1 = []
    if request.method == 'GET':
        ls = ReportersTable.objects.all()
        for rep in ls:
            mjs = {"id" : rep.id , "name" : rep.name}
            ls1.append(mjs)
        myJson = {"response"  : ls1}
        return JsonResponse(myJson)

@csrf_exempt
def Update_report(request, report_id):
    ls = []
    if request.method == 'PUT':
        ls = ReportsTable.objects.filter(id = report_id)
        rep = ls[0]
        msg = request.body.decode('utf-8')
        textm = json.loads(msg)
        rep.text = textm['text']
        rep.save()
        myJson = {"response" : "updated"}
        return JsonResponse(myJson)

@csrf_exempt
def Get_report(request, stdate):
    ls = []
    ls1 = []
    ls = ReportsTable.objects.filter(date = str(stdate))
    for i in ls:
        r = {"text" : i.text , "date" : str(i.date) , "reporter" : i.reporter.name}
        ls1.append(r)
    myJson = {"response" : ls1}
    return JsonResponse(myJson , safe = False)# safe ro ke false mikoni mishe list ham 
    # mishe ferestad

@csrf_exempt
def Delete_report(request , report_id):
    if request.method == 'DELETE':
        try:
            rep = ReportsTable.objects.get(id = report_id)
            rep.delete()
        # ls = list(ReportsTable.objects.all())
            myJson = {"response" : "done"}
        except Exception as e:
            e = str(e)
            myJson = {"erroe" : e}
        return JsonResponse(myJson)


