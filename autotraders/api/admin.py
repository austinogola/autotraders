from django.contrib import admin
from .models import Bid,Bidder,Copart_Account

class BidderAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'surname', 'email','password', 
    'phone', 'allowed_max_bid','bidder_type','copart_accounts')  # Customize this based on your model fields

    def save_model(self, request, obj, form, change):
        print(obj)
        coport_object={}
        username=f'{obj.name.lower()}_{obj.surname.lower()}'
        email=obj.email
        password=obj.password
        for number in obj.copart_accounts:
  	        #Add to coparts
            print(number)

        

        # Call the original save_model method to save the instance
        super().save_model(request, obj, form, change)


admin.site.register(Bidder, BidderAdmin)


admin.site.register(Bid)
# admin.site.register(Bidder)
admin.site.register(Copart_Account)

# Register your models here.
