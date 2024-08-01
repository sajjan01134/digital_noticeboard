from rest_framework import viewsets
from .models import GeneralNotice, ExamNotice, AcademicNotice, DepartmentNotice, PlacementNotice, Department
from users.permissions import IsStaff
from .serializers import (
    GeneralNoticeSerializer, 
    ExamNoticeSerializer, 
    AcademicNoticeSerializer, 
    DepartmentNoticeSerializer, 
    PlacementNoticeSerializer, 
    DepartmentSerializer
)

from users.permissions import IsSuperAdmin
from rest_framework.permissions import AllowAny

class GeneralNoticeViewSet(viewsets.ModelViewSet):
    queryset = GeneralNotice.objects.all()
    serializer_class = GeneralNoticeSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "create":
            permission_classes = [IsSuperAdmin]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsSuperAdmin]
        elif self.action == "destroy":
            permission_classes = [IsSuperAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class ExamNoticeViewSet(viewsets.ModelViewSet):
    queryset = ExamNotice.objects.all()
    serializer_class = ExamNoticeSerializer


    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "create":
            permission_classes = [IsSuperAdmin]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsSuperAdmin]
        elif self.action == "destroy":
            permission_classes = [IsSuperAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class AcademicNoticeViewSet(viewsets.ModelViewSet):
    queryset = AcademicNotice.objects.all()
    serializer_class = AcademicNoticeSerializer

class DepartmentNoticeViewSet(viewsets.ModelViewSet):
    queryset = DepartmentNotice.objects.all()
    serializer_class = DepartmentNoticeSerializer
    permission_classes=[IsStaff]

class PlacementNoticeViewSet(viewsets.ModelViewSet):
    queryset = PlacementNotice.objects.all()
    serializer_class = PlacementNoticeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action == "create":
            permission_classes = [IsSuperAdmin]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsSuperAdmin]
        elif self.action == "destroy":
            permission_classes = [IsSuperAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    