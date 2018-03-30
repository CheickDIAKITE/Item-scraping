from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace="api")),
]

urlpatterns += [
    path('django-rq/', include('django_rq.urls')),
]
