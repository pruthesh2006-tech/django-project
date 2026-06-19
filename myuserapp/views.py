from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.conf import settings
from .models import Student

# Create your views here.

def mailsenddemo(request):
    subject = 'Welcome to My Website '
    message = ' You are Selected as Employee'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['p@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")

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
    subject = 'Login Detected  '
    message = ' Someone has access you website Name is ',txt1
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['p@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)

def logout(request):
    del request.session['myemail']
    return redirect(loginpage)

def contactus(request):
    return render(request,'contactus.html')

def contactMe(request):
    Name = request.POST.get("name")
    Email = request.POST.get("email")
    Contact = request.POST.get("contact")

    mymsg = " Hello has Contact you",Name," Email is ",Email," Contact is ",Contact

    subject = 'Contact us from website'
    email_from = settings.EMAIL_HOST_USER

    message = mymsg
    recipient_list = ['p@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Thank you for Contacting us.")

def addstudentform(request):
    return render(request,"add-student.html")

def addstudentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    # Student.objects.create(sname=txt1,smobile=txt2,semail=txt3,saddress=txt4)
    # return HttpResponse("Thank you for signup")

    send_mail(
            "New Student Details",
            f"sname : {txt1}\n"
            f"smobile : {txt2}\n"
            f"semail : {txt3}\n"
            f"saddress : {txt4}",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
    )
    return render(request,"add-student.html")