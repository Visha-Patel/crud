from django.shortcuts import render,HttpResponseRedirect
from .models import Collage
 

def ins(request):
    return render(request,'inser/insert.html')

def dis(request):
    d=Collage.objects.all()
    return render(request,'inser/display.html',{'data':d})

def insert(request):
    if request.method=="POST":
        print(request.POST)
        nm=request.POST.get('nme')
        em=request.POST.get('eml')
        cn=request.POST.get('cnt')
        rl=request.POST.get('rln')
        cl=request.POST.get('cls')
        cr=request.POST.get('crs')
        im=request.FILES.get('img')
        d=Collage(name=nm,email=em,contact=cn,rollno=rl,clas=cl,course=cr,img=im)
        d.save()
    return render(request,"inser/insert.html")
def dele(request,id):
        k=Collage.objects.get(pk=id)
        k.delete()
        return render(request,"inser/delete.html")
def update(request,id):
          if request.method=="POST":
                a=request.POST.get('nme')
                b=request.POST.get('eml')
                c=request.POST.get('cnt')
                d=request.POST.get('rln')
                e=request.POST.get('cls')
                f=request.POST.get('crs')
                g=request.FILES.get('img')
                if g==None:
                    Collage.objects.filter(id=id).update(name=a,email=b,contact=c,rollno=d,course=e,clas=f)
                    return render(request,'inser/display.html')
                else:
                      data=Collage(id=id,name=a,email=b,contact=c,rollno=d,course=e,clas=f,img=g)
                      data.save()
                      return render(request,'inser/display.html')
          d1=Collage.objects.get(pk=id)
          return render(request,'inser/update.html',{'data':d1})
          
     
    
