import logging
from django.http import JsonResponse
from django.conf import settings

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_email_activate_user(lang, email, first_name):
    activation_link = f'https://nevesjr.vercel.app/{lang}/activate-account?email={email}'

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"email": settings.DEFAULT_FROM_EMAIL, "name": "Neves Jr."},
        to=[{"email": email, "name": first_name}],
        subject="Activate your Neves Jr. account",
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
        api_response = api_instance.send_transac_email(send_smtp_email)
        return JsonResponse({
            'status': 'success',
            'message': 'Email sent successfully',
            'data': api_response.to_dict()
        })
    except ApiException as e:
        logging.error(f"Erro ao enviar e-mail via Brevo: {e}")
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
