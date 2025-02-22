from django.contrib import admin
from django.urls import path, include
from customer_service.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),  # Root URL
    path('admin/', admin.site.urls),
    path('service/', include('customer_service.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]