# Generated by Django 3.2.8 on 2021-10-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_details_heading', models.CharField(max_length=200)),
                ('about_details_description', models.CharField(max_length=200)),
                ('about_card_icon', models.CharField(max_length=200)),
                ('about_card_heading', models.CharField(max_length=200)),
                ('about_card_description', models.CharField(max_length=200)),
                ('about_card_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_email', models.CharField(max_length=200)),
                ('fb_link', models.CharField(max_length=200)),
                ('tw_link', models.CharField(max_length=200)),
                ('in_link', models.CharField(max_length=200)),
                ('insta_link', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='KhajanaClubPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pink_title', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='KhajanaClubPlanCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=200)),
                ('card_icon', models.CharField(max_length=200)),
                ('card_heading', models.CharField(max_length=200)),
                ('card_description', models.TextField()),
                ('card_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TopInvestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TopInvestorCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=200)),
                ('tw_link', models.CharField(max_length=200)),
                ('insta_link', models.CharField(max_length=200)),
            ],
        ),
    ]
