# Generated by Django 4.2 on 2023-04-19 08:00

from django.db import migrations


def copy_data(apps, schema_editor):
    try:
        OldProfile = apps.get_model("oc_lettings_site", "Profile")
    except LookupError:
        # The old app isn't installed.
        return

    NewProfile = apps.get_model("profiles", "Profile")
    NewProfile.objects.bulk_create(
        NewProfile(
            user=old_object.user,
            favorite_city=old_object.favorite_city,
        )
        for old_object in OldProfile.objects.all()
    )


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0003_alter_profile_user"),
    ]

    operations = [
        migrations.RunPython(copy_data, migrations.RunPython.noop),
    ]
