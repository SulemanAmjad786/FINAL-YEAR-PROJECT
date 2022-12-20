from django.shortcuts import render, redirect
from .models import About
from .models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def homes(request):
    return render(request, 'pages/home.html')


@login_required(login_url='login')
def aboutus(request):
    about = About.objects.all()
    data = {
        'about': about,
    }
    return render(request, 'pages/about.html', data)


@login_required(login_url='login')
def bitcoin(request):
    return render(request, 'pages/bitcoin.html')


@login_required(login_url='login')
def watchlist(request):
    return render(request, 'pages/bitcoinwatchlist.html')


@login_required(login_url='login')
def faqask(request):
    return render(request, 'pages/faq.html')


@login_required(login_url='login')
def prediction(request):
    return render(request, 'pages/bitcoinprediction.html')


@login_required(login_url='login')
def stockmarket(request):
    return render(request, 'pages/stock.html')


@login_required(login_url='login')
def stocknews(request):
    return render(request, 'pages/stockwatchlist.html')


@login_required(login_url='login')
def stockprediction(request):
    return render(request, 'pages/stockprediction.html')


@login_required(login_url='login')
def blog(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 3)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)

    data = {
        'blog': paged_blog,
    }
    return render(request, 'pages/blog.html', data)


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        text = request.POST['text']
        message = request.POST['message']

        email_subject = 'You have a new message request' + text
        message_body = 'Name:' + firstname + 'Email:' + \
            email + 'Subject:' + text + 'Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'mirdilawar895@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Thanks for submitting Mail')
        return redirect('contact')

    return render(request, 'pages/contact.html')
