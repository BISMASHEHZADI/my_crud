from django.shortcuts import render,HttpResponseRedirect

from .models import My_Model
from .forms import My_Form
# Create your views here.

def add(request):
    if request.method=='POST':
        fm = My_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = My_Form()
    else:

        fm = My_Form()
    sm = My_Model.objects.all()
    return render(request,'add.html',{'form':fm,'stu':sm})



def delete(request,id):
    if request.method =='POST':
        dl = My_Model.objects.get(pk=id)
        dl.delete()
    else:
        dl = My_Form()
    return HttpResponseRedirect('/')



def update(request,id):
    if request.method=='POST':
        sm = My_Model.objects.get(pk=id)
        fm = My_Form(request.POST,instance=sm)
        if fm.is_valid():
            fm.save()
            fm = My_Form()

    else:
        sm = My_Model.objects.get(pk=id)
        fm = My_Form(instance=sm)
    return render(request,'update.html',{'form':fm})


