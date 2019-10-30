from .models import Essay
from .models import Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    
    #author_name = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name', 'weather')


class AlbumSerializer(serializers.ModelSerializer):

    #author_name = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(use_url=True) # 이미지 업로드 하고 결과값을 알아챈후 확인 작업을 url로 하겠다는 것이 use_url = True라고 한다.

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc', 'weather')


class FileSerializer(serializers.ModelSerializer):
    
    #author_name = serializers.ReadOnlyField(source = 'author.username')
    myfile = serializers.FileField(use_url=True) # 똑같이 url로 확인해 보겠다.

    class Meta:
        model = Files
        fields = ('pk', 'author_name', 'myfile', 'desc', 'weather')
