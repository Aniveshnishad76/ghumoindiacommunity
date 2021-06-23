

from django.db import models

# Create your models here.
from django.db.models import Model


class Registered_users(Model):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    number = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    father_name=models.CharField(max_length=400,blank=True)
    address=models.CharField(max_length=400,blank=True)
    zip_code=models.CharField(max_length=400,blank=True)
    country=models.CharField(max_length=300,blank=True)
    city=models.CharField(max_length=300,blank=True)
    state=models.CharField(max_length=400,blank=True)
    profile=models.ImageField(upload_to="media/profile/",blank=True)
    def __str__(self):
        return self.email


class Add_blog(Model):
    date=models.DateField(auto_now_add=True)
    Visited_place=models.CharField(max_length=500,blank=True)
    categories=models.CharField(max_length=300,blank=True)
    bloger_name=models.CharField(max_length=400,blank=True)
    blog_title=models.CharField(max_length=900,blank=True)
    blog_link=models.URLField(max_length=900,blank=True)
    image_blog=models.ImageField(upload_to="media/blog_images",blank=True)
    def __str__(self):
        return self.bloger_name

class Add_gallery(Model):
    image=models.ImageField(upload_to='media/gallery/',blank=True)


class review(Model):
    username=models.CharField(max_length=300,blank=True)
    email=models.CharField(max_length=300,blank=True)
    comment=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.username

class Messagess(Model):
    fname=models.CharField(max_length=300,blank=True)
    lname = models.CharField(max_length=300, blank=True)
    email=models.CharField(max_length=300,blank=True)
    phone = models.CharField(max_length=300, blank=True)
    message=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.fname

class Otp(Model):
    email=models.EmailField(max_length=200,blank=True)
    number=models.CharField(max_length=200,blank=True)
    otp=models.CharField(max_length=5,blank=True)
    status = models.CharField(default="Valid", max_length=20)
    def __str__(self):
        return self.email

class Add_Tour(Model):

    tour_name=models.CharField(max_length=500,blank=True,null=True)
    number_of_visited_places=models.CharField(max_length=300,blank=True,null=True)
    tour_location=models.CharField(max_length=300,blank=True,null=True)
    tour_tittle=models.CharField(max_length=900,blank=True,null=True)
    day_choose=(
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')
    )
    night_choose = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10')
    )
    day=models.CharField(max_length=100,choices=day_choose)
    night=models.CharField(max_length=100,choices=night_choose)
    charges=models.CharField(max_length=200,blank=True)
    highlight = models.CharField(max_length=2000, blank=True)
    max_people = models.CharField(max_length=300, blank=True)
    start_date = models.DateField(default='dd/mm/yy')
    last_date = models.DateField(default='dd/mm/yy')
    pickup_address = models.CharField(max_length=400, blank=True)
    retuen_location = models.CharField(max_length=400,blank=True)
    bedroom = models.CharField(max_length=400, blank=True)
    depature_time = models.TimeField(default='hh:mm:ss')
    what_to_expect = models.CharField(max_length=1000, blank=True, null=True)
    day1_rout = models.CharField(max_length=1000, blank=True, null=True)
    day1_visited_place = models.CharField(max_length=1000, blank=True, null=True)
    day2_rout = models.CharField(max_length=1000, blank=True, null=True)
    day2_visited_place = models.CharField(max_length=1000, blank=True, null=True)
    day3_rout = models.CharField(max_length=1000, blank=True)
    day3_visited_place = models.CharField(max_length=1000, blank=True, null=True)
    day4_rout = models.CharField(max_length=1000, blank=True)
    day4_visited_place = models.CharField(max_length=1000, blank=True)
    map_link = models.CharField(blank=True,max_length=1000, null=True)
    image1 = models.ImageField(upload_to="media/tour_images/", null=True)
    image2 = models.ImageField(upload_to="media/tour_images/", null=True)
    image3 = models.ImageField(upload_to="media/tour_images/", null=True)
    image4 = models.ImageField(upload_to="media/tour_images/", null=True)
    image5 = models.ImageField(upload_to="media/tour_images/", null=True)
    image6 = models.ImageField(upload_to="media/tour_images/", null=True)
    status = models.CharField(default="destination",null=True, max_length=200)
    def __str__(self):
        return self.tour_name

class txn_details(Model):

    tour_ID=models.CharField(max_length=400,null=True)
    tour=models.ForeignKey(Add_Tour,on_delete=models.CASCADE, default="")
    email=models.CharField(max_length=200,blank=True,null=True)
    txnid=models.CharField(max_length=100,null=True)
    order_id=models.CharField(max_length=200,blank=True,null=True)
    amount=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    zip_code=models.CharField(max_length=200,blank=True,null=True)
    number=models.CharField(max_length=200,blank=True,null=True)
    country=models.CharField(max_length=200,blank=True,null=True)
    city=models.CharField(max_length=200,blank=True,null=True)
    state=models.CharField(max_length=200,blank=True,null=True)
    txndate=models.CharField(max_length=200,null=True)
    status=models.CharField(default="pendding",max_length=200)
    def __str__(self):
        return self.username

