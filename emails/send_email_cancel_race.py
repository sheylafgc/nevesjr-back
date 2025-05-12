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

def send_email_admin_cancel_race(email, client_name, date_booking, hour_booking, from_route, to_route, vehicle_class):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=['nevesjrexecutive@gmail.com', email],
        subject='Trip Canceled by Team NevesJR',
        html_content=f"""
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
    
def send_email_user_cancel_race(email, client_name, date_booking, hour_booking, from_route, to_route, vehicle_class):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
         to_emails=['nevesjrexecutive@gmail.com', email],
        subject=f'Trip Canceled by Customer – {client_name}',
        html_content=f"""
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