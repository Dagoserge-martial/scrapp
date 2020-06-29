from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class FilmeAfricaineAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'duree',
        'disponibilite',
        'description',
        'image',
        'myimage',
        'lien_detail',
        'lien_lien',
        'types',
    )
    list_filter = (
        'id',
        'name',
        'duree',
        'disponibilite',
        'description',
        'image',
        'myimage',
        'lien_detail',
        'lien_lien',
        'types',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.FilmeAfricaine, FilmeAfricaineAdmin)
