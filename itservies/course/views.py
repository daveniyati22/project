from django.shortcuts import render

def home(request):
    return render (request,'home.html') 
def contact(request):
    return render (request,'contact.html')
def about(request):
    return render (request,'about.html')
def faculty(request):
    return render (request,'faculty.html')
def admissions(request):
    return render (request,'admissions.html')

