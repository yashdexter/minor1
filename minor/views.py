from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from . import models
curl = settings.CURRENT_URL
user_curl = settings.USER_CURRENT_URL
myadmin_curl=settings.ADMIN_CURRENT_URL
import time
dt=time.strftime("%d/%m/%Y-%H:%M:%S")
#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
    def middleware(request):
        if request.path=='' or request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/login/' or request.path=='/service/' or request.path=='/register/':
            request.session['enm']=None
            request.session['srole']=None

            response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware

def home(request):
    return render(request,'index.html',{'curl':curl})

def register(request):
    if request.method=="GET":
        return render(request,"register.html",{'curl':curl,'output':''})
    else:

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        enrollmentnumber = request.POST.get("enrollmentnumber")
        college = request.POST.get("college")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        #enrollmentnumber=enrollmentnumber.lower()


        if models.Register.objects.filter(enrollmentnumber=enrollmentnumber):
            return render(request,"register.html",{'curl':curl,'output':'account exists'})

        else:
            p=models.Register(name=name,email=email,password=password,enrollmentnumber=enrollmentnumber,college=college,mobile=mobile,address=address,city=city,gender=gender,status=0,role='user',dt=dt)
            enro=p.enrollmentnumber
            enro1=enro.lower()
            s=models.Register(name=name,email=email,password=password,enrollmentnumber=enro1,college=college,mobile=mobile,address=address,city=city,gender=gender,status=0,role='user',dt=dt)
            s.save()
            return render(request,"register.html",{'curl':curl,'output':'Completed your registration succesfully'})


def login(request):
        if request.method=="GET":
            return render(request,"login.html",{'curl':curl,'output':''})

        else:
            enrollmentnumber = request.POST.get("enrollmentnumber")
            password = request.POST.get("password")

            userDetails = models.Register.objects.filter(enrollmentnumber=enrollmentnumber,password=password,status=1)
            #this return array of object

            if len(userDetails)>0:
                request.session['enm']=userDetails[0].enrollmentnumber
                request.session['srole']=userDetails[0].role
                if userDetails[0].role=="admin":
                    return redirect(curl+'myadmin/')
                else:
                    return redirect(curl+'user/')
            else:
                return render(request,"login.html",{'curl':curl,'output':'Invalid Username or Password'})
