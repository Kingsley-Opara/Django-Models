# Generated by Django 4.0.5 on 2022-06-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Title',
            field=models.CharField(max_length=200),
        ),
    ]
