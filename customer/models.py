from django.db import models
from seller.models import Product
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension

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
        ordering = ['-ordered_at','-ordered']


class GiftProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    sender_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"({self.product} - {self.recipient_name})"

    class Meta:
        ordering = ['-product']


Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)

class ProductReview(models.Model):
    product_reviewed = models.ForeignKey(Product,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=Rating_CHOICES,default=1)
    photo = models.ImageField(upload_to='Customer-Photos',validators=[validate_image_file_extension])
    message = models.CharField(max_length=150,default='No Message')
    reviewed_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.product_reviewed}) - {self.author}"

    class Meta:
        ordering = ['-reviewed_at','-product_reviewed']