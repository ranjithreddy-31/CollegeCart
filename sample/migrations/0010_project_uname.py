# Generated by Django 2.2.5 on 2019-09-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0009_auto_20190911_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='uname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]