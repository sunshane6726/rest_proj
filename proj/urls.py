

from django.contrib import admin
from django.urls import path, include
from mystorage import urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api-auth/', include('rest_framework.urls')), # 필터링 과정을 만들어야 한다.

]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
