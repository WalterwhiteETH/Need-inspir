from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Staff
from .serializers import StaffSerializer
from django.core.exceptions import ValidationError


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def perform_create(self, serializer):
        user = self.request.user
        role = serializer.validated_data.get('role')
        if role != 'manager' and not user.staff.role == 'manager':
            raise ValidationError("Only managers can create or approve staff.")
        serializer.save()
