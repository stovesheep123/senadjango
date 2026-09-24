from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomAdminUserCreationForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomAdminUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "nickname", "is_staff")

    fieldsets = UserAdmin.fieldsets + (
        ("追加情報", {"fields": ("nickname", "birth_date")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("追加情報", {"fields": ("email", "nickname")}),
    )

    # 🛠️ Fix: Strip out 'usable_password' dynamically to prevent the FieldError
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.add_fieldsets:
            clean_fieldsets = []
            for name, field_options in self.add_fieldsets:
                if 'fields' in field_options:
                    # Filter out 'usable_password' if Django tries to inject it automatically
                    new_fields = tuple(f for f in field_options['fields'] if f != 'usable_password')
                    clean_fieldsets.append((name, {'fields': new_fields}))
                else:
                    clean_fieldsets.append((name, field_options))
            self.add_fieldsets = tuple(clean_fieldsets)
