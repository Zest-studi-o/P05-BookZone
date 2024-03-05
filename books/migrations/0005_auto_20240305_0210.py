# Generated by Django 3.2.24 on 2024-03-05 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='book',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='book',
            name='wishlist',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
