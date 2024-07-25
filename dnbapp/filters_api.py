from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import GeneralNotice,ExamNotice,AcademicNotice, DepartmentNotice,PlacementNotice
from .serializers import (
    GeneralNoticeSerializer, 
    ExamNoticeSerializer, 
    AcademicNoticeSerializer, 
    DepartmentNoticeSerializer, 
    PlacementNoticeSerializer, 
)

class GeneralNoticeFilterView(generics.ListAPIView):
    serializer_class =GeneralNoticeSerializer


    queryset = GeneralNotice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'topic']  # Define fields for filtering

class ExamNoticeFilterView(generics.ListAPIView):
    serializer_class = ExamNoticeSerializer


    queryset = ExamNotice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'topic']  # Define fields for filtering

class  AcademicNoticeFilterView(generics.ListAPIView):
    serializer_class =  AcademicNoticeSerializer


    queryset =  AcademicNotice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'department', 'sem', 'topic']  # Define fields for filtering

class DepartmentNoticeFilterView(generics.ListAPIView):
    serializer_class = DepartmentNoticeSerializer


    queryset = DepartmentNotice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'department', 'sem', 'topic']  # Define fields for filtering

class PlacementNoticeFilterView(generics.ListAPIView):
    serializer_class = PlacementNoticeSerializer


    queryset = PlacementNotice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'department', 'sem', 'topic']  # Define fields for filtering



