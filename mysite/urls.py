from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.conf import settings
from django.conf.urls.static import static


def custom_logout(request):
    logout(request)
    return render(request, 'users/logout.html') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'), 
    path('profile/', user_views.profile_page,name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)