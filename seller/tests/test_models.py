from django.test import TestCase
from seller.models import Seller
from django.contrib.auth.models import User

class TestSellerModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin',password='Iamreal123')
        self.seller = Seller.objects.create(
            shop_name='A2 Styles',seller_name='Piyush Jain',seller_user=self.user,
            shop_is_registered=True,seller_ID_method="PAN Card",seller_ID='WRW2VDFWRQ',
            shop_address ='Civil Line')

    def test_seller_user(self):
        self.assertEqual(self.seller.seller_user,self.user)

    def test_info(self):
        self.assertEqual(self.seller.shop_name,'A2 Styles')
        self.assertEqual(self.seller.seller_name,'Piyush Jain')
        self.assertEqual(self.seller.shop_address,'Civil Line')
        self.assertEqual(self.seller.seller_ID,'WRW2VDFWRQ')

    def test_choices(self):
        self.assertEqual(self.seller.seller_ID_method,'PAN Card')
        self.assertEqual(self.seller.shop_is_registered,True)
