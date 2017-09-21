# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# from django.utils.translation import ugettext_lazy as _
#
# from apps_user.models.user import User
#
#
# @admin.register(User)
# class UserAdmin(DjangoUserAdmin):
#     """Define admin model for custom User model with no email field."""
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from apps_user.models import User
from apps_user.models.userProfile import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile',)

    def get_location(self, instance):
        return instance.profile.location

    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)