from django.shortcuts import render, redirect
from django.http import HttpResponse 
from myport.models import Contact 
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def education(request):
    return render(request, 'education.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def savinginfo(request):
    if request.method == "POST":
       
       fullname=  request.POST.get("fname")
       mail = request.POST.get("mail")
       msg = request.POST.get("message")   


       data = Contact(full_name = fullname, email_address = mail, message = msg) 
       data.save()
       return redirect("contact")


    return HttpResponse("Data Saved.")



def records(request):
    all_records = Contact.objects.all()
    return render(request, "records.html", {"records": all_records})

def deleteR(request, x):
    record = Contact.objects.get(id = x)
    record.delete()
    messages.success(request, "Deleted successfully!")
    return redirect("records")



def updating(request, update_id):
    record = Contact.objects.get(id = update_id)
    return render (request, "updatings.html", {"record": record})

def updated(request, update_id):
    record = Contact.objects.get(id=update_id)

    if request.method == "POST":
        fullname = request.POST.get("fname")
        mail = request.POST.get("mail")
        msg = request.POST.get("message")

        record.full_name = fullname
        record.email_address = mail
        record.message = msg
        record.save()

    return redirect("records")


    