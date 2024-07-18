from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GeneralNoticeViewSet, 
    ExamNoticeViewSet, 
    AcademicNoticeViewSet, 
    DepartmentNoticeViewSet, 
    PlacementNoticeViewSet, 
    DepartmentViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'general-notices', GeneralNoticeViewSet)
router.register(r'exam-notices', ExamNoticeViewSet)
router.register(r'academic-notices', AcademicNoticeViewSet)
router.register(r'department-notices', DepartmentNoticeViewSet)
router.register(r'placement-notices', PlacementNoticeViewSet)
router.register(r'departments', DepartmentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
