from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200, verbose_name="Текст")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Тема")
    text = models.TextField(verbose_name="Текст")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.get_short_description()

    def get_short_description(self):
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text



