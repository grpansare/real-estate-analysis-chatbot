from rest_framework import serializers
from .models import RealEstateData


class RealEstateDataSerializer(serializers.ModelSerializer):
    """Serializer for RealEstateData model"""
    class Meta:
        model = RealEstateData
        fields = '__all__'


class QueryResponseSerializer(serializers.Serializer):
    """Serializer for query response"""
    summary = serializers.CharField()
    chart_data = serializers.ListField()
    table_data = serializers.ListField()
    areas = serializers.ListField()
