from django.shortcuts import render
from .forms import RegisterForm
from .models import employee
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.
def home(request):
    forms=RegisterForm()
    return render(request,"index.html",{'form':forms})

def register(request):
   fname=request.GET.get('fname')
   lname=request.GET.get('lname')
   age=request.GET.get('age')
   addr=request.GET.get('addr')
   phn=request.GET.get('phn')
   email=request.GET.get('email')
   pswd=request.GET.get('pswd')
   pht=request.GET.get('pht')
   print(fname,lname)
   tab=employee.objects.create(firstname=fname,lastname=lname,age=age,address=addr,phone=phn,email=email,password=pswd,photo=pht)
   if(tab!=None):
       data={'status':True,'message':'details saved'}
       return JsonResponse(data)
   else:
       data={'status':False,'message':'creation failed'}
       return JsonResponse(data)
   
def details(request):
    data1=employee.objects.all()
    data=serialize('json',data1)
    return JsonResponse(data,safe=False)