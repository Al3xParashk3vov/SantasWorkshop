from django.contrib import admin

from SantasWorkshop.presents.models import Present


@admin.register(Present)
class PresentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user', 'image')
    list_filter = ('user',)
    search_fields = ('name', 'description', 'user__username')
