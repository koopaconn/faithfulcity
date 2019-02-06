from django.db import models

class model_church(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    denomination = models.CharField(max_length=128)
    services = models.IntegerField()
    serviceTimes = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    podcast = models.CharField(max_length=128)
    pastor = models.CharField(max_length=128)
    noCampuses = models.IntegerField()
    size = models.IntegerField()
    ageRange13_24 = models.IntegerField()
    ageRange25_35 = models.IntegerField()
    ageRange35_55 = models.IntegerField()
    ageRange55 = models.IntegerField()
    perFamily = models.IntegerField()
    startDate = models.DateField()
    STATE_CHOICES = (('Yes',1),('No',2),)
    sundaySchool = models.CharField(max_length=3, choices=STATE_CHOICES)
    smallGroups = models.CharField(max_length=3, choices=STATE_CHOICES)
    PREACH_STYLE = (('Topical',1),('Verse-by-verse',2),('Narrative',3),('Other',4),('Mix',5),)
    preachingStyle = models.CharField(max_length=128, choices=PREACH_STYLE)
    leadPic = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("churches:detail",kwargs={'pk':self.pk})

class model_churchpic(models.Model):
    pic = models.ImageField()
    car = models.ForeignKey(model_church,models.CASCADE,related_name='churchpic')
    def __str__(self):
            return str(self.name)
