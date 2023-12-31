from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "contacto"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', views.contacto, name="contactanos"),
    path("acerca_de/", views.acerca_de, name="acerca_de"),
    path("", include("apps.posts.urls")),
    path(
        "login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="usuarios/logout.html"),
        name="logout",
    ),
    path("usuarios/", include("apps.usuarios.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)