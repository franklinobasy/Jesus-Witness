# Generated by Django 4.1.7 on 2023-03-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("witness", "0002_remove_editorprofile_phone_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("NONE", "None"), ("MALE", "Male"), ("FEMALE", "Female")],
                default="NONE",
                max_length=50,
            ),
        ),
    ]
