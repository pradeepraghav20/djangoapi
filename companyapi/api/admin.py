from django.contrib import admin
from api.models import Employee,Company


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')



class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company,CompanyAdmin)




# Register your models here.
