from email.mime import image
from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


match_status = (
    ("Division 1 League", "Division 1 League"),
    ("Division 2 League", "Division 2 League"),
    ("League Cup, Division 1", "League Cup, Division 1"),
    ("League Cup, Division 2", "League Cup, Division 2"),
    ("Champions League", "Champions League"),
    ("Europa League", "Europa League"),
    ("Super Cup", "Super Cup"),
    ("International Match", "International Match"),
)


class Club(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = CloudinaryField('image', null=True)

    def __str__(self):
        return self.name


class Bet(models.Model):
    home_name = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home', null=True)
    away_name = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away', null=True)
    competition = models.CharField(null=True, max_length=100, choices=match_status)
    home_ht = models.IntegerField(blank=True, null=True)
    home_ft = models.IntegerField(blank=True, null=True)
    away_ht = models.IntegerField(blank=True, null=True)
    away_ft = models.IntegerField(blank=True, null=True)
    played = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)
    home = models.FloatField(blank=True, null=True)
    away = models.FloatField(blank=True, null=True)
    draw = models.FloatField(blank=True, null=True)
    home_h1 = models.FloatField(blank=True, null=True)
    away_h1 = models.FloatField(blank=True, null=True)
    draw_h1 = models.FloatField(blank=True, null=True)
    home_cleansheet_yes = models.FloatField(blank=True, null=True)
    home_cleansheet_no = models.FloatField(blank=True, null=True)
    away_cleansheet_yes = models.FloatField(blank=True, null=True)
    away_cleansheet_no = models.FloatField(blank=True, null=True)
    score_home_over_yes = models.FloatField(blank=True, null=True)
    score_home_over_no = models.FloatField(blank=True, null=True)
    score_away_over_yes = models.FloatField(blank=True, null=True)
    score_away_over_no = models.FloatField(blank=True, null=True)
    total_yc_over_yes = models.FloatField(blank=True, null=True)
    total_yc_over_no = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.home_name} vs {self.away_name}'

 
