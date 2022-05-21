# Generated by Django 4.0.4 on 2022-05-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_book_publisher_id_remove_publisher_publisher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(to='store.publisher'),
        ),
    ]
