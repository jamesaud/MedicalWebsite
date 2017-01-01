# Mailchimp imports
from utilities.mailchimp_wrapper.chimp import Client
from config.settings.common import MAILCHIMP_API_KEY, MAILCHIMP_LIST_NEWSLETTER_ID, \
                                   MAILCHIMP_USERNAME, MAILCHIMP_DATA_CENTER

from medweb.homepage.forms import PersonForm, EvaluationForm, EmailForm
import logging # import the logging library
logger = logging.getLogger(__name__) # Get an instance of a logger

"""
These functions help process forms in views.
"""
c = Client(MAILCHIMP_API_KEY, MAILCHIMP_USERNAME, MAILCHIMP_DATA_CENTER)


def handle_email_form(request, mailchimp_form_id):
    """
    Submits an email_form to mailchimp using post data.
    :return: (EmailForm, Dict, Dict), the cleaned form and responses for both mailchimp lists.
    """
    email_form = EmailForm(request.POST)
    report_response = newsletter_response = None

    if email_form.is_valid():
        email = email_form.cleaned_data.get('email')
        report_response = c.subscribe_user(mailchimp_form_id, email)

        if request.POST.get('newsletter'):
            newsletter_response = c.subscribe_user(MAILCHIMP_LIST_NEWSLETTER_ID, email)

        logger.debug('Subscribed :{0}\nReport Response: {1}\nNewsletter Response: {2}\n\n' \
                     .format(email, report_response, newsletter_response))

    return (email_form, report_response, newsletter_response)



