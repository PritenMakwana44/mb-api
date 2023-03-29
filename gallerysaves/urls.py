from django.urls import path
from gallerysaves import views

urlpatterns = [
    path('gallerysaves/', views.GallerySaveList.as_view()),
    path('gallerysaves/<int:pk>/', views.GallerySaveDetail.as_view()),
]