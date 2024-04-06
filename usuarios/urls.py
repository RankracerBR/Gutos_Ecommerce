from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('pagina_conta/', views.pagina_conta, name="pagina_conta"),
    path('pagina_usuarios/', views.pagina_usuarios, name="pagina_usuarios"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)