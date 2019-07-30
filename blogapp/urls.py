from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
   
]