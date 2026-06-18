from django.shortcuts import render,redirect
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

def saveSessionData(request):
    request.session['username'] = 'Pruthesh Shah'
    return HttpResponse("Session Created")

def getSessionData(request):
    if request.session.has_key('username'):
        msg = request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("Session Variable not Present")
    
def deleteSessionData(request):
    del request.session['username']
    return HttpResponse("Session removed")

def getSessionData2(request):
    msg = request.session['username']
    return HttpResponse(msg)

def loginpage(request):
    return render(request,'login.html')

def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)

def logout(request):
    del request.session['myemail']
    return redirect(loginpage)
