from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method == 'POST':
        Topic_Name=request.POST['tn']
        TO=Topic.objects.get_or_create(Topic_Name=Topic_Name)[0]
        TO.save()
        return HttpResponse('Data Inserted Successfully In Topics')
    return render(request,'insert_topic.html')



def insert_webpage(request):
    if request.method == 'POST':
        Topic_Name=request.POST['tn']
        Name=request.POST['na']
        URL=request.POST['url']

        TO=Topic.objects.get(Topic_Name=Topic_Name)
        WO=Webpage.objects.get_or_create(Topic_Name=TO,Name=Name,URL=URL)[0]
        WO.save()
        return HttpResponse('Data Inserted Successfully In Webpage')
    return render(request,'insert_webpage.html')



def insert_accessrecord(request):
    if request.method == 'POST':
        Name=request.POST['na']
        Date=request.POST['dt']
        Author=request.POST['au']

        WO=Webpage.objects.get(Name=Name)
        AO=AccessRecord.objects.get_or_create(Name=WO,Date=Date,Author=Author)[0]
        AO.save()

        return HttpResponse('Data Inserted Successfully In AccessRecord')
    return render(request,'insert_accessrecord.html')





