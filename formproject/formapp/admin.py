from django.contrib import admin
from formapp.models import FromDetails
# Register your models here.
class FromDetailsAdmin(admin.ModelAdmin):
	list_display=('usn','name','age','stream','section')
admin.site.register(FromDetails,FromDetailsAdmin)
