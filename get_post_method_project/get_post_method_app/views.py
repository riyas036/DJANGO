from django.shortcuts import render

# Create your views here. 
def index(request):
    return render(request, "index.html")
def output(request):
    name=request.GET['name']
    password=request.GET['password']
    address=request.GET['address']
    email=request.GET['email']
    return render(request,"output.html",{'name':name,'password':password,'address':address,'email':email})
def back(request):
    return render(request,'index.html')