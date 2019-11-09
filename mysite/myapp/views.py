from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import models
from . import forms

# Create your views here.
def index(request):
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
    context={
        "variable":"CINS465 Hello World",
        "title":"CINS465 Hello World",
        "form":form_instance
    }
    return render(request, "index.html", context=context)
    
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
 
def main_page(request):
    #value = models.Input.objects.all()
    context={
        "variable":"Three by Three",
        "title":"3x3"
        #"form":form_instance
    }
    return render(request, "main_page.html", context=context)
    
def profile(request):
    #value = models.Input.objects.all()
    context={
        "variable":"Three by Three",
        "title":"3x3"
        #"form":form_instance
    }
    return render(request, "profile.html", context=context)
    
def decks(request):
    #value = models.Input.objects.all()
    context={
        "variable":"Three by Three",
        "title":"3x3"
        #"form":form_instance
    }
    return render(request, "decks.html", context=context)
    
def play(request):
    #value = models.Input.objects.all()
    context={
        "variable":"Three by Three",
        "title":"3x3"
        #"form":form_instance
    }
    return render(request, "play.html", context=context)