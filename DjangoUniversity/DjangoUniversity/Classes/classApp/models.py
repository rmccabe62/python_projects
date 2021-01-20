from django.db import models

# creating the djangoClasses for the project
class djangoClasses(models.Model):
    title = models.CharField(max_length=50, help_text="Python")
    courseNum = models.IntegerField(max_length=3, help_text="Course Number")
    instructName = models.CharField(max_length=50, help_text="Instructor's Name")
    durationDays = models.IntegerField(max_length=2, help_text="Days to complete course")
    djangoClassesManager = models.Manager()

    # creating the titles for the objects
    def __str__(self):
        return self.title
