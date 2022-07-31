from django.db import models
from django.contrib.auth.models import User

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
    seller_registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shop_name} - {self.seller_user}"
    
    class Meta:
        ordering = ['-seller_registered_at']