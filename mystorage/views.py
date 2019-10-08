#from django.shortcuts import render 사용 안하구요
from rest_framework import viewsets
from .models import Album, Files
from .models import Essay
from .serializers import EssaySerializer
from .serializers import AlbumSerializer, FileSerializer
# Create your views here.
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all() # 모델에서 쿼리셋
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',) # 튜플로써 저장이 된다.

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

        # 현재 request을 보낸 유저
        # == self.request.user

        # 현재 필터링해야한다.
    def get_queryset(self):
        qs = super().get_queryset() # super() 부모클래스라고 보면된다.
        # 지지고 볶는 다면 생각하면 된다.

        if self.request.user.is_authenticated: # 로그인이 되어 있다면
            qs = qs.filter(author = self.request.user) # 필터 또는 exclude

        else:
            qs = qs.none() # 로그아웃이 되어 있다면

        return qs

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all() # 모델에서 쿼리셋
    serializer_class = AlbumSerializer
    pass

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all() # 모델에서 쿼리셋
    serializer_class = FileSerializer
    pass

