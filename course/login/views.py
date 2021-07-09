from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from login.forms import acc_form
from login.models import account



def login1(request):
    au = request.user
    if au.is_authenticated:
        return redirect('/mainpage/')

    context = {

    }
    return render(request, 'loginpage.html', context)

def CHECK(request):
    context = {

    }

    au = request.user
    if au.is_authenticated:
        return redirect('/mainpage/')

    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        print(user, password)
        form = acc_form(request.POST)
        if user != '' and user is not None:
            if password != '' and password is not None:
                if form.is_valid():
                    acc = authenticate(username=user, password=password)
                    if acc:
                        login(request, acc)
                        return redirect('/mainpage/')
                else:
                    messages.warning(request, "Invalid Username and password")
            else:
                messages.warning(request, "enter your password")
        else:
            messages.warning(request, "enter your username")
    else:
        form = acc_form()

    context['login_form'] = form
    return render(request, 'loginpage.html', context)

def sign(request):

    if request.method == "POST":
        NAME = request.POST.get('NAME')
        USERNAME = request.POST.get('uname')
        PASSWORD = request.POST.get('passwords')
        CONFIRMPASSWORD = request.POST.get('cpassword')

        print(NAME)
        print(USERNAME)
        print(PASSWORD)
        print(CONFIRMPASSWORD)

        user = account.objects.create_user(password=CONFIRMPASSWORD, NAME=NAME, username=USERNAME)
        user.save()

        return redirect('login')
    else:
        context = {

        }
        return render(request, 'signup.html', context)



def signup1(request):

    context = {

    }
    return render(request, 'signup.html', context)


def main(request):
    context = {

    }
    return render(request, 'mainpage.html', context)


def course(request):
    USER = request.user
    reg_id =USER
    coursees = account.objects.get(username=reg_id)
    date_given = str(coursees.NAME)
    context = {

        "data_course": coursees,
        "NAME": date_given

    }
    return render(request, 'course.html', context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)



def c(request):
    USER = request.user
    reg_id = USER
    c = account.objects.get(username=reg_id)
    date_given = str(c.NAME)
    context = {

        "data_c": c,
        "NAME": date_given

    }

    return render(request, 'c.html', context)


def cpp(request):
    USER = request.user
    reg_id = USER
    cpp = account.objects.get(username=reg_id)
    date_given = str(cpp.NAME)
    context = {

        "data_cpp": cpp,
        "NAME": date_given

    }
    return render(request, 'cpp.html', context)


def java(request):
    USER = request.user
    reg_id = USER
    java = account.objects.get(username=reg_id)
    date_given = str(java.NAME)
    context = {

        "data_java": java,
        "NAME": date_given

    }
    return render(request, 'java.html', context)



def python(request):
    USER = request.user
    reg_id = USER
    python = account.objects.get(username=reg_id)
    date_given = str(python.NAME)
    context = {

        "data_python": python,
        "NAME": date_given

    }
    return render(request, 'python.html', context)



def django(request):
    USER = request.user
    reg_id = USER
    django = account.objects.get(username=reg_id)
    date_given = str(django.NAME)
    context = {

        "data_django": django,
        "NAME": date_given

    }
    return render(request, 'django .html', context)


def network(request):
    USER = request.user
    reg_id = USER
    net = account.objects.get(username=reg_id)
    date_given = str(net.NAME)
    context = {

        "data_net": net,
        "NAME": date_given

    }
    return render(request, 'network.html', context)


def logout1(request):

    logout(request)
    return redirect('login')


