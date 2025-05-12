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

def send_email_admin_pending_race(client_name, date_booking, hour_booking, from_route, to_route, vehicle_class, notes):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails='nevesjrexecutive@gmail.com',
        subject='New Travel Request Received',
        html_content=f"""
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