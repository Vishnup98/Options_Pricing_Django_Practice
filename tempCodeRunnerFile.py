from django.db import models

class option(models.Model):
    curr_price = models.FloatField()
    strike = models.FloatField()
    risk_free_rate = models.FloatField()
    time_to_mat = models.FloatField()
