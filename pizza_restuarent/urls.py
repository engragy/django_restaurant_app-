""" pizza_restuarent URL Configuration """
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users_app import views as users_app_views

urlpatterns = [
    path('', include("ordering_app.urls")),
    path("register/", users_app_views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)