from rest_framework import serializers
from .models import VIP, History


class VIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIP
        fields = ['name', 'occupation', 'networth', 'gender', 'age']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['name', 'result', 'timestamp']
