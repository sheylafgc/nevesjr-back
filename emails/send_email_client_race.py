import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sendgrid.helpers.mail import *

from sendgrid import SendGridAPIClient

from django.conf import settings

from datetime import datetime


def format_date_time(date, hour):
    if date and hour:
        combined = datetime.combine(date.date(), hour)
        return combined.strftime('%B %d, %Y at %I:%M %p')
    return 'Date and time not provided'

def send_email_admin_approved_race(email, client_name, date_booking, hour_booking, from_route, to_route, vehicle_class, notes, payment_instructions):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=email,
        subject='Your Trip Confirmed - NevesJR',
        html_content=f"""
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