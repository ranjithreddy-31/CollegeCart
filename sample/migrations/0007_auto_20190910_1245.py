# Generated by Django 2.2.5 on 2019-09-10 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0006_auto_20190910_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='i',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
