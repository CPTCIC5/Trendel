from rest_framework.serializers import ModelSerializer
from .models import *

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class GiftProductSerializer(ModelSerializer):
    class Meta:
        model = GiftProduct
        fields = '__all__'

class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'