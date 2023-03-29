from django.urls import path
from comments_gallery import views

urlpatterns = [
    path('comments_gallery/', views.Comment_galleryList.as_view()),
    path('comments_gallery/<int:pk>/', views.Comment_galleryDetail.as_view())
]