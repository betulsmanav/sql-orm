# Generated by Django 4.0.4 on 2022-05-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_book_name_book_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
