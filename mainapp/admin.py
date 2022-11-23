from django.forms import ModelChoiceField, ModelForm
from django import forms

from django.contrib import admin

from .models import *


class NotebookAdminFrom(ModelForm):
    MIN_RESOLUTION = (488, 488)

    def __str__(self, *args, **kwargs):
        super().__str__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображениея с минималным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION)


class NotebookAdmin(admin.ModelAdmin):
    form = NotebookAdminFrom

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug="notebooks"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug="smartphone"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook)
admin.site.register(Smartphone)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(someModel)
