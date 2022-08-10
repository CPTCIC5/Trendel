from django.contrib import admin
from .models import Category, Seller,Product,Coupon

admin.site.site_header = 'STAFF LOGIN'
admin.site.site_title = 'ADMIN PORTAL'
admin.site.index_title = 'DB-MODELS'

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Coupon)