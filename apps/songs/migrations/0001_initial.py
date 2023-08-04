# Generated by Django 3.2.4 on 2023-02-09 11:02

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Name')),
                ('description', models.TextField(max_length=200, verbose_name='description')),
                ('rating', models.IntegerField(verbose_name='rating')),
                ('songs_duration', models.IntegerField(default=45, verbose_name='duration')),
                ('thumbail', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('music', cloudinary.models.CloudinaryField(max_length=255, verbose_name='music')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.genre')),
            ],
        ),
    ]
