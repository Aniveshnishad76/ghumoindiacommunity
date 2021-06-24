import random


from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from paytm import Checksum
from travel.models import Registered_users, Add_blog, Add_gallery, Add_Tour, review, Messagess, Otp, txn_details


def Index_pages(request):
    return render(request,"index.html")
def home_pages(request):
    return render(request,"index.html")
def home_pages_user(request ):
    try:
        if request.session['email'] is not None:
            x=Add_Tour.objects.filter(status="home")
            return render(request,"user_pages/user_home.html",{'x':x})
    except:
        return render(request,"index.html")


def About_pages(request):
    return render(request,"about.html")
def About_pages_user(request):
    try:
        if request.session['email'] is not None:
            return render(request,"user_pages/about.html")
    except:
        return render(request, "index.html")
def Gallery_pages(request):
    return render(request,"gallery.html")
def Gallery_pages_user(request):
    try:
        if request.session['email'] is not None:
            x=Add_gallery.objects.all()
        return render(request,"user_pages/gallery.html",{"data":x})
    except:
        return render(request, "index.html")
def destination_single_full(request,id):
    try:
        if request.session['email'] is not None:
            email=request.session['email']
        y=Registered_users.objects.get(email=email)
        x=Add_Tour.objects.get(id=id)
        return render(request, "user_pages/destination-single-full.html",{"data":x,"y":y})
    except:
        return render(request, "index.html")
def faq_pages(request):
    return render(request,"faq.html")
def faq_pages_user(request):
    try:
        if request.session['email'] is not None:
            return render(request,"user_pages/faq.html")
    except:
        return render(request, "index.html")
def testimonial_pages(request):
    return render(request,"testimonial.html")
def testimonial_pages_user(request):
    try:
        if request.session['email'] is not None:
            return render(request,"user_pages/testimonial.html")
    except:
        return render(request, "index.html")
def destination_pages(request):
    return render(request,"destination-full.html")
def destination_pages_user(request):
    try:
        if request.session['email'] is not None:
            x=Add_Tour.objects.all().order_by('-id')
            paginator = Paginator(x, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request,"user_pages/destination-full.html",{'data':page_obj})
    except:
        return render(request, "index.html")
def blog_pages(request):
    return render(request,"blog-full.html")
def blog_pages_user(request):
    try:
        if request.session['email'] is not None:
            x=Add_blog.objects.all().order_by('id')
            paginator= Paginator(x,4)
            page_number= request.GET.get('page')
            page_obj= paginator.get_page(page_number)
            return render(request,"user_pages/blog-full.html",{"data":page_obj})
    except:
        return render(request, "index.html")
def blog_single_pages(request):
    return render(request,"blog-single-full.html")
def blog_single_pages_user(request):
    try:
        if request.session['email'] is not None:
            return render(request,"user_pages/blog-single-full.html")
    except:
        return render(request, "index.html")

def contact_pages(request):
    return render(request,"contact.html")
def contact_pages_user(request):
    try:
        if request.session['email'] is not None:
            return render(request,"user_pages/contact.html")
    except:
        return render(request, "index.html")
def Login_pages(request):
    return render(request,"login.html")
def user_home(request):
    try:
        if request.session['email'] is not None:
            return render(request,"user_pages/user_home.html")
    except:
        return render(request, "index.html")
def my_profile(request):
    return render(request,"user_pages/my_profile.html")
def Data_register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['password']
        if Registered_users.objects.filter(email=email).exists():
            messages.error(request," This Email is Already Exists ")
            return render(request,"login.html")
        elif Registered_users.objects.filter(number=number).exists():
            messages.error(request," This Number is Already Exists ")
            return render(request,"login.html")
        else:
            email = request.POST['email']
            number = request.POST['number']
            otp=random.randint(10000,99999)
            sent_otp=str(otp)
            y=Otp(email=email,number=number,otp=sent_otp)
            request.session['email'] = email
            request.session['username'] = username
            request.session['password'] = password
            request.session['number'] = number
            ctx = {
                'otp' :sent_otp
            }
            message = get_template('user_pages/email_tamplate1.html').render(ctx)
            msg = EmailMessage(
                'GhumoIndiaCommunity',
                message,
                'Ghumo_India_Community',
                [email],

            )
            msg.content_subtype = "html"
            msg.send()
            y.save()

            messages.success(request,"Otp sent Successfully")
            return render(request,"enter_otp.html",{'email':email})
    else:
        messages.error(request,"Somthing error!")
    return render(request,"login.html")

def Check_otp(request):
    if request.method == "POST":
        email = request.session['email']
        username = request.session['username']
        password = request.session['password']
        number = request.session['number']
        otp = request.POST['otp']
        if Otp.objects.filter(email=email, otp=otp, status="Valid"):
            o = Otp.objects.filter(email=email, status="Valid")
            for c1 in o:
                p = Otp.objects.get(id=c1.id)
                p.status = "complete"
                p.save()
            object=Registered_users(username=username,email=email,password=password,number=number)
            object.save()
            messages.success(request,'You Are Registered Succrssfully, Please Login!')
            return render(request, 'login.html', {"email": email})
        else:
            messages.error(request, 'Invalid OTP')
            return render(request, 'enter_otp.html')
        messages.ERROR(request, "Invalid OTP")
        return render(request, 'enter_otp.html')


def Data_login(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            if Registered_users.objects.get(email=email,password=password)is not None:
                request.session['email']=email
                x=Registered_users.objects.get(email=email)
                name=x.username
                messages.success(request,"login Successfully")
                return render(request,"user_pages/user_home.html",{"name":name,"data":x,"email":email})
        except:
            messages.error(request, "Invalid Email or Password ")
        return render(request, "login.html")
    return render(request, "login.html")

def Review(request):
    try:
        if request.session['email'] is not None:
            if request.method=="POST":
                username=request.POST['username']
                email=request.POST['email']
                comment=request.POST['comment']
                user=review(username=username,email=email,comment=comment)
                user.save()
                messages.success(request, "you are commented successfully!")
                return render(request, "user_pages/destination-full.html")
    except:
        return render(request,"index.html")
def logout(request):
    try:
        request.session.flush()
    except:
        pass
    messages.success(request,'Logout Successfuly')
    return redirect("Data_login")
def My_profile(request):
    try:
        if request.session['email'] is not None:
            email=request.session['email']
            x=Registered_users.objects.get(email=email)
            return render(request,"user_pages/dashboard-my-profile.html",{"data":x})
    except:
        return render(request,"index.html")

def Update_profile(request,id):
    try:
        if request.session['email'] is not None:
            if request.method == "POST":
                up = Registered_users.objects.get(id=id)
                up.username = request.POST['username']
                up.number = request.POST['number']
                up.bio = request.POST['bio']
                up.twitter_link = request.POST['twitter']
                up.facebook_link = request.POST['facebook']
                up.father_name = request.POST['father_name']
                up.address = request.POST['address']
                up.zip_code = request.POST['zip_code']
                up.country = request.POST['country']
                up.city = request.POST['city']
                up.state = request.POST['state']
                up.profile=request.FILES['profile']
                up.save()
                messages.success(request, 'Saved Successfuly')
                return render(request, "user_pages/user_home.html")
            else:
                messages.error(request, 'Profile Not Saved')
                return render(request, "user_pages/dashboard-my-profile.html")
    except:
        return render(request,"index.html")

def Messages(request):
    try:
        if request.session['email'] is not None:
            if request.method=="POST":
                fname=request.POST['fname']
                lname=request.POST['lname']
                email = request.POST['email']
                phone = request.POST['phone']
                message =request.POST['message']
                user=Messagess(fname=fname,lname=lname,email=email,phone=phone,message=message)

                user.save()
                return render(request,"user_pages/user_home.html")
    except:
        return render(request,"index.html")

def search_place(request):
    try:
        if request.session['email'] is not None:
            if request.method=="POST":
                destination=request.POST['destination']
                day=request.POST['day']
                x=Add_Tour.objects.filter(tour_name=destination,day=day)
                y = Add_Tour.objects.all().order_by('-id')


                return render(request,"user_pages/search_destination.html",{"data":x,"dataa":y})
    except:
        return render(request,"index.html")
def Change_password(request):
    try:
        if request.session['email'] is not None:
            email=request.session['email']

            return render(request,"user_pages/change_password.html",{"email":email})
    except:
        return render(request,"index.html")
def Check_password(request):
    if request.method =="POST":
        email=request.POST['email']
        password=request.POST['password']
        if Registered_users.objects.filter(email=email,password=password):
            otp = random.randint(10000, 99999)
            sent_otp =str(otp)
            y = Otp(email=email,otp=sent_otp)
            request.session['email'] = email
            ctx = {
                'otp': sent_otp
            }
            message = get_template('user_pages/email_tamplate1.html').render(ctx)
            msg = EmailMessage(
                'GhumoIndiaCommunity',
                message,
                'Ghumo_India_Community',
                [email],

            )
            msg.content_subtype = "html"
            msg.send()
            y.save()

            messages.success(request, "Please Enter OTP sent to Your Email ")
            return render(request, "user_pages/change_password_otp.html",{"email":email})
        else:
            messages.error(request, "Invalid Password ")
        return render(request, "user_pages/change_password.html",{"email":email})

    return render(request, "user_pages/change_password.html")

def Check_password_otp(request):
    if request.method == "POST":
        email=request.POST['email']
        otp=request.POST['otp']
        if Otp.objects.filter(email=email,otp=otp,status="Valid"):
            o = Otp.objects.filter(email=email,status="Valid")
            for c1 in o:
                p = Otp.objects.get(id=c1.id)
                p.status = "complete"
                p.save()

            messages.success(request, 'Please Enter Your New Password')
            return render(request, 'user_pages/enter_new_password.html', {"email": email})
        else:
            messages.error(request, "Invalid OTPP")
            return render(request, 'user_pages/change_password_otp.html',{"email":email})
        messages.error(request, "Invalid OTP")
        return render(request, 'user_pages/change_password_otp.html')

def Check_new_password(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if Registered_users.objects.filter(email=email,password=password).exists():
            messages.error(request,"YOur New Password is Same as Old password")
            return render(request, "user_pages/enter_new_password.html", {"email": email})
        else:
            x=Registered_users.objects.get(email=email)
            x.password=request.POST['password']
            x.save()
            request.session.flush()
            messages.success(request,"Password Chnage Successfully")
            return render(request,"user_pages/user_home.html")


        messages.error(request, "Somthinf error ! please try after some time.")
        return render(request, "user_pages/enter_new_password.html.html")

def booking_page(request,id):
    try:
        if request.session['email'] is not None:
            email=request.session['email']
        y=Registered_users.objects.get(email=email)
        x=Add_Tour.objects.get(id=id)
        return render(request, "user_pages/booking.html",{"data":x,"y":y})
    except:
        return render(request, "index.html")
def checkout(request):
    email =  request.POST['email']
    amount = request.POST['amount']
    username = request.POST['username']
    number = request.POST['number']
    country = request.POST['country']
    zip_code = request.POST['zip_code']
    city = request.POST['city']
    state= request.POST['state']
    tour_ID = request.POST['tour_ID']
    order_id = random.randint(10000000, 99999999)
    if txn_details.objects.filter(email=email,order_id=order_id).exists():
        messages.error(request,'something error')
        return redirect(booking_page)
    else:
        obj=txn_details(email=email,order_id=order_id,amount=amount,username=username,zip_code=zip_code,number=number,country=country,city=city,state=state,tour_ID=tour_ID)
        request.session['order_id']= order_id
        obj.save()
        param_dict = {
            'MID': 'etmNMZ18152192158003',#merchant id
            'ORDER_ID': str(order_id), #orderid genrated in our backend
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email, #customer email
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',#webstaging is used if we are in test mode
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'https://ghumoindia.herokuapp.com/handlerequest/',
        }
        MERCHANT_KEY='MaM!%BJgyIZRTEpq'
        param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict, MERCHANT_KEY)

        return render(request,"user_pages/paytm.html",{'param_dict':param_dict})

@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i =="CHECKSUMHASH":
            checksum=form[i]
    MERCHANT_KEY = 'MaM!%BJgyIZRTEpq'
    verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print("sucees")
            amount=response_dict['TXNAMOUNT']
            order_id = response_dict['ORDERID']
            data=txn_details.objects.get(order_id=order_id)
            data.txnid=response_dict['TXNID']
            data.txndate = response_dict['TXNDATE']
            data.amount = response_dict['TXNAMOUNT']
            data.status ='success'
            email=data.email
            username=data.username
            txn_id=data.txnid
            tour_name=data.tour.tour_name
            ctx = {
                'username': username,
                'txn_id': txn_id,
                'tour_name': tour_name,
                'order_id':order_id
            }
            message = get_template('user_pages/email_tamplate2.html').render(ctx)
            msg = EmailMessage(
                'GhumoIndiaCommunity',
                message,
                'Ghumo_India_Community',
                [email],

            )
            msg.content_subtype = "html"
            msg.send()
            data.save()


        else:
            print("fail")
            amount = response_dict['TXNAMOUNT']
            order_id = response_dict['ORDERID']
            print(response_dict)
            print(order_id)
            data = txn_details.objects.get(order_id=order_id)
            data.txnid = response_dict['TXNID']
            data.txndate = response_dict['TXNDATE']
            data.amount = response_dict['TXNAMOUNT']
            data.status = 'failed'
            email = data.email
            username = data.username
            tour_name = data.tour.tour_name
            ctx = {
                'username': username,
                'tour_name': tour_name

            }
            message = get_template('user_pages/email_tamplate3.html').render(ctx)
            msg = EmailMessage(
                'GhumoIndiaCommunity',
                message,
                'Ghumo_India_Community',
                [email],

            )
            msg.content_subtype = "html"
            msg.send()
            data.save()
            return render(request, "user_pages/confirmation-faild.html", {'response': response_dict})

    print(response_dict)

    return render(request,"user_pages/confirmation.html",{'response':response_dict})

def confirmation(request):
    try:
        if request.session['email'] is not None:
            email=request.session['email']
            x=txn_details.objects.filter(email=email,status='success')
            return render(request,"user_pages/confirmation.html",{"data":x})
    except:
        return render(request,"index.html")
def confirmation_failed(request):
    email=request.session['email']
    x=txn_details.objects.filter(email=email,status='failed')
    return render(request,"user_pages/confirmation-faild.html",{"data":x})
def dashboard_history(request):
    email=request.session['email']
    x=txn_details.objects.filter(email=email).order_by('-id')
    return render(request,'user_pages/dashboard-history.html',{"data":x})

def booking_detail(request,id):
    email = request.session['email']
    x = txn_details.objects.get(id=id)
    return render(request, 'user_pages/booking_details.html', {"data": x})



