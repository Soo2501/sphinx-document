from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField( max_length=250 )
    roll_no = models.CharField( max_length=250 )

    def __str__(self):
        return self.name
    
class Teachers(models.Model):
    name = models.CharField( max_length=250 )
    Schedule = models.CharField( max_length=250 )

    def __str__(self):
        return self.name

class Course(models.Model):
    name_name = models.CharField( max_length=250 )
    course_code = models.CharField( max_length=250 )

    def __str__(self):
        return self.name
