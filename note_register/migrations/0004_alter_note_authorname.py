# Generated by Django 4.1.3 on 2022-11-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_register', '0003_alter_note_authorname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='authorname',
            field=models.CharField(max_length=100),
        ),
    ]
