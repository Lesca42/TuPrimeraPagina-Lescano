from django.contrib import admin
from django.urls import path
from APP1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temp1/', views.Mod1, name="Mod1"),
    path('temp2/', views.Mod2, name="Mod2"),
    path('temp3/', views.Mod3, name="Mod3"),
]