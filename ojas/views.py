from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import SingUpForm,contact,EmpForm
from django.contrib import messages
from .models import Employee
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.core.cache import cache
from django.template.response import TemplateResponse
from django.views.generic.base import RedirectView
from django.views import View





from django.contrib.auth import authenticate, login, logout,update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method=='POST':
        fm=SingUpForm(request.POST)
        if fm.is_valid():
            EMAIL=fm.cleaned_data['email']
            fm.save()
            messages.success(request,'your  singup successfully')
            send_mail(
                'Testing Mail',
                'Here is the message.',
                'vadeppa1994@gmail.com',
                [str(EMAIL)],
                fail_silently=False,
            )

            fm=SingUpForm()
    else:
        fm=SingUpForm()
    return render(request,'signup.html',{'form':fm})

# def logins(request):
#     if not request.user.is_authenticated:
#         if request.method=='POST':
#             fm=AuthenticationForm(request=request,data=request.POST)
#             if fm.is_valid():
#                 name = fm.cleaned_data['username']
#                 paswd = fm.cleaned_data['password']
#                 user = authenticate(username=name,password=paswd)
#
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request,'your login seccessfuly')
#                     #return HttpResponseRedirect('/profile/')
#         else:
#             fm=AuthenticationForm()
        #return render(request,'login.html',{'form':fm})
    #else:
       # return HttpResponseRedirect('/profile/')
def profile(request):
    return render(request,'profile.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/dash/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
       return HttpResponseRedirect('/dash/')

def user_loguot(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def feedback(request):
    return render(request,'feedback.html')


# def home(request):
#     form=Employee.objects.all()
#     return render(request,'home.html',{'form':form})

def home(request):
    form = Employee.objects.all()
    ip=request.session.get('ip')
    user=request.user
    ct = cache.get('count', version=user.pk)

    return render(request,'home.html',{'form':form,'ip':ip,'ct':ct})

def about(request):
    return render(request,'about.html')
def Contact(request):
    if request.method=='POST':
        fm=contact(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'successfully aploded')
            return HttpResponse('Thanks')
    else:
        fm=contact()
    return render(request,'contact.html',{'form':fm})

def dashborad(request):
    if request.method=='POST':
        fm=EmpForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=EmpForm()
    else:
        fm=EmpForm()
    return render(request,'dashboard.html',{'form':fm,'name':request.user})

# def delet(request,id):
#     fm=Employee.objects.get(pk=id)
#     fm.delete()
#     return HttpResponseRedirect('/')


#==================================================

# def edite(request, id):
#     fm=Employee.objects.get(pk=id)
#     form=EmpForm(instance=fm)
#     if request.method=='POST':
#         form=EmpForm(request.POST,instance=fm)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('/')
#     else:
#         return render(request,'edit.html',{'form':form})

#==========================================================
class DeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Employee.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class EditView(View):
    def get(self, request, id):
        pi = Employee.objects.get(pk=id)
        fm = EmpForm(instance=pi)
        return render(request, 'edit.html', {'form': fm})

    def post(self, request, id):
        pi = Employee.objects.get(pk=id)
        fm = EmpForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request, 'edit.html', {'form': fm})


#===============================================================================
def set_cookie(request):
    obj=render(request,'set.html')
   # obj.set_cookie('name','sonu',max_age=20)
    obj.set_signed_cookie('name', 'Sonam', salt='apple', expires=datetime.utcnow() + timedelta(days=2))

    #obj.set_cookie('lastname','chakali')
    return obj


def get_cookie(request):
    #obj=request.COOKIES.get('name','vadeppa')
    obj = request.get_signed_cookie('name', default="Ojas", salt='banana')

    return render(request,'get.html',{'name':obj})

def del_cookie(request):
    reponse = render(request, 'del.html')
    reponse.delete_cookie('name')
    reponse.delete_cookie('lastname')

    return reponse

def set_session(request):
    request.session['name']='sonu'
    request.session['lastname']='madiwal'
    return render(request,'setsession.html')
def get_session(request):
    name=request.session['name']
    return render(request,'get1.html',{'name':name})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'delsession.html')