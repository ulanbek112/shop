# Generated by Django 4.1.3 on 2022-11-17 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Частота процессора')),
                ('ram', models.CharField(max_length=255, verbose_name='Оперативная память')),
                ('video', models.CharField(max_length=255, verbose_name='видеокарта')),
                ('tine_without_charge', models.CharField(max_length=255, verbose_name='Время работу аккуьулятора')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
