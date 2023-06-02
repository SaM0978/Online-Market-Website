# Generated by Django 4.2.1 on 2023-05-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("description", models.TextField(blank=True, null=True)),
                ("print", models.FloatField()),
                ("is_sold", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ("name",), "verbose_name_plural": "Categories"},
        ),
    ]