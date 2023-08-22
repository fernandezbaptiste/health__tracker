from django.urls import path,include
from . import views



urlpatterns = [
    # path('register/', views.user_registration, name='register'),
    # path('login/', views.user_login, name='login'),
    # ... other URLs ...

    # Create similar URL patterns for adding Diet, Sleep, Emotion, and other data types
    # path('', views.health_dashboard, name='health_dashboard'),
    path('track/', views.health_tracker_view, name='track'),
    path('responses/', views.responses_view, name='responses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    # path('dash/', views.dash_view, name='dash_view'),
    path('main/', views.home, name='home'),
    path('activity/', views.activity_calories, name='activity_calories'),
    path('cal/', views.calorie_calculator, name='calorie_calculator'),
    path('exe/', views.exercise_nutrition, name='calorie_calculator'),
    path('workout/', views.workout_view, name='workout'),
    path('', views.index_view, name='index'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
