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

def send_email_admin_pending_race(client_name, date_booking, hour_booking, from_route, to_route, vehicle_class, notes):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    html_content = f"""
        <p>Hello, NevesJR team!</p>

        <p>A new travel request has been made through the website and is awaiting approval. </p>

        <p><strong>Check out the booking details:</strong><br>
        👤 Client: {client_name}<br>
        📅 Date and time: {format_date_time(date_booking, hour_booking)}<br>
        📍 Origin: {from_route}<br>
        📍 Destination: {to_route}<br>
        🚗 Vehicle category: {vehicle_class}<br>
        📝 Notes: {notes}<br>

        <p>The booking will only be effective after manual confirmation and sending of payment instructions to the customer. </p>

        <p>Go to the admin panel to approve or edit this booking.</p>

        <p>Thanks,<br>NevesJR System</p>
    """

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"email": settings.DEFAULT_FROM_EMAIL, "name": "Neves Jr."},
        to=[{"email": "nevesjrexecutive@gmail.com", "name": "NevesJR Team"}],
        subject="New Travel Request Received",
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
        logging.error("Erro ao enviar e-mail via Brevo: %s", e)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
