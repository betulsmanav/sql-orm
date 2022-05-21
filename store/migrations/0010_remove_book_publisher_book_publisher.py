# Generated by Django 4.0.4 on 2022-05-21 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_book_publisher_book_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.publisher'),
            preserve_default=False,
        ),
    ]