# Generated by Django 4.2.1 on 2023-06-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppCoder", "0005_delete_curso"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="profesion",
            field=models.CharField(max_length=40),
        ),
    ]
