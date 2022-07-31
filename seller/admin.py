from django.contrib import admin
from .models import Seller

admin.site.site_header = 'STAFF LOGIN'
admin.site.site_title = 'ADMIN PORTAL'
admin.site.index_title = 'DB-MODELS'

admin.site.register(Seller)