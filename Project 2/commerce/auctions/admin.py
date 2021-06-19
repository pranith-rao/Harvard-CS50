from django.contrib import admin
from auctions.models import User,auction,bids

# Register your models here.
admin.site.register(User)
admin.site.register(auction)
admin.site.register(bids)
