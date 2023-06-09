# Generated by Django 4.2 on 2023-06-13 18:42

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('all_reviews', '0003_alls_tags_alter_alls_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alls',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
