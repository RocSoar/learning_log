# Generated by Django 4.1 on 2022-08-06 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0003_pizza_topping"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topping",
            old_name="name",
            new_name="topping",
        ),
    ]
