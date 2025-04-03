from django.conf import settings
from django.http import JsonResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import logging

logger = logging.getLogger(__name__)


def send_email_template(model_class, email):
    try:
        email_template = model_class.objects.first()
        if not email_template:
            return {"status": "error", "message": "Nenhum template de e-mail encontrado."}

        subject = email_template.subject
        message = email_template.message
        
        mail = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=email,
            subject=subject,
            html_content=message
        )

        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(mail)

        logger.info(f"E-mail enviado com status {response.status_code}")

        return {
            "status": "success",
            "message": "E-mail enviado com sucesso",
            "status_code": response.status_code
        }

    except Exception as e:
        logger.error(f"Erro ao enviar e-mail: {e}")
        return {
            "status": "error",
            "message": str(e),
            "status_code": 500
        }