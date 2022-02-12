from django.db import models

# Create your models here.
class KeysRelatorioFiscal(models.Model):
    key = models.CharField(verbose_name="Chave de uso", max_length=6, blank=False)
    expiration_date = models.DateTimeField(verbose_name="Data de expiração")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name, verbose_name_plural = 'Chave', 'Chaves'
        ordering = ("id",)

    def __str__(self):
        return self.key