# Generated by Django 3.1.3 on 2021-01-05 08:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main_App', '0003_description_header_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description_header',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
