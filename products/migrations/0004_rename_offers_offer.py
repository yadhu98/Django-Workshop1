# Generated by Django 3.2 on 2021-05-02 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_discount_offers_discount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='offers',
            new_name='offer',
        ),
    ]