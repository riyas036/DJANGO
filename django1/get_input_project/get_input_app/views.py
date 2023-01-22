from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def product(request):
    mobile=int(request.GET["mobile"])
    keyboard=int(request.GET["keyboard"])
    monitor=int(request.GET["monitor"])
    price=mobile+keyboard+monitor
    return render(request, "product.html",{'price':price})