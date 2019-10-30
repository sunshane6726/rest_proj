from .models import UserEssay
from .models import UserAlbum, UserFiles, UserWeather
from rest_framework import serializers

class UserEssaySerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = UserEssay
        fields = ('pk', 'title', 'body', 'author_name', 'weather')


class UserAlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(use_url=True) # 이미지 업로드 하고 결과값을 알아챈후 확인 작업을 url로 하겠다는 것이 use_url = True라고 한다.

    class Meta:
        model = UserAlbum
        fields = ('pk', 'author_name', 'image', 'desc', 'weather')


class UserFileSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source = 'author.username')
    myfile = serializers.FileField(use_url=True) # 똑같이 url로 확인해 보겠다.

    class Meta:
        model = UserFiles
        fields = ('pk', 'author_name', 'myfile', 'desc', 'weather')

class UserWeatherSerializer(serializers.ModelSerializer):
    
    #author_name = serializers.ReadOnlyField(source = 'author.username')
    #myfile = serializers.FileField(use_url=True) # 똑같이 url로 확인해 보겠다.

    class Meta:
        model = UserWeather
        fields = ('pk', 'weather')

