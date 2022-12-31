from django.shortcuts import render

# Create your views here.
def bala(request):
    d={'a':1,'b':0,'c':1}
    return render(request,'ravi.html',d)