from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, EditCoursesTakenForm, UserSearchForm

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            messages.success(request, ("We can't find that email and password. Please try again."))
            return redirect('login')
    else:
        return render(request, 'members/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout was successful."))
    return redirect('login')

def signup_page(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print("made it here")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('edit_profile')
    else:
        print("made")
        form = RegisterUserForm()
    

    return render(request, 'members/signup.html', {
        'form': form,
    })

@login_required
def edit_profile_page(request):
    if request.method == "POST":
        update_form = EditCoursesTakenForm(request.POST, instance=request.user.student)
        if (update_form.is_valid()):
            print("update made")
            update_form.save()
            print("new val: " + str(request.user.student.taken_EECS485))
            messages.success(request, ("update was successful"))
            return redirect('mainpage')
    else:
        print("hereerere")
        update_form = EditCoursesTakenForm(instance=request.user.student)
    
    
    context = {
        'update_form': update_form,
    }

    return render(request, 'members/edit_profile.html', context)
