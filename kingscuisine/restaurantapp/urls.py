from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-a-table/', views.book_table, name='book_table'),
    path('contact/', views.contact, name='contact'),
]
