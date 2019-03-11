from django.shortcuts import render
from django.shortcuts import get_object_or_404
from recipebox.models import Author, Recipe
from recipebox.forms import RecipeAddForm, AuthorAddForm


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

def recipeadd(request):
    html = 'recipeadd.html'
    form = None

    if request.method == "POST":
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            RecipeItem.objects.create(
                title=data['title'],
                description=['description'],
                time_required=['time_required'],
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

            AuthorItem.objects.create(
                user=data['user'],
                bio=['bio']
            )
            return render(request, 'thanks.html')

    else:
        form = AuthorAddForm()
    return render(request, html, {'form': form})
