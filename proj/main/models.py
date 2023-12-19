from django.db import models

# Create your models here.

class Coordinate_System(models.Model):

    zone_types = [("C1", "C1"), ("C2", "C2"), ("C3", "C3"), ("Not Zone", "Not Zone")]
    SC_types = [("SC63", "SC63"), ("MSK", "MSK")]
    
    name_calib_in_TBC = models.CharField(blank=False, max_length=50)
    name_calib_rus = models.CharField(blank=False, max_length=50)
    SC = models.CharField(max_length=4, choices=SC_types)
    zone = models.CharField(max_length=8, choices=zone_types)

    
    
class Upload_file(models.Model):

    separator_type = [(" ", "Пробел"), ("   ", "Табуляция"), (",", "Запятая"), (";", "Точка с запятой")]

    file_in = models.FileField(upload_to="upload_file")
    separator = models.CharField(max_length=25, blank=False, choices=separator_type)
    time_upload = models.DateTimeField(auto_now_add=True)  