# Generated by Django 3.2 on 2021-05-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemcode', models.CharField(max_length=16)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.CharField(max_length=5000),
        ),
    ]