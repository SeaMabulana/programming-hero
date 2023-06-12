from django.urls import path # include import
from . import views # include import

app_name = 'AppName'
urlpatterns = [
    path('', views.function, name='community'),
    path('contact/', views.function, name='contact'),
]