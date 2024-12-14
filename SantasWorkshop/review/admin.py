from django.contrib import admin

from SantasWorkshop.review.models import KidStatus


class KidStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'status',)
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(KidStatus, KidStatusAdmin)
