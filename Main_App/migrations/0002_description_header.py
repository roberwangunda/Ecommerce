# Generated by Django 3.1.3 on 2021-01-05 06:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description_header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
