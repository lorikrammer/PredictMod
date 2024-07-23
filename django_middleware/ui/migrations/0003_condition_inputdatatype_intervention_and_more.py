# Generated by Django 4.1.3 on 2024-07-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ui", "0002_pendingmodel_link_releasedmodel_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Condition",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="InputDataType",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("conditions", models.ManyToManyField(to="ui.condition")),
            ],
        ),
        migrations.CreateModel(
            name="Intervention",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("conditions", models.ManyToManyField(to="ui.condition")),
                ("input_data_type", models.ManyToManyField(to="ui.inputdatatype")),
            ],
        ),
        migrations.AddField(
            model_name="inputdatatype",
            name="interventions",
            field=models.ManyToManyField(to="ui.intervention"),
        ),
        migrations.AddField(
            model_name="condition",
            name="input_data_types",
            field=models.ManyToManyField(to="ui.inputdatatype"),
        ),
        migrations.AddField(
            model_name="condition",
            name="interventions",
            field=models.ManyToManyField(to="ui.intervention"),
        ),
        migrations.AddField(
            model_name="releasedmodel",
            name="condition",
            field=models.ManyToManyField(to="ui.condition"),
        ),
        migrations.AddField(
            model_name="releasedmodel",
            name="input_type",
            field=models.ManyToManyField(to="ui.inputdatatype"),
        ),
        migrations.AddField(
            model_name="releasedmodel",
            name="intervention",
            field=models.ManyToManyField(to="ui.intervention"),
        ),
    ]
