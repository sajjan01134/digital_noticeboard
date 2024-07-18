from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)

    

class GeneralNotice(models.Model):
    topic = models.CharField(max_length=255)
    main_content = models.TextField()
    image = models.ImageField(upload_to='notices/', blank=True, null=True)
    document = models.FileField(upload_to='notices/', blank=True, null=True)
    date = models.DateField()

    

class ExamNotice(models.Model):
    topic = models.CharField(max_length=255)
    main_content = models.TextField()
    image = models.ImageField(upload_to='exam_notices/', blank=True, null=True)
    document = models.FileField(upload_to='exam_notices/', blank=True, null=True)
    sem = models.IntegerField()
    date = models.DateField()

 

class AcademicNotice(models.Model):
    topic = models.CharField(max_length=255)
    main_content = models.TextField()
    image = models.ImageField(upload_to='academic_notices/', blank=True, null=True)
    document = models.FileField(upload_to='academic_notices/', blank=True, null=True)
    sem = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()

   

class DepartmentNotice(models.Model):
    topic = models.CharField(max_length=255)
    main_content = models.TextField()
    image = models.ImageField(upload_to='department_notices/', blank=True, null=True)
    document = models.FileField(upload_to='department_notices/', blank=True, null=True)
    sem = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()

    

class PlacementNotice(models.Model):
    topic = models.CharField(max_length=255)
    main_content = models.TextField()
    image = models.ImageField(upload_to='placement_notices/', blank=True, null=True)
    document = models.FileField(upload_to='placement_notices/', blank=True, null=True)
    sem = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=255)
    specific_details = models.TextField()
    date = models.DateField()

   
