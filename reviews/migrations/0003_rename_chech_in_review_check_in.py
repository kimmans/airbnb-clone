# Generated by Django 4.0.5 on 2022-07-04 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_room_alter_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='chech_in',
            new_name='check_in',
        ),
    ]
