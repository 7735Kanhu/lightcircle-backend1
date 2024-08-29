from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Myuser)
class User(admin.ModelAdmin):
    list_display = ['id','age','privacy','receive_news','email','otp_code','nick_name','image','csrf_token','created_at']


@admin.register(Myteam)
class Myteam(admin.ModelAdmin):
    list_display = ['id','name','team_mode','team_note','image','timezone','email']
    
@admin.register(CompanyInformation)
class CompanyInformation(admin.ModelAdmin):
    list_display = ['company_name','business_regd_number','address','company_representative','phone']
    
@admin.register(Item_Information)
class Item_Information(admin.ModelAdmin):
    list_display = ['id','Name','Barcode','cost','Price','image','initial_quantity','created_at','feature_vector','myteam']

@admin.register(ItemAttribute)
class ItemAttribute(admin.ModelAdmin):
    list_display = ['id','attribute_name','attribute_value','attribute_type','name','item']
    
@admin.register(Permission)
class Permission(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ['id','name','permissions','role']
# class Role(admin.ModelAdmin):
#     list_display = ['name', 'permissions']

# admin.site.register(Role, RoleAdmin)
    
@admin.register(Permiteduser)
class Permiteduser(admin.ModelAdmin):
    list_display = ['id','email','otp_code','permission','additional_permission','permission_status','image','myteam']
    
@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ['transaction_id','created_at']
    
@admin.register(Stockin)
class stockin(admin.ModelAdmin):
    list_display = ['id','supplier','initial_quantity','present_quantity','created_at','memo','rack_no','myteam','transaction']
    
@admin.register(Stockout)
class stockout(admin.ModelAdmin):
    list_display = ['id','customer','initial_quantity','created_at','memo','rack_no','myteam','transaction']
    
@admin.register(Adjust)
class Adjust(admin.ModelAdmin):
    list_display = ['memo','initial_quantity','myteam','created_at','rack_no','transaction']
    
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ['id','type','name','mobile','email','address','memo','favorite']

@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display = ['id','type','name','mobile','email','address','memo','favorite']
    
# @admin.register(GFG)
# class GFG(admin.ModelAdmin):
#     list_display = ['name','contact','address']
    
# @admin.register(File)
# class File(admin.ModelAdmin):
#     list_display = ['file']
    
    
#admin.register(Person)
#class PersonAdmin(ImportExportModelAdmin):
#   list_display = ('name','email','location')
