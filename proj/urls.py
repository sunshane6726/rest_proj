

from django.contrib import admin
from django.urls import path, include
from mystorage import urls
from userstorage import urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mystorage', include('mystorage.urls')),
    path('api-auth/', include('rest_framework.urls')), # 필터링 과정을 만들어야 한다.
    path('', include('userstorage.urls')),
    #path('api-auth/', include('rest_framework.urls')), # 로그인 기능을 해줄수 있는 rest_framework.urls이다.
    path('api-token-auth/', obtain_auth_token), # Token 의 획득하는법

]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
