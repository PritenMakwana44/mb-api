from django.urls import path
from contact import views

"""
URL paths to contact
"""

urlpatterns = [
    path('contact/', views.ContactDetail.as_view()),
]
