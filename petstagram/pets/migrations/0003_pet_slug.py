# Generated by Django 4.2 on 2023-05-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_create_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]
