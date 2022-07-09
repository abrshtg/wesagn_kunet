from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('birth/', views.birth, name='birth'),
    path('death/', views.death, name='death'),
    path('marriage/', views.marriage, name='marriage'),
    path('divorce/', views.divorce, name='divorce'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout')
]
