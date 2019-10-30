from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from rest_framework.urlpatterns import format_suffix_patterns
from . import views



# django rest framework -> router -> url 라우터를 통해서 url를 인식하는 구나

router = DefaultRouter() #기본 초기값만 사용한다.
#router.register('', views.UserPostViewSet)
router.register('Essay', views.UserEssayViewSet)
router.register('Album', views.UserAlbumViewSet)
router.register('Files', views.UserFileViewSet)
router.register('Weather', views.UserWeatherViewSet)
# DefaultRouter 사용 x ==> API ROOT가 없다.

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    #path('post/', views.Postlist.as_view()),
    # 127.0.0.1:8000/post/<pk> == DetailView
    #path('post/<int:pk>/', views.PostDetail.as_view()),
    path('',include(router.urls))
]

#
#urlpatterns = format_suffix_patterns(urlpatterns)
