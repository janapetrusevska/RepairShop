from django.contrib import admin
from .models import *

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ("type", "max_speed")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Car, CarAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", )


admin.site.register(Manufacturer, ManufacturerAdmin)

class WorkshopManufacturerAdmin(admin.TabularInline):
    model = WorkshopManufacturer
    extra = 0

class WorkshopAdmin(admin.ModelAdmin):
    inlines = [WorkshopManufacturerAdmin, ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Workshop, WorkshopAdmin)

class ScheduledRepairAdmin(admin.ModelAdmin):
    list_display = ("code", "user")
    # exclude = ("user", )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(ScheduledRepair,ScheduledRepairAdmin)
