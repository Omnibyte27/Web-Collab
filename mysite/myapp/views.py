#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
from . import forms

# Create your views here.
def index(request, page=0):
    if request.method=="POST":
        form_instance = forms.InputForm(request.POST)
        if form_instance.is_valid():
            # "cleaned_data" generates a dictionary of the form entries that can be
            # indexed into by keys (name of the form)- getting the data back out
            new_input = models.Input(input = form_instance.cleaned_data["input"])
            # Save into the database
            new_input.save()
            # New form instance after successfully saving
            form_instance = forms.InputForm()
    else:
        form_instance = forms.InputForm()
    
    value = models.Input.objects.all()
    valuelist = range(10*page+10)
    context={
        "variable":"CINS465 Hello World",
        "title":"CINS465 Hello World",
        "form":form_instance,
        #"some_list":value[page*5:(page*5+5)],
        "some_list":value,
        "value_list":valuelist[page*10:(page*10+10)]
    }
    return render(request, "index.html", context=context)

@csrf_exempt
@login_required(login_url='/login/')    
def inputs_view(request):
    if request.method == "GET":
        #REST API call that gets all data
        #Query objects and get back a set
        input_query = models.Input.objects.all()
        input_list = {"inputs":[]}
        #For each input_query in the query-
        #add to input_list
        for i_q in input_query:
            input_list["inputs"] += [{"input":i_q.input}]
        #Use the JsonResponse to return back JSON
        return JsonResponse(input_list)
    else:
        return HttpResponse("Unsupported HTTP Method")

def logout_view(request):
    logout(request)
    return redirect("/login/")
