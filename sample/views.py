from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Register,project
from django.http import HttpResponse
from django.conf import settings
import random
def index(request):
    return render(request,"home.html")
def photo(request):
    return render(request,"p.html")
def register(request):
    return render(request,"register.html")
def RegisterUpload(request):
    if request.method=='POST':
        n=request.POST['Name']
        p=request.POST['Password']
        R=Register(
            Name=n,
            Password=p
        )
        R.save()
    return redirect('/')
def take(request):
        if 'save' in request.POST:
            uname=request.POST['uname']
            pw=request.POST['password']
            f=Register.objects.values_list('Name')
            l=[]
            for i in range(len(f)):
                l.append(f[i][0])
            if(uname in l):
                k=Register.objects.get(Name__exact=uname)
                if(k.Password==pw):
                    name=request.POST['name'] 
                    e=request.POST['e_mail']
                    phone=request.POST['phone']
                    img=request.FILES['img']
                    nop=request.POST['name_of_product']
                    des=request.POST['description']
                    uid=random.randrange(1000,100000)
                    p=project(
                        uname=uname,
                        name=name,
                        email=e,
                        phone=phone,
                        i=img,
                        Name_of_Product=nop,
                        description=des,
                        u_id=uid
                    )
                    p.save()
                    return render(request,"upload_success.html",{"a":uid})
                else:
                    return render(request,"incorrect.html")
            else:
                return render(request,"incorrect.html")
        elif 'delete' in request.POST:
            return render(request,"delete.html")
        else:
            form=project.objects.all()
            return render(request,"show.html",{"p":form})
def about(request):
    return render(request,"about.html")
def mail_to(request):
    return render(request,"mail.html")
def mail(request):
    if request.method=='POST':
        a=request.POST['smail']
        b=request.POST['rmail']
        message=request.POST['message']
        recipient_list =[b,]
    #recipient_list = ['vislavathsrinath125@gmail.com',]  settings.EMAIL_HOST_USER
    send_mail("Hello!!",message,a,recipient_list,fail_silently=False)
    return redirect('/')
def delete(request):
    if request.method=='POST':
        pid=request.POST['pid']
        instance = project.objects.get(u_id=pid)
        instance.delete()
    return redirect('/')


# Create your views here.
