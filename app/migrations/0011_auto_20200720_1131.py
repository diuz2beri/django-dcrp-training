# Generated by Django 3.0.5 on 2020-07-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200720_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='special_general',
            field=models.CharField(blank=True, choices=[('ad', 'ADMINISTRATION'), ('sg', 'AGRICULTURE'), ('ar', 'ARCHITECTURE'), ('br', 'BROADCASTING OR MEDIA'), ('co', 'COMMUNICATIONS'), ('cm', 'COMMUNITY DEVELOPMENT'), ('de', 'DEFENSE'), ('di', 'DISASTER MANAGEMENT'), ('ec', 'ECONOMICS'), ('eu', 'EDUCATION AND TRAINING AND PUBLIC AWARENESS'), ('el', 'ELECTRICIAN'), ('fi', 'FINANCE'), ('fr', 'FIRE AND SEARCH AND RESCUE'), ('fi', 'FIRST AID INSTRUCTOR'), ('fo', 'FOREIGN AFFAIRS'), ('he', 'HEALTH EDUCATION'), ('la', 'LAND VALUATION'), ('lo', 'LOGISTICS'), ('ma', 'MANAGEMENT'), ('mr', 'MARITIME'), ('me', 'MEDICAL METEREOLOGICAL_SERVICES'), ('mi', 'MINERAL RESOURCES'), ('na', 'NATIONAL PLANNING'), ('po', 'POLICE'), ('', 'PRISON SERVICES'), ('pu', 'PUBLIC HEALTH'), ('pb', 'PUBLIC WORK AND WATER'), ('re', 'RED CROSS'), ('rs', 'RESEARCH DEPARTMENT'), ('tr', 'TRANSPORT')], max_length=200, null=True),
        ),
    ]
