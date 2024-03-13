from rest_framework import serializers

from .models import ShortsUrl

class ShortsUrlSerializer(serializers.ModelSerializer):

        class Meta:
            model = ShortsUrl
            fields = '__all__'