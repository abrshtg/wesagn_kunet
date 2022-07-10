from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('birth/', views.birth, name='birth'),
    path('birth/<int:pk>/', views.birth_detail, name='birth-detail'),
    path('death/', views.death, name='death'),
    path('death/<int:pk>/', views.death_detail, name='death-detail'),
    path('marriage/', views.marriage, name='marriage'),
    path('marriage/<int:pk>/', views.marriage_detail, name='marriage-detail'),
    path('divorce/', views.divorce, name='divorce'),
    path('divorce/<int:pk>/', views.divorce_detail, name='divorce-detail'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('about/', views.about, name='about')
    
]
