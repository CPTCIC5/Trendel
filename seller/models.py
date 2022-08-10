from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension

id_choices = {
    ("Aadhar Card","Aadhar Card"),
    ("PAN Card","PAN Card")
}

class Seller(models.Model):
    shop_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    seller_user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop_is_registered =  models.BooleanField(default=False)
    seller_ID_method = models.CharField(choices=id_choices,max_length=20)
    seller_ID = models.CharField(max_length=12,unique=True,null=True,blank=True)
    shop_address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=10,unique=True)
    seller_registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shop_name} - {self.seller_user}"
    
    class Meta:
        ordering = ['-seller_registered_at']

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    category_image = models.ImageField(validators=[validate_image_file_extension],null=True,blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural  = 'Category'

class Coupon(models.Model):
    product = models.ForeignKey(related_name="Product",on_delete=models.CASCADE)
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class Product(models.Model):
    product_name = models.CharField(max_length=60)
    product_category = models.ManyToManyField(Category)
    product_image = models.ImageField(upload_to='product_images',validators=[validate_image_file_extension])
    price = models.FloatField()
    offer_price = models.FloatField()
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE,null=True,blank=True)
    size = models.CharField(max_length=60)
    material_type = models.CharField(max_length=60)
    description = models.TextField()
    generic_name = models.CharField(max_length=60)
    fit_type = models.CharField(max_length=60)
    material_composition = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField()
    product_seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_published_at = models.DateTimeField(auto_now_add=True)

    @property
    def discount_percentage(self):
        pass

    def __str__(self):
        return f"{self.product_name} -{self.product_seller}"

    class Meta:
        ordering = ['-product_seller','-product_published_at']