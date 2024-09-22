from django.shortcuts import render,redirect
from .models import Members

# Create your views here.

def home(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')
def view(request):
    member = Members.objects.all()
    return render(request,'view.html',context={'member':member})


def addrecord(request):
    first = request.POST['first']
    last = request.POST['first']
    country = request.POST['first']
    member = Members(first_name = first,last_name = last,country=country)
    member.save()
    return redirect('/view/')

def delete_item(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect("/view/")

def update(request,id):
    member = Members.objects.get(id=id)

    return render(request,'update.html',context={"member":member})

def update_record(request,id):
    first = request.POST['first']
    last = request.POST['last']
    country = request.POST['country']
    member = Members.objects.get(id=id)
    member.first_name = first
    member.last_name = last
    member.country = country
    member.save()
    return redirect('/view/')
