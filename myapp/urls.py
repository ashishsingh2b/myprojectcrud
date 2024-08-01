from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.user_profile, name='user_profile'),  # Profile URL
    path('', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
