"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace = 'home')),
    path('booking/', include('booking.urls', namespace='booking')),
    path('reserve_table/', include('reservation.urls', namespace='reservation')),
    path('testimonial/', include('testimonial.urls', namespace='testimonial')),
    path('team/', include('team.urls', namespace= 'team')),
    path('service/', include('service.urls', namespace = 'service')),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace = 'contact')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'EpicureResure Administration'                 
admin.site.index_title = 'Features Administration'
admin.site.site_title = "Epicure Admin"