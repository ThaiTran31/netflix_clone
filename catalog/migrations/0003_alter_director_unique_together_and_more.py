# Generated by Django 4.2.4 on 2023-08-11 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_video_file_alter_movie_age_limit"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="director",
            unique_together={("first_name", "last_name")},
        ),
        migrations.AlterUniqueTogether(
            name="star",
            unique_together={("first_name", "last_name")},
        ),
    ]