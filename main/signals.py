from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Blog, Subscriber
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Blog)
def send_new_blog_email(sender, instance, created, **kwargs):
    if created:
        subject = f"New Blog Post: {instance.title}"
        from_email = settings.DEFAULT_FROM_EMAIL
        blog_url = f"https://blog-test-mauve-psi.vercel.app/pages/Blog/{instance.slug}"
        subscribers = Subscriber.objects.all()
        emails = [subscriber.email for subscriber in subscribers]

        for email in emails:
            html_content = render_to_string('main/email.html', {'blog': instance, 'blog_url': blog_url})
            plain_content = strip_tags(html_content)
            
            # Create the email
            email_message = EmailMultiAlternatives(
                subject=subject,
                body=plain_content,
                from_email=from_email,
                to=[email],
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()  # Send each email individually with HTML content

@receiver(post_save, sender=Subscriber)
def welcome_mail(sender, instance, created, **kwargs):
    if created:
        print("hello, world!")
        subject = "Welcome to Lumen Blog"
        from_email = settings.DEFAULT_FROM_EMAIL
        email = instance.email

        html_content = render_to_string('main/welcome.html')
        plain_content = strip_tags(html_content)
        
        # Create the email
        email_message = EmailMultiAlternatives(
            subject=subject,
            body=plain_content,
            from_email=from_email,
            to = [email]
        )
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()  
            

    