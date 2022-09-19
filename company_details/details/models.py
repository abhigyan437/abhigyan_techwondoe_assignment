from django.db import models

class Company(models.Model):
    uuid = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=200)
    company_ceo = models.CharField(max_length=200)
    company_address = models.TextField(max_length=400)
    company_inception = models.DateField()

    def __str__(self):
        return str(self.uuid)

class Team(models.Model):
    uuid = models.IntegerField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    team_lead_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_lead_name
