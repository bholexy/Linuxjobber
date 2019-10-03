from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from home.models import FAQ
from Courses.models import Course # will be used to populate the course list in base.html


def index(request):
    aut = False
    current_user = ''
    if request.user.is_authenticated:
        aut = True
        current_user = request.user.last_name
    # simply pass 'courses' : all_course_objects here, to be able to use the list in the base.html
    return render (request, 'home/index.html', {'current_user':current_user, 'aut':aut})


#SIGNUP VIEW
def signup(request):
    if request.method == "POST":
        firstname = request.POST['fullname']
        email = request.POST['email']
        x = email.split('@')
        password = request.POST['password']
        username = email
        lastname = x[0]

        if (firstname):
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return render(request, "home/registration/success.html",{'username':lastname})
        else:
            error = True
            return render(request, 'home/registration/signup.html', {'error':error})
    else:
        return render(request, 'home/registration/signup.html')


def selfstudy(request):
    return render(request, 'home/selfstudy.html')


def faq(request):
    faqs = FAQ.objects.all()
    context ={
            'faqs': faqs        
                }
    return render(request, 'home/faq.html', context)


def log_in(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = user_name, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("home:index")
        else:
            error_message = "yes"
            return render(request, "home/registration/login.html", {'error_message' : error_message})
    else:
        return render(request, "home/registration/login.html")

def log_out(request):
    logout(request)
    return redirect("home:login")

def   linux_certification(request):
    return render(request, 'home/linux_certification.html')

def workexperience(request):
    return render(request, 'home/workexperience.html')

def jobplacements(request):
    return render(request, 'home/jobplacements.html')

def apply(request):
    return render(request, 'home/apply.html')

def apply_jnr(request):
    return render(request, 'home/apply_jnr.html')

def qualify(request):
    return render(request, 'home/qualify.html')

def required2(request):
    return render(request, 'home/required2.html')

def qualify2(request):
    return render(request, 'home/qualify2.html')

def required(request):
    return render(request, 'home/required.html')

# @login_required(login_url="/home/log_in/")
def pay(request):
    return render(request, 'home/pay.html')

def accepted(request):
    return render(request, 'home/accepted.html')

def group(request):
    return render(request, 'home/group_class.html')
