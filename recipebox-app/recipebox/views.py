from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse

from recipebox.models import Author, Recipe
from recipebox.forms import RecipeAddForm, AuthorAddForm, SignupForm, LoginForm

def index(request):
    items = Recipe.objects.all()
    return render(request, 'index.html', {'data':items})

def author(request, author_id):
    author_object = Author.objects.get(id=author_id)
    items = Recipe.objects.filter(author=author_object)
    context = {
        'data':items,
        'author':author_object
    }
    return render(request, 'author.html', context)

def recipe(request, recipe_id):
    items = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe.html', {'data':items})

@login_required()
def recipeadd(request):
    html = 'recipeadd.html'
    form = None

    if request.method == "POST":
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                body=data['body'],
                author=data['author']
            )
            return render(request, 'thanks.html')

    else:
        form = RecipeAddForm()
    return render(request, html, {'form': form})

def authoradd(request):
    html = 'authoradd.html'
    form = None

    if request.method == "POST":
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
                )
            Author.objects.create(
                user=user,
                bio=data['bio']
            )
            return render(request, 'thanks.html')

    else:
        form = AuthorAddForm()
    return render(request, html, {'form': form})

def signup_view(request):
    html = 'generic_form.html'
    form = None

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = user.objects.create_user(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            login(request, user)
            Author.objects.create(
                user=user,
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignupForm()
    return render(request, html, {'form': form})

def login_view(request):
    html = 'gereric_form.html'

    form = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
    return render(request, html, {'form': form})


def logout(request):
    pass
    