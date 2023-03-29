from django.urls import path
from saves_gallery import views

urlpatterns = [
    path('saves_gallery/', views.Save_galleryList.as_view()),
    path('saves_gallery/<int:pk>/', views.Save_galleryDetail.as_view()),
]