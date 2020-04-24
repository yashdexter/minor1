from django.shortcuts import render
from django.conf import settings
curl = settings.CURRENT_URL
user_curl=settings.USER_CURRENT_URL
myadmin_curl=settings.ADMIN_CURRENT_URL
import time
from . import models
dt=time.strftime("%d/%m/%Y-%H:%M:%S")

def sessioncheckuser_middleware(get_response):
	def middleware(request):
		if request.path=='/user/':
			if request.session['enm']==None or request.session['srole']!="user":
				response = redirect(curl+'login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)
		return response
	return middleware

def userhome(request):
    return render(request,"userhome.html",{'user_curl':user_curl})
def addpost(request):
    if request.method=="GET":
        return render(request,"addpost1.html",{myadmin_curl:'myadmin_curl',user_curl:'user_curl','output':''})
    else:
        title=request.POST.get("title")
        description = request.POST.get("description")
        category= request.POST.get("category")
        p=models.Post(title=title,description=description,category=category,dt=dt,enrollmentnumber=0,status=0)
        p.save()
        return render(request,"addpost1.html",{'myadmin_curl':myadmin_curl,user_curl:'user_curl','output':'your post is uploaded but not verified'})

def viewpost(request):
    return render(request,"viewpost.html",{'user_curl':user_curl})
def viewdeeppost(request):
    return render(request,"viewdeeppost.html",{'user_curl':user_curl,'curl':curl})
