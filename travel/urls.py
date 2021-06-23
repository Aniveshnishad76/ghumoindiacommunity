"""travel_tour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from travel import views
from travel.views import Review

urlpatterns = [
    path('',views.Index_pages,name="Index_pages"),
    path('home_pages', views.home_pages, name="home_pages"),
    path('About_pages', views.About_pages, name="About_pages"),
    path('Gallery_pages', views.Gallery_pages, name="gallery_pages"),
    path('faq_pages', views.faq_pages, name="faq_pages"),
    path('testimonial_pages', views.testimonial_pages, name="testimonial_pages"),
    path('destination_pages', views.destination_pages, name="destination_pages"),
    path('blog_pages', views.blog_pages, name="blog_pages"),
    path('blog_single_pages', views.blog_single_pages, name="blog_single_pages"),
    path('contact_pages', views.contact_pages, name="contact_pages"),
path('home_pages_user', views.home_pages_user, name="home_pages_user"),
    path('About_pages_user', views.About_pages_user, name="About_pages_user"),
    path('Gallery_pages_user', views.Gallery_pages_user, name="gallery_pages_user"),
    path('faq_pages_user', views.faq_pages_user, name="faq_pages_user"),
    path('testimonial_pages_user', views.testimonial_pages_user, name="testimonial_pages_user"),
    path('destination_pages_user', views.destination_pages_user, name="destination_pages_user"),
    path('blog_pages_user', views.blog_pages_user, name="blog_pages_user"),
    path('blog_single_pages_user', views.blog_single_pages_user, name="blog_single_pages_user"),
    path('contact_pages_user', views.contact_pages_user, name="contact_pages_user"),
    path('Login_pages', views.Login_pages, name="Login_pages"),
    path('Data_register', views.Data_register, name="Data_register"),
path('user_home', views.user_home, name="user_home"),
path('my_profile', views.my_profile, name="my_profile"),
path('Data_login', views.Data_login, name="Data_login"),
    path('destination_single_full<id>',views.destination_single_full, name="destination_single_full"),
    path('Review',views.review,name='Review'),
path('logout',views.logout,name='logout'),
path('My_profile',views.My_profile,name='My_profile'),
    path('Update_profile<id>', views.Update_profile, name="Update_profile"),
path('Messages',views.Messages,name='Messages'),
path('Check_otp',views.Check_otp,name='Check_otp'),
path('search_place',views.search_place,name='search_place'),
path('Change_password',views.Change_password,name='Change_password'),
path('Check_password',views.Check_password,name='Check_password'),
path('Check_password_otp',views.Check_password_otp,name='Check_password_otp'),
path('Check_new_password',views.Check_new_password,name='Check_new_password'),
path('booking_page<id>',views.booking_page,name='booking_page'),
path('checkout', views.checkout, name="checkout"),
path('handlerequest/', views.handlerequest, name="handlerequest"),
path('confirmation', views.confirmation, name="confirmation"),
path('confirmation_failed', views.confirmation_failed, name="confirmation_failed"),
    path('dashboard_history', views.dashboard_history, name="dashboard_history"),
path('booking_detail<id>',views.booking_detail,name='booking_detail'),
]
