from django.shortcuts import render

from django.shortcuts import render, redirect

from .models import Exercise

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExerciseForm()
    return render(request, 'add_exercise.html', {'form': form})

# Create similar views for adding Diet, Sleep, Emotion, and other data types

def public_dashboard(request):
    exercises = Exercise.objects.all()
    diets = Diet.objects.all()
    # Similar queries for Sleep, Emotion, and other data types
    
    context = {
        'exercises': exercises,
        'diets': diets,
        # Add data for Sleep, Emotion, and other data types
    }
    return render(request, 'public_dashboard.html', context)

from django.shortcuts import render

def dashboard(request):
    # Your view logic here
    # Fetch data (you can customize this query based on your needs)
    exercises = Exercise.objects.all()

    return render(request, 'dashboard.html', {'exercises': exercises})

# health_app/views.py
from django.shortcuts import render
from django.conf import settings
import openai

from .models import HealthData


# def health_dashboard(request):
#     form = HealthInputForm()

#     if request.method == 'POST':
#         form = HealthInputForm(request.POST)
#         if form.is_valid():
#             exercise_info = form.cleaned_data['exercise_info']
#             diet_preferences = form.cleaned_data['diet_preferences']
#             sleep_patterns = form.cleaned_data['sleep_patterns']
#             emotion_status = form.cleaned_data['emotion_status']

#             user_input = f"Exercise: {exercise_info}\nDiet: {diet_preferences}\nSleep: {sleep_patterns}\nEmotion: {emotion_status}"

#             openai.api_key = settings.OPENAI_API_KEY

#             response = openai.Completion.create(
#                 engine="davinci",  # Choose the appropriate GPT model
#                 prompt=f"User: {user_input}\nAI:",
#                 max_tokens=200,  # Adjust the response length
#                 stop=None,
#             )
#             recommendation = response.choices[0].text.strip()

#             HealthData.objects.create(
#                 exercise_info=exercise_info,
#                 diet_preferences=diet_preferences,
#                 sleep_patterns=sleep_patterns,
#                 emotion_status=emotion_status,
#                 recommendation=recommendation
#             )

#             return render(request, 'health_app/recommendations.html', {'recommendation': recommendation})

#     return render(request, 'health_app/dashboard.html', {'form': form})
# views.py
import openai
from django.conf import settings

from .models import Diet
from django.shortcuts import render

def health_dashboard(request):
    health_form = HealthInputForm()
    diet_form = DietForm()

    if request.method == 'POST':
        if 'health_form_submit' in request.POST:
            health_form = HealthInputForm(request.POST)
            # Rest of your health input handling code

        elif 'diet_form_submit' in request.POST:
            diet_form = DietForm(request.POST)
            if diet_form.is_valid():
                diet_form.save()

                user_input = f"Calories: {diet_form.cleaned_data['calories']}\nProtein: {diet_form.cleaned_data['protein']}\nCarbohydrates: {diet_form.cleaned_data['carbohydrates']}\nFats: {diet_form.cleaned_data['fats']}"

                openai.api_key = settings.OPENAI_API_KEY

                response = openai.Completion.create(
                    engine="davinci",  # Choose the appropriate GPT model
                    prompt=f"User input:\n{user_input}\nAI:",
                    max_tokens=150,  # Adjust the response length
                    stop=None,
                )
                recommendation = response.choices[0].text.strip()

                Diet.objects.filter(pk=diet_form.instance.pk).update(recommendation=recommendation)

    return render(request, 'health_app/dashboard.html', {'health_form': health_form, 'diet_form': diet_form})
# health_tracker/views.py
from django.shortcuts import render
from django.http import JsonResponse
import openai

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a health expert that specializes in health advice."}]
responses = [] 
def custom_chat_gpt(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    responses.append(ChatGPT_reply)
    
    return ChatGPT_reply

def health_tracker_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = custom_chat_gpt(user_input)
        response_points = response.split('\n')
        print(response_points)
        return render(request, "health_app/health_tracker.html", {"response_points": response_points})
    return render(request, "health_app/health_tracker.html")

    
def responses_view(request):
    return render(request, "health_app/responses.html", {"responses": responses})


# health_tracker/views.py
# health_tracker/views.py
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# from django.shortcuts import render

# def dash_visualization():
#     app = dash.Dash(__name__)

#     # Assume you have fetched these values from your data source
#     nutrients = ['Calories', 'Protein', 'Carbohydrates', 'Fats']
#     values = [2000, 100, 300, 70]

#     app.layout = html.Div([
#         dcc.Graph(id='nutrient-distribution'),
#     ])

#     @app.callback(
#         Output('nutrient-distribution', 'figure'),
#         Input('url', 'pathname')  # Use this callback to trigger data updates
#     )
#     def update_graphs(pathname):
#         figure = {
#             'data': [{'x': nutrients, 'y': values, 'type': 'bar', 'name': 'Nutrient Distribution'}],
#             'layout': {
#                 'title': 'Nutrient Distribution',
#             }
#         }
#         return figure

#     return app

# def dash_view(request):
#     dash_app = dash_visualization()
#     dash_app.layout = html.Div([dash_app.layout, dcc.Location(id='url')])
#     return render(request, "health_app/dash.html", {"dash_app": dash_app})


# health_tracker/views.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from django.shortcuts import render

def dash_view(request):
    app = dash.Dash(__name__)

    # Assume you have fetched these values from your data source
    nutrients = ['Calories', 'Protein', 'Carbohydrates', 'Fats']
    values = [2000, 100, 300, 70]

    app.layout = html.Div([
        dcc.Graph(id='nutrient-distribution'),
    ])

    @app.callback(
        Output('nutrient-distribution', 'figure'),
        Input('url', 'pathname')  # Use this callback to trigger data updates
    )
    def update_graphs(pathname):
        figure = {
            'data': [{'x': nutrients, 'y': values, 'type': 'bar', 'name': 'Nutrient Distribution'}],
            'layout': {
                'title': 'Nutrient Distribution',
            }
        }
        return figure

    return render(request, "health_app/dash.html")


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'todo_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'todo_app/login.html'




# newfiles are intregrated below this
from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

import requests
from django.shortcuts import render

def activity_calories(request):
    activity = 'cycling'
    api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
    response = requests.get(api_url, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})

    if response.status_code == requests.codes.ok:
        data = response.json()
        print(data)
    else:
        data = []

    return render(request, 'activity_calories.html', {'activity_data': data})

from django.shortcuts import render
import json
import requests

from django.shortcuts import render
import json
import requests

def calorie_calculator(request):
    total_calories = None

    if request.method == 'POST':
        query = request.POST.get('query')
        food_items = [item.strip() for item in query.split(',')]

        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='

        total_calories = 0
        

        for item in food_items:
            api_request = requests.get(
                api_url + item, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})
            print(f"API URL for {item}: {api_request.url}")  # Check the URL being requested
            print(f"API response for {item}: {api_request.content}") 
            print(f"data{item}:{api_request.content[1]}")
            api_response = api_request.content.decode('utf-8')
            api_data = json.loads(api_response)
            print(api_data)
            total_calories += float(api_data[0].get('calories', 0))
            print(total_calories)
            

    return render(request, 'calorie_calculator.html', {'total_calories': total_calories})

from django.shortcuts import render
import requests
import json

def exercise_nutrition(request):
    if request.method == 'POST':
        exercise_name = request.POST.get('exercise_name')
        api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={exercise_name}'
        response = requests.get(api_url, headers={'X-Api-Key': 'DWuCI3z4Qakky7/FdzHJHg==yRSlXi5uPF9CUECz'})

        if response.status_code == requests.codes.ok:
            api_data = json.loads(response.content.decode('utf-8'))
            exercise_info = api_data[0] if api_data else None
        else:
            exercise_info = None

        return render(request, 'exercise_nutrition.html', {'exercise_info': exercise_info})
    return render(request, 'exercise_nutrition.html')
