# Generated by Django 4.1.1 on 2022-11-22 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0005_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='belong_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions.city'),
        ),
    ]
