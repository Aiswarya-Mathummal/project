from django.shortcuts import render,redirect,HttpResponse
from.forms import RegisterForm,LoginForm,UpdateForm,changePswdForm
from django.contrib import messages
from . models import user_register,Galleryy
from django.contrib.auth import logout as logouts

# Create your views here.
def home(request):
    return render(request,"index.html")



def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            pswd=form.cleaned_data['password']
            try:
                user=user_register.objects.get(email=email)
                if not user:
                   messages.warning(request,"email doesnot exists") 
                   return redirect('myapp:login')
                elif pswd!=user.password:
                  messages.warning(request,"incorrect password")
                  return redirect('myapp:login')
                else:
                  messages.success(request,"success")
                  return redirect('/user/%s' % user.id)
            except:
                messages.warning(request,"user doesnot exist")
                return redirect('myapp:login')
            
    else: 
        form=LoginForm()     
        return render(request,"login.html",{'form':form})
    
def user_account(request,id):
        user=user_register.objects.get(id=id)
        print(user.photo)
        return render(request,'user.html',{'user':user})

def edit_profile(request,id):
     user=user_register.objects.get(id=id)
     if request.method=='POST':
        form=UpdateForm(request.POST or None,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/user/%s' % user.id)
     else:
        form=UpdateForm(instance=user)
        return render(request,'update.html',{'user':user,'form':form})

def Change_password(request,id):
    user=user_register.objects.get(id=id)
    if request.method=='POST':
        form=changePswdForm(request.POST or None)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            if oldpassword!= user.password:
                messages.warning(request,"incorrect")
                return redirect('/change_pswd/%s' % user.id)
            elif oldpassword==newpassword: 
                messages.warning(request, "password similar")
                return redirect('/change_pswd/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"password new")
                return redirect('/change_pswd/%s'% user.id)
            else:
                user.password=newpassword
                user.save()
                messages.success(request,"change success")
                return redirect('/user/%s'% user.id)
    else:
        form=changePswdForm()
        return render(request,'change_pswd.html',{'user':user, 'form':form})
    
 
def sign_up(request):
    if request.method=='POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['username']
            pswd=form.cleaned_data['password']
            addr=form.cleaned_data['address']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            photos=form.files['photo']
            tab=user_register(username=name,password=pswd,address=addr,email=email,phone=phone,photo=photos)
            tab.save()
            return redirect('myapp:login')
    else:
        form=RegisterForm()
    return render(request,'signup.html',{'form':form })

def logout(request):
    logouts(request)
    messages.success(request,"logged out")
    return redirect('/')



# ------------------------------------ GALLERY---------------------------

def gallery(request):
    data=Galleryy.objects.all()
    context = {
        'data' : data
    }
    return render(request,"gallery_home.html",context)

def image_details(request,id):
        img=Galleryy.objects.get(id=id)
        return render(request,'details.html',{'img':img})
