from django.contrib import admin
from .models import *
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    exclude = ['id']
    
    
admin.site.register(Agentname)
admin.site.register(Polling_unit)
admin.site.register(Announced_lga_results)
admin.site.register(Announced_pu_results,PersonAdmin)
admin.site.register(Announced_ward_results, PersonAdmin)
admin.site.register(Announced_state_results, PersonAdmin)
admin.site.register(Ward)
admin.site.register(States)
admin.site.register(Party)
admin.site.register(Lga)
