from django.contrib import admin
from django.urls import include, path

from django.conf import settings # include import for static file config
from django.conf.urls.static import static # include import for static file config

urlpatterns = [
    # ... snip ...
    path('admin/', admin.site.urls), # created by default
    path('community/', include('app_name.urls')), # app 1
    path('contact/', include('app_name.urls')), # app 2
    # ... snip ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # static file config