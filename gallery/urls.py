from django.urls import path
from gallery import views

urlpatterns = [
    path('gallery/', views.GalleryPostList.as_view()),
    path('gallery/<int:pk>/', views.GalleryPostDetail.as_view())
]