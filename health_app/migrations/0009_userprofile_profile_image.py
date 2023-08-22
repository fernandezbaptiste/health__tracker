# Generated by Django 3.1 on 2023-08-22 18:41

from django.db import migrations, models
import health_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0008_healthreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default=health_app.models.default_profile_image_path, null=True, upload_to='profile_images/'),
        ),
    ]