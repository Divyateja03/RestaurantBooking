from django.shortcuts import render
from .models import Menu, Category

# Create your views here.


def menu_list(request):
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    context = {
        'menu_list' : menu_list,
        'categories' : categories,
        }
    return render(request, 'menu/list.html', context)


def meal_details(request, slug):
    meal_details = Menu.objects.get(slug = slug)
    context = {'meal_details' : meal_details,}
    return render(request, 'menu/details.html', context)

    