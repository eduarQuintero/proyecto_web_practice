from django.urls import path
from ProyectoWebApp.views import home, servicios, tienda, blog, contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name = "home"),
    path('servicios/', servicios, name = "servicios"),
    path('tienda/', tienda, name = "tienda"),
    path('blog/', blog, name = "blog"),
    path('contacto/', contacto, name = "contacto")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)