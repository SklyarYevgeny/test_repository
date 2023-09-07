from django.db import models

# Create your models here.
from django.db import models


class Articles(models.Model):
    name = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=100)
    full_text = models.TextField("Текст публикации", max_length=300)
    data = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
