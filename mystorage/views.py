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
from mystorage.pagination import EssayPagination
from mystorage.pagination import ImagePagination
from mystorage.pagination import FilePagination

class PostViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all() # 모델에서 쿼리셋
    serializer_class = EssaySerializer
    pagination_class = EssayPagination

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body','weather') # 튜플로써 저장이 된다.
    
    '''
    # @action(method = ['post']) post방식을 이용할때
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 "TestAction"을 Custom Api을 할수있는 방법
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("TestAction")
    '''
    

    

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all() # 모델에서 쿼리셋
    serializer_class = AlbumSerializer
    pagination_class = ImagePagination

    filter_backends = [SearchFilter]
    search_fields = ('image','desc','weather') # 튜플로써 저장이 된다.
   
    '''
    # @action(method = ['post']) post방식을 이용할때
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 "TestAction"을 Custom Api을 할수있는 방법
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("TestAction")
    '''


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all() # 모델에서 쿼리셋
    serializer_class = FileSerializer
    pagination_class = FilePagination

    filter_backends = [SearchFilter]
    search_fields = ('myfile','desc','weather') # 튜플로써 저장이 된다.

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

    '''
    # @action(method = ['post']) post방식을 이용할때
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 "TestAction"을 Custom Api을 할수있는 방법
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("TestAction")
    '''




    

