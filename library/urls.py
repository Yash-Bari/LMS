from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views. CustomLoginView.as_view(), name='login'),
    path('home', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('view_issued_books/', views.view_issued_books, name='view_issued_books'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('logout/', views.custom_logout, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
