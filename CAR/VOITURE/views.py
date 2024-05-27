from django.shortcuts import render,redirect
from .forms import UserCreationForm


# Create your views here.
def acceuil(request):
    return render(request,'acceuil.html')

def Login(request):
    return render(request,'Login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def aboutus(request):
    return render(request,'aboutus.html')

def reserver(request):
    return render(request,'reserver.html')




