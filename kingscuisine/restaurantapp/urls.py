from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('book-a-table/', views.book_table, name='book_table'),
    path('contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
