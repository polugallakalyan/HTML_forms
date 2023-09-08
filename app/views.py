from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        To=Topic.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=To,name=na,url=ur)[0]
        wo.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def select_and_display(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tnlist=request.POST.getlist('tn')
        print(tnlist)

        QSWO=Webpage.objects.none()

        for tn in tnlist:
            QSWO=QSWO|Webpage.objects.filter(topic_name=tn)

        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_and_display.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)

def radio_button(request):
    LTO=Topic.objects.all()
    wo=Webpage.objects.filter(pk=2).delete()
    wo=Webpage.objects.all()
    d={'LTO':LTO}
    
    return render(request,'radio_button.html',d)