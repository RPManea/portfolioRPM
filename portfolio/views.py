from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def link_cv(request):
    return render(request, 'link_cv.html')