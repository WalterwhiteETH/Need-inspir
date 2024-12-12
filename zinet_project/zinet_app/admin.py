from django.contrib import admin
from .models import Staff, User  # Import User model
from rest_framework.exceptions import ValidationError


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'approved_by_manager')
    list_filter = ('role', 'approved_by_manager')
    search_fields = ('user__username',)

    def save_model(self, request, obj, form, change):
        if obj.role != 'manager' and not obj.approved_by_manager and not request.user.is_manager:
            raise ValidationError(
                "Only managers can approve non-manager staff."
            )
        super().save_model(request, obj, form, change)
