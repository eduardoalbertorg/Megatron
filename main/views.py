from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html')


def contact(request):
    return render(request=request,
                  template_name='main/contact.html')


def incidence(request):
    return render(request=request,
                  template_name='main/incidence.html')


def profile(request):
    return render(request=request,
                  template_name='main/profile.html')


def login(request):
    return render(request=request,
                  template_name='login.html')