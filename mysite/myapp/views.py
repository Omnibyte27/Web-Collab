from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.forms import ModelChoiceField

from django.views.generic import ( 
    DetailView,
    UpdateView,
    DeleteView
)

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            form_instance = forms.InputForm(request.POST)
            if form_instance.is_valid():
                # "cleaned_data" generates a dictionary of the form entries that can be
                # indexed into by keys (name of the form)- getting the data back out
                new_input = models.Input(input = form_instance.cleaned_data["input"])
                new_input.author = request.user
                # Save into the database
                new_input.save()
                # New form instance after successfully saving
                form_instance = forms.InputForm()
        else:
            form_instance = forms.InputForm() 
    else:
        form_instance = forms.InputForm()
    
    value = models.Input.objects.all()
    context={
        "variable":"Three by Three",
        "title":"3x3",
        "form":form_instance,
        "some_list":value
    }
    return render(request, "main_page.html", context=context)

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
            input_list["inputs"] += [{
                "input":i_q.input,
                "author":i_q.author.username
            }]
        #Use the JsonResponse to return back JSON
        return JsonResponse(input_list)
    else:
        return HttpResponse("Unsupported HTTP Method")
 
def main_page(request):
    context={
        "variable":"Three by Three",
        "title":"3x3"
    }
    return render(request, "main_page.html", context=context)
    
def profile(request):
    #value = models.Profile.objects.get(p_username = request.user)
    user = models.User.objects.get(username = request.user)
    context={
        #"val":value,
        "user_data":user,
        "variable":"Three by Three",
        "title":"3x3"
    }
    return render(request, "profile.html", context=context)

def play(request):
    context={
        "variable":"Three by Three",
        "title":"3x3"
    }
    return render(request, "play.html", context=context)

############################################
#Deck Views
############################################

#Deck creation view
def decks(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            create_form_instance = forms.DeckForm(request.POST)
            if create_form_instance.is_valid():
                new_deck = create_form_instance.save(commit=False)
                new_deck.author = request.user
                new_deck.save()
                create_form_instance = forms.DeckForm()
        else:
            create_form_instance = forms.DeckForm() 
    else:
        create_form_instance = forms.DeckForm()

    value = models.Deck.objects.all().order_by('deck_name')
    context={
        "variable":"Three by Three",
        "title":"3x3",
        "deck_list":value,
        "create_deck_form":create_form_instance,
    }
    return render(request, "decks.html", context=context)

class DeckDetailView(DetailView):
    model = models.Deck
    template_name = 'deck/deck_detail.html' #<app>/<model>_<viewtype>.html

class DeckUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Deck
    template_name = 'deck/deck_form.html'#<model>_form.html
    fields = ["deck_name", "card1", "card2", "card3", "card4", "card5"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        deck = self.get_object()
        if self.request.user == deck.author:
            return True
        return False

class DeckDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Deck
    template_name = 'deck/deck_delete.html' #<app>/<model>_<viewtype>.html
    success_url = '/decks/'

    def test_func(self):
        deck = self.get_object()
        if self.request.user == deck.author:
            return True
        return False

############################################
#End Deck Views
############################################
    
def logout_view(request):
    logout(request)
    return redirect("/login/")
    
def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
        "help":"helping"
    }
    return render(request, "registration/register.html", context=context)
    