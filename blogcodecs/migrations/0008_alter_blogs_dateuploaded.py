# Generated by Django 3.2.4 on 2021-06-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcodecs', '0007_contactqueries_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='dateUploaded',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
