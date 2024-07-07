from django.urls import path, include
from django.contrib.auth import views 
from .views import CustomLogoutView ,login,generate_image,home

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', home, name='home'),
    path('generate_image/', generate_image, name='generate_image'),
]
# Register your models here.
