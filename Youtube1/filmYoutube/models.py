from django.db import models

# Create your models here.

class FilmeAfricaine(models.Model):
    """Model definition for FilmeAfricaine."""

    # TODO: Define fields here
    name = models.CharField(max_length=250)
    duree = models.CharField(max_length=250, blank=True, null=True)
    disponibilite = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    image = models.URLField()
    myimage = models.FileField(upload_to='africafimes', blank=True, null=True)
    lien_detail = models.URLField( blank=True, null=True)
    lien_lien = models.URLField()
    types = models.PositiveIntegerField(default=0)
    class Meta:
        """Meta definition for FilmeAfricaine."""

        verbose_name = 'FilmeAfricaine'
        verbose_name_plural = 'FilmeAfricaines'

    def __str__(self):
        """Unicode representation of FilmeAfricaine."""
        return self.name

# python manage.py admin_generator filmYoutube >> filmYoutube/admin.py