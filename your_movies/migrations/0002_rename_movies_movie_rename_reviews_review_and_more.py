# Generated by Django 4.1.7 on 2023-03-26 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('your_movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': 'Movies'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Users'},
        ),
    ]
