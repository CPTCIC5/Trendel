from django.db import models
from seller.models import Product
from django.contrib.auth.models import User

STATUS = (
    ('Pending','Pending'),
    ('Out for delivery','Out for delivery'),
    ('Delivered','Delivered')
)

# Create your models here.
class Order(models.Model):
    ordered = models.ForeignKey(Product,on_delete=models.CASCADE)
    reciever_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=12)
    street_address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=6)
    order_quantity = models.PositiveIntegerField(default=1)
    ordered_by = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=STATUS,null=True,blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    #city =

    def __str__(self):
        return f"({self.ordered}) - {self.ordered_by}"

    class Meta:
        ordering = ['-ordered_at']