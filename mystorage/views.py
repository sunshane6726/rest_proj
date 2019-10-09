#from django.shortcuts import render 사용 안하구요
from rest_framework import viewsets
from .models import Album, Files
from .models import Essay
from .serializers import EssaySerializer
from .serializers import AlbumSerializer, FileSerializer
# Create your views here.
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status 

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
    


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all() # 모델에서 쿼리셋
    serializer_class = FileSerializer

    parser_classes = (MultiPartParser, FormParser) # 튜플로써

    # 다양한 이미더등 파일등의 인코딩 방식이 다양하다. 이미지 pdf gif jpeg 등
    # parser # pdf 파일을 넣어야하는 방법 
    # parser_class 지정


    # create() 오버라이딩을 해야한다. -> post() 방식으로 오버라이딩 
    # API HTTP -> get() post()등의 방식을 사용한다.

    def post(self, request, *args, **kwargs): # argument keyword argument 
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)



    

