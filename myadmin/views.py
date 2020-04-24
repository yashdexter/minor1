from django.shortcuts import render,redirect
from minor import models as mainmodel
from . import models
from django.conf import settings
curl=settings.CURRENT_URL
myadmin_curl = settings.ADMIN_CURRENT_URL

# Create your views here.
def adminhome(request):
    return render(request,"adminhome.html",{})

def manageuser(request):
    userDetails = mainmodel.Register.objects.filter(role='user')
    return render(request,"manageuser.html",{'myadmin_curl':myadmin_curl,'userDetails':userDetails,'curl':curl})
def manageuserstatus(request):
    s=request.GET.get("s")
    rid=request.GET.get("rid")
    if s=="block":
        mainmodel.Register.objects.filter(regid=int(rid)).update(status=0)
    elif s=="unblock":
        mainmodel.Register.objects.filter(regid=int(rid)).update(status=1)
    else:
        mainmodel.Register.objects.filter(regid=int(rid)).delete()
    return redirect(myadmin_curl+'manageuser/')
def managepost(request):
    return render(request,"managepost.html",{'curl':curl})
