from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from main.models import AttendanceRecord, Employee, Incidence


# Create your views here.
@login_required
def homepage(request):
    return render(request=request,
                  template_name='main/home.html')


@login_required
def contact(request):
    return render(request=request,
                  template_name='main/contact.html')


@login_required
def incidence(request):
    return render(request=request,
                  template_name='main/incidence.html')


@login_required
def attendance_record(request):
    return render(request=request,
                  template_name='main/attendance_records.html')


@login_required
def profile(request):
    return render(request=request,
                  template_name='main/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # To obtain the username after it is valid
            username = form.cleaned_data.get('username')
            messages.success(request, f"Se ha creado tu cuenta.")
            return redirect('main:login')
    else:
        form = UserRegisterForm()
    return render(request=request,
                  template_name='register.html',
                  context={'form': form})
