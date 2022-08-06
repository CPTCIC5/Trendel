from django.test import TestCase
from seller.models import Seller,Product
from django.contrib.auth.models import User
from customer.models import Order

class TestSellerModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin',password='Iamreal123')
        self.seller = Seller.objects.create(
            shop_name='A2 Styles',seller_name='Piyush Jain',seller_user=self.user,
            shop_is_registered=True,seller_ID_method="PAN Card",seller_ID='WRW2VDFWRQ',
            shop_address ='Civil Line')
        #⚡⚡⚡

        self.product = Product.objects.create(
            product_name='xyz',product_image='xyz.jpeg',price=100,offer_price=80,size='220C',
            material_type='100% COTTON',description='desc',generic_name='UH',fit_type='xyz',
            material_composition='efhj',quantity=3,product_seller=self.user.seller
        )
        #⏭️⏭️⏭️⏭️⏭️

        self.order = Order.objects.create(ordered=self.product,reciever_name='Aryan',
        phone_no='8349811004',street_address='Wall Street',zipcode='483501',order_quantity=5,
        ordered_by=self.user)


    def test_seller_user(self):
        self.assertEqual(self.seller.seller_user,self.user)

    def test_seller_info(self):
        self.assertEqual(self.seller.shop_name,'A2 Styles')
        self.assertEqual(self.seller.seller_name,'Piyush Jain')
        self.assertEqual(self.seller.shop_address,'Civil Line')
        self.assertEqual(self.seller.seller_ID,'WRW2VDFWRQ')

    def test_seller_choices(self):
        self.assertEqual(self.seller.seller_ID_method,'PAN Card')
        self.assertEqual(self.seller.shop_is_registered,True)
    #⚡⚡

    def test_product_seller(self):
        self.assertEqual(self.product.product_seller,self.user.seller)

    def test_product_info(self):
        self.assertEqual(self.product.product_name,'xyz')
        self.assertEqual(self.product.price,100)
        self.assertEqual(self.product.offer_price,80)
        self.assertEqual(self.product.size,'220C')
        self.assertEqual(self.product.material_type,'100% COTTON')
        self.assertEqual(self.product.description,'desc')
        self.assertEqual(self.product.generic_name,'UH')
        self.assertEqual(self.product.fit_type,'xyz')
        self.assertEqual(self.product.material_composition,'efhj')
        self.assertEqual(self.product.quantity,3)

    def test_product_image(self):
        self.assertEqual(self.product.product_image,'xyz.jpeg')
    #⏭️⏭️⏭️⏭️⏭️⏭️

    def test_order_product(self):
        self.assertEqual(self.order.ordered,self.product)

    def test_order_info(self):
        self.assertEqual(self.order.reciever_name,'Aryan')
        self.assertEqual(self.order.phone_no,'8349811004')
        self.assertEqual(self.order.street_address,'Wall Street')
        self.assertEqual(self.order.zipcode,'483501')
        self.assertEqual(self.order.order_quantity,5)

    def test_order_author(self):
        self.assertEqual(self.order.ordered_by,self.user)

    def test_order_status(self):
        self.assertIsNone(self.order.status)