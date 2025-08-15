from django.conf import settings
from django.http import JsonResponse
import logging

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

logger = logging.getLogger(__name__)


def send_email_template(model_class, email):
    try:
        email_template = model_class.objects.first()
        if not email_template:
            return {"status": "error", "message": "Nenhum template de e-mail encontrado."}

        subject = email_template.subject
        message = email_template.message

        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = settings.BREVO_API_KEY

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": email}],
            sender={"email": settings.DEFAULT_FROM_EMAIL},
            subject=subject,
            html_content=message
        )

        response = api_instance.send_transac_email(send_smtp_email)

        logger.info(f"E-mail enviado com sucesso! ID: {response.message_id}")

        return {
            "status": "success",
            "message": "E-mail enviado com sucesso",
            "message_id": response.message_id
        }

    except ApiException as e:
        logger.error(f"Erro da API Brevo: {e}")
        return {
            "status": "error",
            "message": str(e),
            "status_code": e.status if hasattr(e, "status") else 500
        }

    except Exception as e:
        logger.error(f"Erro inesperado ao enviar e-mail: {e}")
        return {
            "status": "error",
            "message": str(e),
            "status_code": 500
        }
