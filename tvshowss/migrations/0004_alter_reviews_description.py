# Generated by Django 4.2 on 2023-06-12 19:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshowss', '0003_remove_reviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
