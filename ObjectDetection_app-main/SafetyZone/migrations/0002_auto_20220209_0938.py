# Generated by Django 3.1.2 on 2022-02-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SafetyZone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectconfig',
            name='configValue',
            field=models.CharField(max_length=200, null=True),
        ),
    ]