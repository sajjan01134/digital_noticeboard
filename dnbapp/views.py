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

class GeneralNoticeViewSet(viewsets.ModelViewSet):
    queryset = GeneralNotice.objects.all()
    serializer_class = GeneralNoticeSerializer

class ExamNoticeViewSet(viewsets.ModelViewSet):
    queryset = ExamNotice.objects.all()
    serializer_class = ExamNoticeSerializer

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
    