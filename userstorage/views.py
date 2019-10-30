from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
#from django.shortcuts import render
#from userpost.models import UserPost
#from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework import status 
from userstorage.models import UserAlbum, UserFiles
from userstorage.models import UserEssay, UserWeather
from userstorage.serializers import UserEssaySerializer
from userstorage.serializers import UserAlbumSerializer, UserFileSerializer, UserWeatherSerializer
from userstorage.pagination import UserEssayPagination
from userstorage.pagination import UserAlbumPagination
from userstorage.pagination import UserFilePagination
from userstorage.pagination import UserWeatherPagination

from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse
# Create your views here.

class UserEssayViewSet(viewsets.ModelViewSet):
    queryset = UserEssay.objects.all().order_by('pk')
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # 응답이 가능한것과 비응답 허가의 차이를 잘 알고 있어야한다.  IsAuthenticated / IsAuthenticateOrReadOnly/ IsAdminUser 차이 구별
    
    serializer_class = UserEssaySerializer
    pagination_class = UserEssayPagination


    filter_backends = [SearchFilter]
    search_fields = ('title','body','weather') # 튜플로 할때 ,을 적어주어라 아니면 'title'은 문자열로 인식을 하게 된다.
    '''
    # @action(method = ['post']) post방식을 이용할때
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 "TestAction"을 Custom Api을 할수있는 방법
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("TestAction")
    '''
      
    def get_queryset(self):
        # 여기내부쿼리셋 지지고 볶는 다음에 return 값을 한다는 편이 괜찮다. 필터링 비인증 로그인 기능 등

        qs = super().get_queryset()
        #qs = qs.filter(author__id = 2) # 이미 지정하는 것보다 지금 로그인한 유저의 글만 필터링을 해라 종류로 해줘라

        #qs = qs.filter(author=self.request.user) # 그 유저로 필터링 글

        # 만약 로그인이 안되어 있다면 -> 비어있는 쿼리셋을 리턴하라
        if self.request.user.is_authenticated: # 인증된 요청이라고 한다면
        # 지금 만약 로그린이 되어있다면 -> 로그인한 유저의 글만 필터링해라
            qs = qs.filter(author=self.request.user)
            
        else:
            qs = qs.none() # 비어있는 요청만 해달라

        # .filter .exclude 등이 있다.
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #author_field의 self.request.user을 save 메소드에 저장

class UserAlbumViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # 응답이 가능한것과 비응답 허가의 차이를 잘 알고 있어야한다.  IsAuthenticated / IsAuthenticateOrReadOnly/ IsAdminUser 차이 구별
    queryset = UserAlbum.objects.all().order_by('pk')
    serializer_class = UserAlbumSerializer
    pagination_class = UserAlbumPagination

    filter_backends = [SearchFilter]
    search_fields = ('image','desc','weather') # 튜플로 할때 ,을 적어주어라 아니면 'title'은 문자열로 인식을 하게 된다.
    # 어떤 컬럼을 기반으로 검색을 할 건지
    
    def get_queryset(self):
        # 여기내부쿼리셋 지지고 볶는 다음에 return 값을 한다는 편이 괜찮다. 필터링 비인증 로그인 기능 등

        qs = super().get_queryset()
        #qs = qs.filter(author__id = 2) # 이미 지정하는 것보다 지금 로그인한 유저의 글만 필터링을 해라 종류로 해줘라

        #qs = qs.filter(author=self.request.user) # 그 유저로 필터링 글

        # 만약 로그인이 안되어 있다면 -> 비어있는 쿼리셋을 리턴하라
        if self.request.user.is_authenticated: # 인증된 요청이라고 한다면
        # 지금 만약 로그린이 되어있다면 -> 로그인한 유저의 글만 필터링해라
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none() # 비어있는 요청만 해달라

        # .filter .exclude 등이 있다.
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #author_field의 self.request.user을 save 메소드에 저장

class UserFileViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # 응답이 가능한것과 비응답 허가의 차이를 잘 알고 있어야한다.  IsAuthenticated / IsAuthenticateOrReadOnly/ IsAdminUser 차이 구별
    queryset = UserFiles.objects.all().order_by('pk')
    serializer_class = UserFileSerializer
    pagination_class = UserFilePagination

    filter_backends = [SearchFilter]
    search_fields = ('myfile','desc','weather') # 튜플로 할때 ,을 적어주어라 아니면 'title'은 문자열로 인식을 하게 된다.
    # 어떤 컬럼을 기반으로 검색을 할 건지
    
    def get_queryset(self):
        # 여기내부쿼리셋 지지고 볶는 다음에 return 값을 한다는 편이 괜찮다. 필터링 비인증 로그인 기능 등

        qs = super().get_queryset()
        #qs = qs.filter(author__id = 2) # 이미 지정하는 것보다 지금 로그인한 유저의 글만 필터링을 해라 종류로 해줘라

        #qs = qs.filter(author=self.request.user) # 그 유저로 필터링 글

        # 만약 로그인이 안되어 있다면 -> 비어있는 쿼리셋을 리턴하라
        if self.request.user.is_authenticated: # 인증된 요청이라고 한다면
        # 지금 만약 로그린이 되어있다면 -> 로그인한 유저의 글만 필터링해라
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none() # 비어있는 요청만 해달라

        # .filter .exclude 등이 있다.
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #author_field의 self.request.user을 save 메소드에 저장

class UserWeatherViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # 응답이 가능한것과 비응답 허가의 차이를 잘 알고 있어야한다.  IsAuthenticated / IsAuthenticateOrReadOnly/ IsAdminUser 차이 구별
    queryset = UserWeather.objects.all().order_by('pk')
    serializer_class = UserWeatherSerializer
    pagination_class = UserWeatherPagination

    filter_backends = [SearchFilter]
    search_fields = ('weather') # 튜플로 할때 ,을 적어주어라 아니면 'title'은 문자열로 인식을 하게 된다.
    # 어떤 컬럼을 기반으로 검색을 할 건지
    
    def get_queryset(self):
        # 여기내부쿼리셋 지지고 볶는 다음에 return 값을 한다는 편이 괜찮다. 필터링 비인증 로그인 기능 등

        qs = super().get_queryset()
        #qs = qs.filter(author__id = 2) # 이미 지정하는 것보다 지금 로그인한 유저의 글만 필터링을 해라 종류로 해줘라

        #qs = qs.filter(author=self.request.user) # 그 유저로 필터링 글

        # 만약 로그인이 안되어 있다면 -> 비어있는 쿼리셋을 리턴하라
        if self.request.user.is_authenticated: # 인증된 요청이라고 한다면
        # 지금 만약 로그린이 되어있다면 -> 로그인한 유저의 글만 필터링해라
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none() # 비어있는 요청만 해달라

        # .filter .exclude 등이 있다.
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #author_field의 self.request.user을 save 메소드에 저장

