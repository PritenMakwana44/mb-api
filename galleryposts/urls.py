from django.urls import path
from galleryposts import views

urlpatterns = [
    path('galleryposts/', views.GalleryPostList.as_view()),
    path('galleryposts/<int:pk>/', views.GalleryPostDetail.as_view()),
]
