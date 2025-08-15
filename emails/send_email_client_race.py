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

def send_email_admin_approved_race(email, client_name, date_booking, hour_booking, from_route, to_route, vehicle_class, notes, payment_instructions):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    html_content = f"""
        <p>Hello, {client_name}!</p>

        <p>We are pleased to inform you that your booking with NevesJR has been successfully confirmed!</p>

        <p><strong>Check out the details of your trip below:</strong><br>
        📍 Origin: {from_route}<br>
        📍 Destination: {to_route}<br>
        📅 Date and time: {format_date_time(date_booking, hour_booking)}<br>
        🚗 Vehicle booked: {vehicle_class}<br>
        📝 Notes: {notes}</p>

        <p>To ensure you receive excellent service, we ask that you complete the payment according to the instructions below:</p>
        <p>💳 {payment_instructions}</p>

        <p>If you have any questions, our team is available to help.</p>

        <p>Thank you for choosing NevesJR!</p>

        <p>Sincerely,<br>NevesJR Team</p>
    """

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"email": settings.DEFAULT_FROM_EMAIL, "name": "Neves Jr."},
        to=[{"email": email, "name": client_name}],
        subject="Your Trip Confirmed - NevesJR",
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
