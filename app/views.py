import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Tracker

# Create your views here.

def list_app_items(request):
    tracker_list = Tracker.objects.all()

    total_carbs = sum(tracker.carbs for tracker in tracker_list)
    total_fat = sum(tracker.fat for tracker in tracker_list)
    total_protein = sum(tracker.protein for tracker in tracker_list)
    total_calories = sum(tracker.calories for tracker in tracker_list)

    context = {
        'tracker_list': tracker_list,
        'total_carbs': total_carbs,
        'total_fat': total_fat,
        'total_protein': total_protein,
        'total_calories': total_calories,
    }

    return render(request, 'app/app_list.html', context)

def insert_meal_item(request:HttpRequest):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"
    querystring = {"title": request.POST['content']}
    headers = {
	    "X-RapidAPI-Key": "81f467dcb4msha267bb86997498fp1d11f6jsnb2233dd28739",
	    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response_dict = response.json()
    print(response_dict)
    tracker = Tracker(content = request.POST['content'],
    calories = int(response_dict['calories']['value']), 
    fat = int(response_dict['fat']['value']),
    protein = int(response_dict['protein']['value']),
    carbs = int(response_dict['carbs']['value']))
    tracker.save()

    return redirect('/app/list/')

def delete_meal_item(request, meal_id):
    meal_to_delete = Tracker.objects.get(id=meal_id)
    meal_to_delete.delete()
    return redirect('/app/list/')