from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def homepageview(request):
    return render(request,'home.html')
def aboutpageview(request):
    return render(request,'about.html')    
def contactpageview(request):
    return render(request,'contact.html')
def shoppage(request):
    return render(request,'shop.html')

def contactprocess(request):
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b
    msg = "A value is",a,"B value is",b,"Sum is ",c
    
    d = ""
    if c == 30:
        d = "if condition called"
    elif c<30:
        d = "elseif called"
    else:
        d = "else called"
    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d})