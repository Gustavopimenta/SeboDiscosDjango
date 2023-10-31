from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('discos/', include('discos.urls')),
    path('', include('discos.urls')),
]


    #path('discos/', views.lista_discos, name='lista_discos'),
    #path('discos/<int:disco_id>/', views.detalhes_disco, name='detalhes_disco'),