from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),  # Ruta para ver el home en tu navegador (usa la clase de tu frontend)
    path('', views.PostList.as_view(), name='home'),  # Ruta para ver el home en tu navegador (usa la clase de tu frontend)
]