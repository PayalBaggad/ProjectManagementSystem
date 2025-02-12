""" This model is used to register the models in the admin panel """

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from accounts.forms import User, CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    """This class defines the Custom User Admin"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = [
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    list_filter = ["is_staff", "is_active", "is_superuser", "role"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]


admin.site.register(User, CustomUserAdmin)
