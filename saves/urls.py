from django.urls import path
from saves import views

urlpatterns = [
    path('saves/', views.SavesList.as_view()),
    path('saves/<int:pk>/', views.SavesDetail.as_view()),
]