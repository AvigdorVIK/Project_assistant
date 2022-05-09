from django.db import models

class Tasks(models.Model):
    title = models.TextField (blank=True)
    content = models.TextField (blank=True)
    created = models.DateField ()
    cat = models.ForeignKey ('Category', on_delete = models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField (max_length=100, db_index=True)

    def __str__(self):
        return self.name
