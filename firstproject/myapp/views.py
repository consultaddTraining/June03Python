from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WorkHours
from .serializers import LoginSerializer
from django.views import generic

# Create your views here.


def homepage(request):
    data = {"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth"},{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver"},{"id":3,"email":"emma.wong@reqres.in","first_name":"Emma","last_name":"Wong"}]}
    return JsonResponse(data)


def about(request):
    return HttpResponse("This is my Second Webpage")

def contact(request):
    return HttpResponse("This os contact page")

def custom(request):
    dict_var = {'template_var' : "It is used to display our Custom Webpage"}
    return render(request, 'myapp/login.html', context = dict_var)


def login_form(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("name ="+form.cleaned_data["email"])
            print(request.POST.get("name"))
            #form.save()

    return render(request, 'myapp/login.html', {'login_form':form})


class LoginList(APIView):
    def get(self,request):
        values = WorkHours.objects.all()
        serializer = LoginSerializer(values, many=True)
        return Response(serializer.data)








