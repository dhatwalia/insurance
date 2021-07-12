from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .insurance import Automotive, Disability, Health, House, Life
from .rates import *

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

from .models import User, UserProfile
from .forms import UserAdminForm


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user', 'dob')
    ordering = ('user',)
    list_select_related = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)


class UserProfileAdminInline(admin.TabularInline):
    model = UserProfile


class UserAdmin(DjangoUserAdmin):
    inlines = [
        UserProfileAdminInline,
    ]

    # readonly_fields = ('private_uuid', 'public_id')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'display_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # (_('Ids'), {'fields': ('private_uuid', 'public_id')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    list_display = ('email', 'first_name', 'last_name', 'display_name', 'is_staff')
    search_fields = ('first_name', 'last_name', 'display_name', 'email')
    ordering = ('email',)

    form = UserAdminForm


admin.site.register(User, UserAdmin)
admin.site.register(Automotive)
admin.site.register(Disability)
admin.site.register(Health)
admin.site.register(House)
admin.site.register(Life)
