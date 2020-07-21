from django.shortcuts import render

def homepage(request):
    return render(request, 'home/home-page.html', {'name':"Naedeezy"})

def reg(request):
    return render(request, 'home/reg.html')

def result(request):
    return render(request, 'home/result.html')

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    sum = val1 + val2
    return render(request,'home/result.html', {'result': sum})