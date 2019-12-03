from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from . import models
from . import forms
from django.forms import ModelChoiceField
from django.views.generic import ( 
    DetailView,
    UpdateView,
    DeleteView
)

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

    dev_posts = models.DevMessages.objects.all()
    input_messages = models.Input.objects.all()
    
    if request.user.is_authenticated:
        value = models.Deck.objects.exclude(author=request.user)[:1]
        name = request.user.username
    else:
        value = None
        name = None
    context={
        "variable":"Three by Three",
        "title":"3x3",
        "form":form_instance,
        "player_list":value,
        "dev_posts":dev_posts,
        "input_messages":input_messages
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

@csrf_exempt
@login_required(login_url='/login/')
def players_view(request):
    if request.method == "GET":
        #REST API call that gets all data
        #Query objects and get back a set
        player_query = models.Deck.objects.exclude(author=request.user)[:1]
        player_list = {"players":[]}
        #For each player_query in the query-
        #add to player_list
        for i_q in player_query:
            player_list["players"] += [{
                "author":i_q.author.username
            }]
        #Use the JsonResponse to return back JSON
        return JsonResponse(player_list)
    else:
        return HttpResponse("Unsupported HTTP Method")

############################################
#Game Views
############################################

@login_required(login_url='/login/')
def player_view(request, player):
    opp = models.User.objects.filter(username=str(player)).exists()

    if opp == False:
        return HttpResponse("Unsupported HTTP Method")

    print(opp)

    opp_decks = models.Deck.objects.filter(author__username__exact = str(player))
    print(opp_decks)
    user_decks = models.Deck.objects.filter(author__username__exact = request.user)
    print(user_decks)

    opponent = models.User.objects.get(username=str(player))

    forms.VersusDeck.base_fields['user_from_deck'] = forms.ModelChoiceField(queryset=user_decks)
    forms.VersusDeck.base_fields['user_to_deck'] = forms.ModelChoiceField(queryset=opp_decks)

    forms.VersusDeck.base_fields['user_from_deck'].label = "Choose your deck"
    forms.VersusDeck.base_fields['user_to_deck'].label = "Choose your opponent's deck"

    if request.method=="POST":
        if request.user.is_authenticated:
            create_form_instance = forms.VersusDeck(request.POST)
            if create_form_instance.is_valid():
                new_deck = create_form_instance.save(commit=False)
                new_deck.user_from = request.user
                new_deck.user_to = opponent
                new_deck.save()
                create_form_instance = forms.VersusDeck()
        else:
            create_form_instance = forms.VersusDeck() 
    else:
        create_form_instance = forms.VersusDeck()

    um = models.Challenge.objects.filter(user_from__username__exact = request.user).latest('user_from_deck')
    um2 = models.Challenge.objects.filter(user_from__username__exact = request.user, user_to__username__exact = opponent).latest('created_at')
    
    deck_detail = models.Deck.objects.get(pk=um.user_from_deck)
    
    decks_of = models.Deck.objects.filter(author__username = opponent.username)

    context={
        "variable":"Three by Three",
        "title":"3x3",
        "player":player,
        "opponent": opponent,
        "deck1": um,
        "deck2": um2,
        "deck": deck_detail,
        "deck_list": decks_of,
        "create_deck_form":create_form_instance
    }
    return render(request, "play.html", context=context)

@login_required(login_url='/login/')
def matching_view(request, player):
    opp = models.User.objects.filter(username=str(player)).exists()

    if opp == False:
        return HttpResponse("Unsupported HTTP Method")

    challenger = models.User.objects.get(username=request.user)
    opponent = models.User.objects.get(username=str(player))
    challenge = models.Challenge.objects.filter(user_from__username__exact = request.user, user_to__username__exact = opponent).latest('created_at')
    from_deck_detail = models.Deck.objects.get(pk=challenge.user_from_deck)
    to_deck_detail = models.Deck.objects.get(pk=challenge.user_to_deck)

    context={
        "variable":"Three by Three",
        "title":"3x3",
        "challenger": challenger,
        "opponent": opponent,
        "challenge": challenge,
        "deck_from": from_deck_detail,
        "deck_to": to_deck_detail
    }
    return render(request, "matching.html", context=context)

############################################
#Deck Views
############################################

#Deck creation view
@login_required(login_url='/login/') 
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

    catalog = models.CardCatalogue.objects.all()
    value = models.Deck.objects.filter(author=request.user).order_by('deck_name')
    user = models.User.objects.get(username = request.user)
    
    #cur = models.Challenge.objects.latest('field')

    context={
        "variable":"Three by Three",
        "title":"3x3",
        "deck_list":value,
        "create_deck_form":create_form_instance,
        "user_data":user,
        "catalog":catalog
    }
    return render(request, "deck/decks.html", context=context)

class DeckDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.Deck
    template_name = 'deck/deck_detail.html' #<app>/<model>_<viewtype>.html

    def test_func(self):
        deck = self.get_object()
        if self.request.user == deck.author:
            return True
        return False

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
#Logout/Register Views
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
    