from django.shortcuts import render
from django.shortcuts import get_object_or_404
from recipebox.models import Author, Recipe

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
    # items = Recipe.objects.get(id=recipe_id)
    items = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe.html', {'data':items})
