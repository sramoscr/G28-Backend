from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('product/', admin.site.urls),
    path('almacen/', include('almacen.urls'))
]
