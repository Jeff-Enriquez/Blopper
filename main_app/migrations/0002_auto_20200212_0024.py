# Generated by Django 3.0.2 on 2020-02-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blop',
            name='article',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]