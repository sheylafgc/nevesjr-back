import logging
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def format_date_time(date, hour):
    if date and hour:
        combined = datetime.combine(date.date(), hour)
        return combined.strftime('%B %d, %Y at %I:%M %p')
    return 'Date and time not provided'

def send_email_admin_cancel_race(email, client_name, date_booking, hour_booking, from_route, to_route, vehicle_class):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    html_content = f"""
        <p>Hello, {client_name}!</p>

        <p>We inform you that Team NevesJR has canceled the trip that was scheduled. </p>

        <p><strong>Check the details of the canceled reservation:</strong><br>
        📅 Date and time: {format_date_time(date_booking, hour_booking)}<br>
        📍 Origin: {from_route}<br>
        📍 Destination: {to_route}<br>
        🚗 Vehicle category: {vehicle_class}<br>

        <p>If there has already been an advance payment or payment, please check the internal procedures for refund or rescheduling, if necessary. </p>

        <p>Sincerely,<br>NevesJR System</p>
    """

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"email": settings.DEFAULT_FROM_EMAIL, "name": "Neves Jr."},
        to=[
            {"email": "nevesjrexecutive@gmail.com", "name": "NevesJR Team"},
            {"email": email, "name": client_name}
        ],
        subject="Trip Canceled by Team NevesJR",
        html_content=html_content
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return JsonResponse({
            "status": "success",
            "message": "Email sent successfully",
            "response": str(api_response)
        })
    except ApiException as e:
        logging.error("Erro ao enviar e-mail via Brevo: %s", e)
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

def send_email_user_cancel_race(email, client_name, date_booking, hour_booking, from_route, to_route, vehicle_class):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    html_content = f"""
        <p>Hello!</p>

        <p>We inform you that customer {client_name} has canceled the trip that was scheduled.</p>

        <p><strong>Check the details of the canceled reservation:</strong><br>
        📅 Date and time: {format_date_time(date_booking, hour_booking)}<br>
        📍 Origin: {from_route}<br>
        📍 Destination: {to_route}<br>
        🚗 Vehicle category: {vehicle_class}<br>

        <p>If there has already been an advance payment or payment, please check the internal procedures for refund or rescheduling, if necessary.</p>

        <p>Sincerely,<br>NevesJR System</p>
    """

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"email": settings.DEFAULT_FROM_EMAIL, "name": "Neves Jr."},
        to=[
            {"email": "nevesjrexecutive@gmail.com", "name": "NevesJR Team"},
            {"email": email, "name": client_name}
        ],
        subject=f"Trip Canceled by Customer – {client_name}",
        html_content=html_content
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return JsonResponse({
            "status": "success",
            "message": "Email sent successfully",
            "response": str(api_response)
        })
    except ApiException as e:
        logging.error("Erro ao enviar e-mail via Brevo: %s", e)
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
