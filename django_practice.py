from django.db import models

class option(models.Model):
    curr_price = models.FloatField()
    strike = models.FloatField()
    risk_free_rate = models.FloatField()
    time_to_mat = models.FloatField()

CREATE TABLE myapp_option(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "curr_price" REAL,
    "strike" REAL,
    "risk_free_rate" REAL,
    "time_to_mat" REAL
);