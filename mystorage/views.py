#from django.shortcuts import render 사용 안하구요
from rest_framework import viewsets
from .models import Essay
#from .serializers import EssaySerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all() # 모델에서 쿼리셋
#   serializer_class = EssaySerializer
