from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def elephanttoe(request):
    return HttpResponse("You are at the elephant's toe")

def beansprout(request):
    return HttpResponse("You are at the beansprout!")

def octopus(request):
    return HttpResponse("You are at the octopus!")

def yes(request):
    return redirect('/dashboard/no')

def fungus(request):
    return redirect('/home/duckbill')

def rubberducky(request, numberofgreenhouses):
    return HttpResponse(f"I have {numberofgreenhouses} toenails!")