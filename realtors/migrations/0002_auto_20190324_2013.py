# Generated by Django 2.1.7 on 2019-03-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
