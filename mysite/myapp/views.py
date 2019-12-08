from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
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
                # indexed into b y keys (name of the form)- getting the data back out
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

    challenge_from = ""
    challenge_to = ""
    
    if request.user.is_authenticated:
        intial = models.User.objects.exclude(d_author=None)
        values = intial.exclude(username=request.user)

        length_from = len(models.Challenge.objects.filter(user_from__username__exact = request.user))
        if length_from > 0:
            challenge_from = models.Challenge.objects.filter(user_from__username__exact = request.user).latest('created_at')
        else:
            challenge_from = ""

        length_to = len(models.Challenge.objects.filter(user_to__username__exact = request.user))
        if length_to > 0:
            challenge_to = models.Challenge.objects.filter(user_to__username__exact = request.user).latest('created_at')
        else:
            challenge_to = ""

        #challenge_to = models.Challenge.objects.filter(user_to__username__exact = request.user).latest('created_at')
    else:
        values = None
    context={
        "challenge_from": challenge_from,
        "challenge_to": challenge_to,
        "form":form_instance,
        "values": values,
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
        return HttpResponseRedirect('/')

    length_of = len(models.Deck.objects.filter(author__username__exact = str(player)))
    if length_of == 0:
        return HttpResponseRedirect('/')

    if (str(player) == str(request.user)):
        return HttpResponseRedirect('/')

    opp_decks = models.Deck.objects.filter(author__username__exact = str(player))
    user_decks = models.Deck.objects.filter(author__username__exact = request.user)

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
                return HttpResponseRedirect('/game/' + player + '/matching')
        else:
            create_form_instance = forms.VersusDeck() 
    else:
        create_form_instance = forms.VersusDeck()
    
    decks_of = models.Deck.objects.filter(author__username = opponent.username)

    context={
        "player":player,
        "opponent": opponent,
        "deck_list": decks_of,
        "create_deck_form":create_form_instance
    }
    return render(request, "play.html", context=context)

@csrf_exempt
@login_required(login_url='/login/')    
def from_view(request):
    if request.method == "GET":

        from_length = len(models.Challenge.objects.filter(user_from=request.user))

        if (from_length > 0):
            ufq = models.Challenge.objects.filter(user_from=request.user).latest('created_at')
            user_from_list = {"user_from_challenge":[]}

            user_from_list["user_from_challenge"] += [{
                "user_from":ufq.user_from.username,
                "user_to":ufq.user_to.username,
                "user_from_deck":ufq.user_from_deck.deck_name,
                "user_to_deck":ufq.user_to_deck.deck_name,
                "created_at":ufq.created_at
            }]
        else:
           return HttpResponse("None")
        
        #Use the JsonResponse to return back JSON
        return JsonResponse(user_from_list)
    else:
        return HttpResponse("Unsupported HTTP Method")

@csrf_exempt
@login_required(login_url='/login/')    
def to_view(request):
    if request.method == "GET":

        to_length = len(models.Challenge.objects.filter(user_to=request.user))

        if (to_length > 0):
            utd = models.Challenge.objects.filter(user_to=request.user).latest('created_at')
            user_to_list = {"user_to_challenge":[]}

            user_to_list["user_to_challenge"] += [{
                "user_from":utd.user_from.username,
                "user_to":utd.user_to.username,
                "user_from_deck":utd.user_from_deck.deck_name,
                "user_to_deck":utd.user_to_deck.deck_name,
                "created_at":utd.created_at
            }]
        else:
            return HttpResponse("None")
        
        #Use the JsonResponse to return back JSON
        return JsonResponse(user_to_list)
    else:
        return HttpResponse("Unsupported HTTP Method")

@login_required(login_url='/login/')
def matching_view(request, player):
    opp = models.User.objects.filter(username=str(player)).exists()

    if opp == False:
        return HttpResponseRedirect('/')

    length_of = len(models.Deck.objects.filter(author__username__exact = str(player)))
    if length_of == 0:
        return HttpResponseRedirect('/')

    if (str(player) == str(request.user)):
        return HttpResponseRedirect('/')

    challenger = models.User.objects.get(username=request.user)
    opponent = models.User.objects.get(username=str(player))
    challenge = models.Challenge.objects.filter(user_from__username__exact = request.user, user_to__username__exact = opponent).latest('created_at')
    from_deck_detail = models.Deck.objects.get(pk=challenge.user_from_deck)
    to_deck_detail = models.Deck.objects.get(pk=challenge.user_to_deck)

    context={
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

    context={
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
    