from rest_framework.serializers import ModelSerializer
from .models import *

class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'