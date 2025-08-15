import logging
from django.http import JsonResponse
from django.conf import settings

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_email_reset_password(lang, email, user_name, code):
    reset_link = f'https://nevesjr.vercel.app/{lang}/auth/ValidateCode?code={code}&email={email}'

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY 

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    subject = "Password Reset Request"
    html_content = f"""
        <p>Hello {user_name},</p>
        <p>We have identified that you have requested to change your password to access the NevesJR platform. To change your password, please click on the link below.</p>
        <p><a href="{reset_link}" target="_blank">Reset Password</a></p>
        <p>For security reasons, this link will only be valid for 10 minutes.</p>
        <p>Sincerely,<br>NevesJR Team</p>
    """

    sender = {"name": "NevesJR Team", "email": settings.DEFAULT_FROM_EMAIL} 
    to = [{"email": email, "name": user_name}]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return JsonResponse({
            'status': 'success',
            'message': 'Email sent successfully',
            'response': str(api_response)
        })
    except ApiException as e:
        logging.error("Exception when sending email via Brevo: %s\n" % e)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
