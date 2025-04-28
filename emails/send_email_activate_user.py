import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sendgrid.helpers.mail import *

from sendgrid import SendGridAPIClient

from django.conf import settings

from datetime import datetime

def send_email_activate_user(lang, email, first_name):
    activation_link = f'https://nevesjr.vercel.app/{lang}/activate-account?email={email}'

    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=email,
        subject='Activate your Neves Jr. account',
        html_content=f"""
        <p>Hello, {first_name}!</p>

        <p>Welcome to <strong>Neves Jr.</strong>! Your account has been successfully created.</p>

        <p>To complete your registration, please activate your account by clicking on the button below:</p>

        <p><a href="{activation_link}" target="_blank">Activate account</a></p>

        <p style="color: #999;">If you have not requested this registration, simply ignore this message.</p>

        <p>Welcome,<br>Neves Jr. team</p>
        """
    )

    try:
        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)

        return JsonResponse({
            'status': 'success',
            'message': 'Email sent successfully',
            'status_code': response.status_code
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)