# Generated by Django 4.2.4 on 2023-08-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_employee_lat_alter_employee_lon"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="udpated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]