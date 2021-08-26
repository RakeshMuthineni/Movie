from urllib import request

from django.shortcuts import render,redirect
from django.http import HttpResponse
from Rating.models import Cinima_Info
from django.views.generic.edit import UpdateView
# Create your views here.
from Rating.forms import Cinima_InfoForm,Cinima_InfoModelform


def info_view(request):
    cini=Cinima_Info.objects.all().order_by('-id')
    return render(request,'htmlpage/home.html',{'cini':cini})


def htmlform_view(request):
    if request.method=="POST":
        mname=request.POST['mname']
        print(request.FILES['poster'])
        mvs=Cinima_Info(Name=mname,Desc=request.POST['desc'],Budget=request.POST['budget'],Director=request.POST['director'],Hero=request.POST['hero'],Heroin=request.POST['heroin'],poster=request.FILES['poster'])
        mvs.save()
        return redirect('mahesh')
    return render(request,'forms/htmlform.html')

def djangoform_view(request):
    form=Cinima_InfoForm()
    if request.method == "POST":

        mvs = Cinima_Info(Name=request.POST['mname'], Desc=request.POST['desc'], Budget=request.POST['budget'],
                          Director=request.POST['director'], Hero=request.POST['hero'], Heroin=request.POST['heroin'],
                          poster=request.FILES['poster'])
        mvs.save()
        return redirect('mahesh')

    return render(request, 'forms/djangoform.html',{'form':form})

def modelform_view(request):
    form=Cinima_InfoModelform()
    if request.method == "POST":
        form = Cinima_InfoModelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mahesh')

    return render(request, 'forms/modelform.html', {'form': form})

def delete_view(request,id):
    return render(request,'htmlpage/delete.html',{'did':id})

def delete_confirm(request,id):
        cinima = Cinima_Info.objects.get(id=id)
        cinima.delete()
        return redirect('mahesh')
def update_view(request,id):
    edit1 = Cinima_Info.objects.get(id=id)
    if request.method == "POST":
        Name=request.POST['mname']
        Hero = request.POST['hero']
        Heroin = request.POST['heroin']
        Director = request.POST['director']
        Budget = request.POST['budget']
        Desc=request.POST['desc']
        poster = request.FILES['poster']
        edit = Cinima_Info.objects.get(id=id)
        edit.Name=Name
        edit.Hero=Hero
        edit.Heroin=Heroin
        edit.Director=Director
        edit.Budget=Budget
        edit.Desc= Desc
        edit.poster= poster
        edit.save()
        return redirect('mahesh')
    return render(request,'htmlpage/update.html',{'edit1':edit1})
