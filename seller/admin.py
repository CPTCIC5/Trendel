from django.contrib import admin
from .models import ProductReview, Seller,Product

admin.site.site_header = 'STAFF LOGIN'
admin.site.site_title = 'ADMIN PORTAL'
admin.site.index_title = 'DB-MODELS'

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(ProductReview)