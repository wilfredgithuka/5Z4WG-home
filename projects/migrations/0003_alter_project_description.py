# Generated by Django 4.1 on 2022-10-08 19:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_options_project_manuals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]