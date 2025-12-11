from django.shortcuts import render
from core import models as core_models 

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Portfolios
def index(request):
    # Get all published posts
    posts_list = core_models.Portfolio.objects.filter(status="Published").order_by('-date')  # Added ordering
    
    # Create paginator - 6 items per page (good for grid layouts)
    paginator = Paginator(posts_list, 5)
    
    # Get page number from request
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        posts = paginator.page(paginator.num_pages)
    
    context = {
        "posts": posts,
        "page_obj": posts,  # For compatibility with Django's pagination templates
    }
    return render(request, "core/index.html", context)

# Portfolio Detail
def portfolio_detail(request, pid):
    post = core_models.Portfolio.objects.get(pid=pid, status="Published")
  
    context = {"post": post}
    return render(request, "core/portfolio_detail.html", context)

# Services 
def service(request):
    context = {}
    return render(request, "core/service.html", context)



# Other Pages 
def contact(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        core_models.Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        # ---- SEND EMAIL ----
        full_message = f"""
            New Contact Message

            Name: {name}
            Email: {email}
            Phone: {phone}

            Subject: {subject}

            Message:
            {message}
        """

        send_mail(
            subject=f"New Contact Message: {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,  # your sending email
            recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Email that receives messages
            fail_silently=False,
        )

        messages.success(request, "Message Sent Successfully")

    return render(request, "core/contact.html", )