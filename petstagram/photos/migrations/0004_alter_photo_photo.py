# Generated by Django 4.2 on 2023-05-16 19:37

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_photo_alter_photo_tagged_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet-photos', validators=[petstagram.photos.validators.validate_file_size]),
        ),
    ]
