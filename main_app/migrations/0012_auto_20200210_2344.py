# Generated by Django 3.0.3 on 2020-02-10 23:44

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_merge_20200210_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blop',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
