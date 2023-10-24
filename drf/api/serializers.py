from rest_framework.serializers import ModelSerializer
from .models import HostelPost, Dante
class HotelSerializer(ModelSerializer):
    class Meta:
        model = HostelPost
        fields = '__all__'
class DanteSerializer(ModelSerializer):
    class Meta:
        model=Dante
        fields='__all__' 