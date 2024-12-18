from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from SantasWorkshop.accounts.forms import ProfileEditForm, CustomUserForm
from SantasWorkshop.accounts.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('age', 'first_name', 'last_name')


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'is_staff')  # Ensure is_staff is displayed here
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        ('Credentials', {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Include is_staff
        ('Important Dates', {'fields': ('last_login',)}),
    )




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'age', 'email', 'presents_count', 'profile_image')
    list_filter = ('age', 'user__is_active')
    search_fields = ('user__username', 'first_name', 'last_name', 'user__email')
    readonly_fields = ('presents_count',)

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def full_name(self, obj):
        return f"{obj.first_name or ''} {obj.last_name or ''}".strip() or "N/A"

    def profile_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No image"

    profile_image.short_description = 'Profile Picture'
    full_name.short_description = 'Full Name'
