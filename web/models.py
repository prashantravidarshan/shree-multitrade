from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(default="", null=True)


class Contact(models.Model):
    info_email = models.CharField(max_length=200)
    fb_link = models.CharField(max_length=200)
    tw_link = models.CharField(max_length=200)
    in_link = models.CharField(max_length=200)
    insta_link = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.address


class AboutUs(models.Model):
    about_card_icon = models.ImageField()
    about_details_heading = models.CharField(max_length=200)
    about_details_description = models.CharField(max_length=200)
    about_card_link = models.CharField(max_length=200)

    def __str__(self):
        return self.about_details_heading


class WhoWeAre(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    button_lebel = models.CharField(max_length=20)
    button_link = models.CharField(max_length=200)
    video_link = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class WhoWeAreCard(models.Model):
    icon = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    button = models.CharField(max_length=200)

    def __str__(self):
        return self.heading


class KhajanaClubPlan(models.Model):
    pink_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class KhajanaClubPlanCard(models.Model):
    card_title = models.CharField(max_length=200)
    card_icon = models.CharField(max_length=200)
    card_heading = models.CharField(max_length=200)
    card_description = models.TextField()
    card_link = models.CharField(max_length=200)

    def __str__(self):
        return self.card_heading


class TopInvestor(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class TopInvestorCard(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=200)
    tw_link = models.CharField(max_length=200)
    insta_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Partners(models.Model):
    name = models.CharField(max_length=200, default="")
    image = models.ImageField()

    def __str__(self):
        return self.name
