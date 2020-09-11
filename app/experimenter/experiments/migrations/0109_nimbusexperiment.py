# Generated by Django 3.0.7 on 2020-09-10 20:29

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import experimenter.experiments.constants


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_project"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiments", "0108_auto_20200817_1534"),
    ]

    operations = [
        migrations.CreateModel(
            name="NimbusExperiment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Draft", "Draft"),
                            ("Review", "Ready for Sign-Off"),
                            ("Ship", "Ready to Ship"),
                            ("Accepted", "Accepted by Normandy"),
                            ("Live", "Live"),
                            ("Complete", "Complete"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Draft",
                        max_length=255,
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("public_description", models.TextField(blank=True, null=True)),
                ("is_paused", models.BooleanField(default=False)),
                (
                    "proposed_duration",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(1000)],
                    ),
                ),
                (
                    "proposed_enrollment",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(1000)],
                    ),
                ),
                (
                    "firefox_min_version",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("55.0", "Firefox 55.0"),
                            ("56.0", "Firefox 56.0"),
                            ("57.0", "Firefox 57.0"),
                            ("58.0", "Firefox 58.0"),
                            ("59.0", "Firefox 59.0"),
                            ("60.0", "Firefox 60.0"),
                            ("61.0", "Firefox 61.0"),
                            ("62.0", "Firefox 62.0"),
                            ("63.0", "Firefox 63.0"),
                            ("64.0", "Firefox 64.0"),
                            ("65.0", "Firefox 65.0"),
                            ("66.0", "Firefox 66.0"),
                            ("67.0", "Firefox 67.0"),
                            ("68.0", "Firefox 68.0"),
                            ("69.0", "Firefox 69.0"),
                            ("70.0", "Firefox 70.0"),
                            ("71.0", "Firefox 71.0"),
                            ("72.0", "Firefox 72.0"),
                            ("73.0", "Firefox 73.0"),
                            ("74.0", "Firefox 74.0"),
                            ("75.0", "Firefox 75.0"),
                            ("76.0", "Firefox 76.0"),
                            ("77.0", "Firefox 77.0"),
                            ("78.0", "Firefox 78.0"),
                            ("79.0", "Firefox 79.0"),
                            ("80.0", "Firefox 80.0"),
                            ("81.0", "Firefox 81.0"),
                            ("82.0", "Firefox 82.0"),
                            ("83.0", "Firefox 83.0"),
                            ("84.0", "Firefox 84.0"),
                            ("85.0", "Firefox 85.0"),
                            ("86.0", "Firefox 86.0"),
                            ("87.0", "Firefox 87.0"),
                            ("88.0", "Firefox 88.0"),
                            ("89.0", "Firefox 89.0"),
                            ("90.0", "Firefox 90.0"),
                            ("91.0", "Firefox 91.0"),
                            ("92.0", "Firefox 92.0"),
                            ("93.0", "Firefox 93.0"),
                            ("94.0", "Firefox 94.0"),
                            ("95.0", "Firefox 95.0"),
                            ("96.0", "Firefox 96.0"),
                            ("97.0", "Firefox 97.0"),
                            ("98.0", "Firefox 98.0"),
                            ("99.0", "Firefox 99.0"),
                            ("100.0", "Firefox 100.0"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "firefox_max_version",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("55.0", "Firefox 55.0"),
                            ("56.0", "Firefox 56.0"),
                            ("57.0", "Firefox 57.0"),
                            ("58.0", "Firefox 58.0"),
                            ("59.0", "Firefox 59.0"),
                            ("60.0", "Firefox 60.0"),
                            ("61.0", "Firefox 61.0"),
                            ("62.0", "Firefox 62.0"),
                            ("63.0", "Firefox 63.0"),
                            ("64.0", "Firefox 64.0"),
                            ("65.0", "Firefox 65.0"),
                            ("66.0", "Firefox 66.0"),
                            ("67.0", "Firefox 67.0"),
                            ("68.0", "Firefox 68.0"),
                            ("69.0", "Firefox 69.0"),
                            ("70.0", "Firefox 70.0"),
                            ("71.0", "Firefox 71.0"),
                            ("72.0", "Firefox 72.0"),
                            ("73.0", "Firefox 73.0"),
                            ("74.0", "Firefox 74.0"),
                            ("75.0", "Firefox 75.0"),
                            ("76.0", "Firefox 76.0"),
                            ("77.0", "Firefox 77.0"),
                            ("78.0", "Firefox 78.0"),
                            ("79.0", "Firefox 79.0"),
                            ("80.0", "Firefox 80.0"),
                            ("81.0", "Firefox 81.0"),
                            ("82.0", "Firefox 82.0"),
                            ("83.0", "Firefox 83.0"),
                            ("84.0", "Firefox 84.0"),
                            ("85.0", "Firefox 85.0"),
                            ("86.0", "Firefox 86.0"),
                            ("87.0", "Firefox 87.0"),
                            ("88.0", "Firefox 88.0"),
                            ("89.0", "Firefox 89.0"),
                            ("90.0", "Firefox 90.0"),
                            ("91.0", "Firefox 91.0"),
                            ("92.0", "Firefox 92.0"),
                            ("93.0", "Firefox 93.0"),
                            ("94.0", "Firefox 94.0"),
                            ("95.0", "Firefox 95.0"),
                            ("96.0", "Firefox 96.0"),
                            ("97.0", "Firefox 97.0"),
                            ("98.0", "Firefox 98.0"),
                            ("99.0", "Firefox 99.0"),
                            ("100.0", "Firefox 100.0"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "firefox_channel",
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, "Firefox Channel"),
                            ("Nightly", "Nightly"),
                            ("Beta", "Beta"),
                            ("Release", "Release"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "objectives",
                    models.TextField(
                        blank=True,
                        default="If we <do this/build this/create this change in the experiment> for <these users>, then we will see <this outcome>.\nWe believe this because we have observed <this> via <data source, UR, survey>.\n     \nOptional - We believe this outcome will <describe impact> on <core metric>\n    ",
                        null=True,
                    ),
                ),
                ("bugzilla_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "features",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("FEATURE 1", "FEATURE 1"),
                                ("FEATURE 2", "FEATURE 2"),
                            ],
                            max_length=255,
                            null=True,
                        ),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "audience",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AUDIENCE 1", "AUDIENCE 1"),
                            ("AUDIENCE 2", "AUDIENCE 2"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owned_nimbusexperiments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("projects", models.ManyToManyField(blank=True, to="projects.Project")),
            ],
            options={
                "verbose_name": "NimbusExperiment",
                "verbose_name_plural": "NimbusExperiments",
            },
            bases=(experimenter.experiments.constants.ExperimentConstants, models.Model),
        ),
    ]
