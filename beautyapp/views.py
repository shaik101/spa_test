from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Register
from .models import Gift
from .models import Citys
from .models import Services
from .models import Appointment
from .models import Carriers


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
# from twilio.rest import Client




# Create your views here.
def home(request):
    return render(request,'beautyapp/home.html')

def memberplan(request):
    return render(request,'beautyapp/memberplan.html')

def eservice(request):
    return render(request,'beautyapp/eservice.html')

def about(request):
    return render(request,'beautyapp/about.html')

def footrefl(request):
    return render(request,'beautyapp/footrefl.html')

def services(request):
    return render(request,'beautyapp/service.html')

def gallery(request):
    return render(request,'beautyapp/gallery.html')

def espackage(request):
    return render(request,'beautyapp/espackage.html')

def mens(request):
    return render(request,'beautyapp/mens.html')


def contact(request):
    return render(request,'beautyapp/contact.html')

# @login_required(login_url='/beautyapp/login')
def careers(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        date = request.POST['date']
        email = request.POST['email']
        mobileno = request.POST['mobileno']
        totalexp = request.POST['totalexp']
        lastsalary = request.POST['lastsalary']
        fileupload = request.POST['fileupload']

        careers=Carriers(name=name,address=address,date=date,email=email,mobileno=mobileno,totalexp=totalexp,lastsalary=lastsalary,fileupload=fileupload)
        careers.save()
        messages.info(request,'  ')
        return redirect(home)



    return render(request,'beautyapp/careers.html')

# @login_required(login_url='/beautyapp/login')
def appointment(request):
    if request.method == 'POST':
        name=request.POST['name']
        mobileno=request.POST['mobileno']
        # account_sid = 'AC3549bd6e2b8a691aead0d4734145d67d'
        # auth_token = '18907a34592521315623e94e9e8f7cd9'
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #               from_='+12055641901',
        #               body ='hello sandy',
        #               to =mobileno,
        #               )
        city=request.POST['city']
        date=request.POST['pdate']
        time=request.POST['ptime']
        services=request.POST['services']
        se=Services.objects.get(id=services)
        # se.save()
        qs = Citys.objects.get(id=city)
        # qs.save()
        appointment=Appointment(name=name,mobileno=mobileno,city=qs,date=date,time=time,services=se)
        appointment.save()
        messages.success(request,'  ')
        return redirect(home)

        # return render(request,'beautyapp/appointment.html')

    else:

        context_data = {
        'appointment':'appointment',
        'services':Services.objects.all(),
          'city':Citys.objects.all()


        }
        return render(request,'beautyapp/appointment.html', context_data)



def logout(request):
    auth.logout(request)
    return redirect(home)

def buygift(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        price=request.POST['price']
        message=request.POST['message']
        gift=Gift(name=name,email=email,mobile=mobile,address=address,price=price,message=message)
        messages.warning(request,'  ')
        gift.save()


        return redirect(home)

    else:
        return render(request,'beautyapp/gift.html')

def login(request):
    if request.method=='POST':


        register=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if register is not None:
            auth.login(request,register)
            return redirect(home)
        else:
            messages.info(request,'invalid credentials')
            return redirect(login)
    else:
        return render(request,'beautyapp/login.html')


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']



        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif Register.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                # emails = EmailMessage("Request is raised", ' welocome in beuty spa ',settings.EMAIL_HOST_USER , [email])
                # emails.send()
                user.save();
                print('user created')
                messages.success(request,' ')
                return redirect(login)

        else:
            messages.info(request,'password do not match')
            return redirect('register')
        return redirect(home)
    else:
        return render(request,'beautyapp/register.html')
