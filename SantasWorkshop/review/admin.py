from django.contrib import admin

class KidStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'updated_by', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('updated_by', 'updated_at')

    def save_model(self, request, obj, form, change):
        """Automatically set the 'updated_by' field to the current admin."""
        if not obj.pk:  # New record
            obj.updated_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(KidStatus, KidStatusAdmin)
