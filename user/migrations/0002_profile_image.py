# Generated by Django 5.2.1 on 2025-05-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='Profile_Images'),
        ),
    ]
