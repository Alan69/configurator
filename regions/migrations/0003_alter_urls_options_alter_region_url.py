# Generated by Django 4.1.1 on 2022-11-16 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_urls'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name_plural': 'Urls'},
        ),
        migrations.AlterField(
            model_name='region',
            name='url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions.urls'),
        ),
    ]
