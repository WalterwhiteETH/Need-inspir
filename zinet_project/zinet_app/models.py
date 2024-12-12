from django.db import models

# Create your models here.
import random
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


# Helper Functions
def generate_customer_number():
    """Generate a unique 7-digit customer number."""
    return random.randint(1000000, 9999999)


def generate_account_number():
    """Generate a unique 13-digit account number."""
    return random.randint(1000000000001, 9999999999999)


def generate_internal_account_number():
    """Generate a unique internal account number starting with 'ETB'."""
    return f"ETB{random.randint(1000000000001, 9999999999999)}"


class Staff(models.Model):
    ROLES = (
        ('maker', 'Maker'),
        ('checker', 'Checker'),
        ('auditor', 'Auditor'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),  # New role for super admin
        ('support', 'Support Staff'),  # For general support roles
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff')
    role = models.CharField(max_length=10, choices=ROLES)
    approved_by_manager = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Allow admin to create roles without approval
        if self.role != 'manager' and not self.approved_by_manager and self.role != 'admin':
            raise ValidationError(
                f"{self.role.capitalize()} users must be approved by a manager.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
