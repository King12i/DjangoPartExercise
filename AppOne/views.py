from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def show_all(request):
    return HttpResponse("This is the page that will show all things")

def platypus(request):
    return redirect('/dashboard/orange')

def yellow_shoe(request):
    return HttpResponse("You're at the yellow shoe!")

def ear(request):
    return HttpResponse("you're at the ear!")

def pumpernickel(request):
    return redirect('/home/showallthings')

def beyonce(request, whatsmyname):
    return HttpResponse(f"My name is {whatsmyname}")