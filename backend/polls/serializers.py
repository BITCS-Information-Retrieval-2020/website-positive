from rest_framework import serializers

from polls.models import UserModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('url','author','title','content',)