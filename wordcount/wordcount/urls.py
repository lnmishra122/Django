from django.contrib import admin
from django.urls import path
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
]

urlpatterns += staticfiles_urlpatterns( )

