# Generated by Django 3.2.12 on 2022-03-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20220313_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Event Name'),
        ),
    ]