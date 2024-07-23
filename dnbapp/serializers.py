from rest_framework import serializers
from .models import GeneralNotice, ExamNotice, AcademicNotice, DepartmentNotice, PlacementNotice, Department

class GeneralNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralNotice
        fields = '__all__'

class ExamNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamNotice
        fields = '__all__'

class AcademicNoticeSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = AcademicNotice
        fields = '__all__'

class DepartmentNoticeSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = DepartmentNotice
        fields = '__all__'

class PlacementNoticeSerializer(serializers.ModelSerializer):
     

    class Meta:
        model = PlacementNotice
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
