from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('birth/', views.birth, name='birth'),
    path('death/', views.death, name='death'),
    path('marriage/', views.marriage, name='marriage'),
    path('divorce/', views.divorce, name='divorce')
]
