from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('search', views.search,name='search'),
    path('single/<int:pk>', views.single,name='single'),
    path('header-articles/<int:nid>', views.header_single,name='header-single'),
    path('showbiz-articles/<int:pin>', views.showbiz_single,name='showbiz-single'),
    path('tech-articles/<int:pin>', views.tech_single,name='tech-single'),
    path('sport-articles/<int:nop>', views.sport_single,name='sport-single'),
    path('travel-articles/<int:suk>', views.travel_single,name='travel-single'),
    path('about', views.about_us,name='about-us'),
    path('contact', views.contact,name='contact'),
    path('category', views.category,name='category'),
    path('sport-category', views.sport_category,name='sport-category'),
    path('travel-category', views.travel_category,name='travel-category'),
    path('showbiz-category', views.showbiz_category,name='showbiz-category'),
    path('tech-category', views.tech_category,name='tech-category'),
]