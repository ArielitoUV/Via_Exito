from django.contrib import admin
from django.urls import path
from core import views
from core.views import registrar_usuario,iniciar_sesion,gestionar_perfil

urlpatterns = [
    path('',views.index,name="index"),
    path('iniciosesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registroap/', registrar_usuario, name='registrar_usuario'),
    path('gestionperfil/', gestionar_perfil, name='gestionar_perfil'),
    path('rs/',views.rs,name="rs"),
    path('donaciones/',views.donaciones,name="donaciones"),
    path('pasoapaso/',views.pasoapaso,name="pasoapaso"),
    path('unicolla/',views.unicolla,name="unicolla"),
    path('secundaria/',views.secundaria,name="secundaria"),
    path('acercade/',views.acercade,name="acercade"),
    path('index2/',views.index2,name="index2"),
    path('infobecas/',views.infobecas,name="infobecas"),
    path('admin/', admin.site.urls),
]
