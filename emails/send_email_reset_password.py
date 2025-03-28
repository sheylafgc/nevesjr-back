import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sendgrid.helpers.mail import *

from sendgrid import SendGridAPIClient

from django.conf import settings


@csrf_exempt
def send_email_reset_password(email, user_name, code):
    reset_link = f"https://nevesjr.vercel.app/auth/ValidateCode?code={code}&email={email}"

    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=email,
        subject='Password Reset Request',
        html_content=f"""
        <p>Hello {user_name},</p>
        <p>We have identified that you have requested to change your password to access the NevesJR platform. To change your password, please click on the link below.</p>
        <p><a href="{reset_link}" target="_blank">Reset Password</a></p>
        <p>For security reasons, this link will only be valid for 10 minutes..</p>
        <p>Sincerely,<br>NevesJR Team</p>
        """
    )

    try:
        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)

        return JsonResponse({
            "status": "success",
            "message": "Email sent successfully",
            "status_code": response.status_code
        })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)