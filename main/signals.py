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
        blog_url = f"https://ifepolitikal.vercel.app/pages/Blog/{instance.slug}"
        subscribers = Subscriber.objects.all()

        for subscriber in subscribers:
            # Generate unsubscribe URL for each subscriber
            unsubscribe_url = f"localhost:8000/unsubscribe/{subscriber.unsubscribe_token}/"  # Adjust with your URL pattern

            # Render HTML content with unsubscribe link and blog details
            html_content = render_to_string('main/email.html', {
                'blog': instance,
                'blog_url': blog_url,
                'subscriber': subscriber,
                'unsubscribe': unsubscribe_url,
            })
            plain_content = strip_tags(html_content)

            # Create and send the email
            email_message = EmailMultiAlternatives(
                subject=subject,
                body=plain_content,
                from_email=from_email,
                to=[subscriber.email],  # Send to individual subscriber's email
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()


@receiver(post_save, sender=Subscriber)
def welcome_mail(sender, instance, created, **kwargs):
    if created:
        # print("hello, world!")
        subject = "Welcome to Lumen Blog"
        from_email = settings.DEFAULT_FROM_EMAIL
        email = instance.email
        # base_url = request.build_absolute_uri('/')
        unsubscribe_url = f"localhost:8000/unsubscribe/{instance.unsubscribe_token}"

        html_content = render_to_string('main/welcome.html', {'unsubscribe': unsubscribe_url})
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
            

    