from django.db import models


class Peticao(models.Model):
    name = models.CharField(max_length=40, null=False)
    body = models.TextField()
    category = models.CharField(max_length=40, null=False, default="Geral")
    description = models.CharField(max_length=80, null=True)

    def __str__(self) -> str:
        return self.name
