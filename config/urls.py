from django.contrib import admin
from django.urls import include
from django.urls import path

from shortener.views import redirect_to_long_url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    path('<int:short_link_id>/', redirect_to_long_url)
]
