from django.urls import path
from gallerycomments import views

urlpatterns = [
    path('gallerycomments/', views.GalleryCommentList.as_view()),
    path('gallerycomments/<int:pk>/', views.GalleryCommentDetail.as_view())
]
