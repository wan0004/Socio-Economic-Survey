# Generated by Django 3.0.6 on 2020-05-11 09:39

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0003_auto_20200510_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='DifferentlyAblePerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(blank=True, max_length=200, verbose_name='Type')),
                ('scemes', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Haji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scemes', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Orphan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scemes', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.Person')),
            ],
        ),
        migrations.CreateModel(
            name='OldAgedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scemes', models.CharField(blank=True, max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.IntegerField(unique=True, verbose_name='House No')),
                ('head_of_family', models.CharField(max_length=100)),
                ('homested_area', models.CharField(max_length=20)),
                ('type_of_house', models.CharField(choices=[('Pucca', 'Pucca'), ('Semi Pucca', 'Semi Pucca'), ('Kutcha', 'Kutcha')], max_length=100)),
                ('ownership', models.CharField(choices=[('Owned', 'Owned'), ('Rented', 'Rented')], max_length=100)),
                ('no_of_rooms', models.IntegerField()),
                ('fuel_for_cooking', multiselectfield.db.fields.MultiSelectField(choices=[('Firewood', 'Firewood'), ('LPG', 'LPG'), ('Electricity', 'Electricity'), ('Kerosene', 'Kerosene'), ('All', 'All')], max_length=37)),
                ('access_to_electricity', models.BooleanField(default=False)),
                ('water_source', models.CharField(choices=[('Pipe', 'Pipe'), ('River', 'River'), ('Handpump', 'Handpump'), ('Common Pond', 'Common Pond'), ('Own Pond', 'Own Pond'), ('Others', 'Others')], max_length=100)),
                ('water_availability', models.CharField(choices=[('Less than 1km', 'Less than 1km'), ('More than 1km', 'More than 1km')], max_length=100)),
                ('toilet_facility', models.CharField(choices=[('Open', 'Open'), ('Outlet', 'Outlet'), ('Others', 'Others')], max_length=100)),
                ('bath_facility', models.BooleanField(default=False)),
                ('sewage_disposal_facility', models.BooleanField(default=False)),
                ('no_of_years_stayed_here', models.IntegerField()),
                ('ever_lived_in_another_place', models.BooleanField(default=False)),
                ('family_type', models.CharField(choices=[('Joint Family', 'Joint Family'), ('Nuclear Family', 'Nuclear Family'), ('Extended Family', 'Extended Family')], max_length=100)),
                ('orphan_children_available', models.BooleanField(default=False, verbose_name='Is there any orphan children in your household? If yes, specify how many?')),
                ('differently_able_person_available', models.BooleanField(default=False, verbose_name='Are there any differently able persons in the household?')),
                ('old_aged_person_available', models.BooleanField(default=False, verbose_name='Is there any old aged person in your household? If yes, specify below?')),
                ('haji_available', models.BooleanField(default=False, verbose_name='Is there any Haji in the household?')),
                ('priority_household', models.CharField(choices=[('bpl', 'BPL'), ('apl', 'APL'), ('aay', 'AAY')], max_length=10)),
                ('nation_food_security_act', models.BooleanField(verbose_name='Covered by National Food Security Act (NFSA)?')),
                ('housing_scemes', models.BooleanField(verbose_name='Housing Scheme? If yes, specify below.')),
                ('specify_housing_scemes', models.CharField(blank=True, max_length=300)),
                ('old_aged_pension_scheme', models.BooleanField(verbose_name='Old aged pension scheme, If yes, specify below.')),
                ('specify_old_aged_pension_scheme', models.CharField(blank=True, max_length=300)),
                ('other_schemes', models.BooleanField(verbose_name='If other scheme, specify below.')),
                ('specify_other_schemes', models.CharField(blank=True, max_length=300)),
                ('differently_able_person_available_names', models.ManyToManyField(blank=True, related_name='differently_able_person', to='act.DifferentlyAblePerson')),
                ('haji_name', models.ManyToManyField(blank=True, max_length=300, related_name='haji_person_names', to='act.Haji', verbose_name='Haji Names')),
                ('members', models.ManyToManyField(related_name='family_members', to='act.Person')),
                ('old_aged_person_names', models.ManyToManyField(blank=True, max_length=300, related_name='old_person_names', to='act.OldAgedPerson', verbose_name='Old Aged Names')),
                ('orphan_children_names', models.ManyToManyField(blank=True, max_length=300, related_name='orphan_person_names', to='act.Orphan', verbose_name='Orphan Names')),
            ],
        ),
    ]
