from django.db.models import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Recipe

def index(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        # save in db
        Recipe.objects.create(recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description
        )
        return redirect("recipe:index")
    recipes = Recipe.objects.all()

    search_query = request.GET.get('search')

    if search_query:
        recipes = recipes.filter(recipe_name__icontains=search_query)

    return render(request, "recipes/index.html", {'recipes':recipes})

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)

    if request.method == "POST":

        data = request.POST
        image = request.FILES.get("recipe_image")
        recipe.recipe_name = data.get('recipe_name')
        recipe.recipe_description = data.get('recipe_description')

        if image:
            recipe.recipe_image = image
        recipe.save()
        return redirect("recipe:index")

    return render(request, "recipes/update.html", {"recipe":recipe})


def delete_recipe(request, id):
    try:
        recipe = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        return render(request, "recipes/index.html", {"error_message":"Invalid recipe id"})
    else:
        recipe.delete()
        return redirect( "recipe:index")
