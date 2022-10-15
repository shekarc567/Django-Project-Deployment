from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course, Batch, Student


# Create your views here.

def index(request):
    # return HttpResponse("<h1>Welcome to Prime Intuit Registration Page</h1>")
    batch_list = Batch.objects.raw('select * from Registration_Batch')
    data_dict = {'access_record': batch_list,'Insert_Me': "I am a text from Registration/views.py",
                 'Insert_Shivu':"Shivu is becoming more punctual these days" }

    return render(request,'Registration/index.html',context=data_dict)

def Home(request):
    # return HttpResponse("<h1>Welcome to Prime Intuit Home Page</h1>")
    # my_dict = {'Insert_Me': "I am a text from Registration/Views.py now from sub templates",
    #            'Insert_Shivu':"Shivu is becoming more punctual these days"}
    # batch_list = Batch.objects.order_by('batch_ID')
    # batch_list = Batch.objects.raw('select * from Registration_Batch where start_date >"2021-06-01"')
    batch_list = Batch.objects.raw('select * from Registration_Batch')
    data_dict = {'access_record': batch_list,'Insert_Me': "I am a text from Registration/views.py",
                 'Insert_Shivu':"Shivu is becoming more punctual these days" }

    return render(request,'Registration/index.html',context=data_dict)