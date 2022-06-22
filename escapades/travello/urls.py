from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
urlpatterns = [
    path('bloghome', views.bloghome, name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='events-about'),

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('destination_list/<str:city_name>/', views.destination_list, name='destination_list'),
    path('destination_list/destination_details/<str:city_name>', views.destination_details, name='destination_details'),
    path('destination_details/<str:city_name>/', views.destination_details, name='destination_details'),
    path('destination_list/destination_details/pessanger_detail_def/<str:city_name>/',views.pessanger_detail_def,name='pessanger_detail_def'),
    path('upcoming_trips/', views.upcoming_trips, name='upcoming_trips'),
    path('destination_list/destination_details/pessanger_detail_def/pessanger_detail_def/card_payment/', views.card_payment, name='card_payment'),
    path('destination_list/destination_details/pessanger_detail_def/pessanger_detail_def/otp_verification/', views.otp_verification, name='otp_verification'),
    path('destination_list/destination_details/pessanger_detail_def/pessanger_detail_def/net_payment/', views.net_payment, name='net_payment'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

