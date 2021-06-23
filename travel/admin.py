from django.contrib import admin

# Register your models here.
from travel.models import Registered_users, Add_Tour, Add_blog, Add_gallery, Messagess, Otp, txn_details

admin.site.register(Registered_users)
admin.site.register(Add_Tour)
admin.site.register(Add_blog)
admin.site.register(Add_gallery)
admin.site.register(Messagess)
admin.site.register(Otp)
admin.site.register(txn_details)

