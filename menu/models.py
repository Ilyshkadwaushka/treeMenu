from django.db import models

class MenuItem(models.Model):
    menu_name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'