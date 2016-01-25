from django.shortcuts import render
from .models import paints
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from mysite.serializers import Serializer
from rest_framework import generics
from django.contrib.auth.models import User
from  mysite.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class List(generics.ListCreateAPIView):
    queryset=paints.objects.all()
    serializer_class=Serializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
    
class Detail(generics.RetrieveUpdateDestroyAPIView):
        queryset=paints.objects.all()
        serializer_class=Serializer
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
        queryset=User.objects.all()
        serializer_class=UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({'users':reverse('UserList',request=request,format=format),
                     'paints':reverse('List',request=request,format=format)})
    
# Create your views here.

def add(request):
    data=paints.objects.values('name','price','availability','image')
    return render(request,'add.html',{'data':data})

@csrf_exempt
def compare(request):   
    ty=[]
    for key in request.POST:
        query=paints.objects.get(name=request.POST[key])
        ty.append(query)
    return render(request,'compare.html',{'query':ty})
 
        
@csrf_exempt
def pdf(request):
    ty=[]
    for key in request.POST:
        query=paints.objects.get(name=request.POST[key])
        ty.append(query)
    p = canvas.Canvas("some.pdf")
    xco=0
    yco=800
    counter=0
    for i in ty:
        x=i.washability
        y=i.eco_friendly
        stri="   "+i.name+"  "+i.price+"   "+i.availability+"  "+i.brand+"  "+i.coverage+"  "+i.product_type+"  "+i.finish_type+"  "+i.best_for+"  "+str(x)+"  "+str(y)+"  "
        p.drawString(xco,yco-counter*50,stri)
        counter=counter+1
    p.save()
    message=EmailMessage('Comparison Sheet','Here is your comparison sheet in pdf','shivi.bajpai1@gmail.com',['xyz@gmail.com','abc@gmail.com'])
    attachment=open('some.pdf','rb')
    message.attach('some.pdf',attachment.read(),'application/pdf')
    p.showPage()
    return HttpResponse("Thanks Dude!!")