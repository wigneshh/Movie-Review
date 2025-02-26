from django.urls import path
from . import views

urlpatterns = [
    path('logout/',views.logout_view, name='logout'),
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
    path('register/', views.register, name='register'),
    path('add_review/', views.add_review, name='add_review'),
    path('your-api-endpoint/', views.your_api_view, name='your_api'),

]
