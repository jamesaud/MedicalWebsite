import random
import json
from django.test import TestCase # Comment out the next line for autocomplete in pycharm
from test_plus.test import TestCase
from django.core.urlresolvers import reverse
from medweb.homepage.views import *
from medweb.homepage.models import *
from medweb.homepage.models import REFERRAL_CHOICES
from django.test import Client

# AssertGoodView tests for 200 response, database calls under 50, etc.
# Read test_plus documentation for more details

class BaseHomepageTestCase(TestCase):

    def setUp(self):
        self.client = Client()


class TestViews(BaseHomepageTestCase):

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertGoodView(index)


    def test_create_view(self):
        choices = tuple([tupl[0] for tupl in REFERRAL_CHOICES])
        url = reverse('create')
        person_post = {'first_name':'test', 'last_name': 'test', 'email':'test@test.com', 'position':'test'}
        evaluation_post = {
            'message': 'hello',
            'ehr_likes': 'test',
            'referral': choices,
        }

        # Test Get Request as error
        response = self.client.get(url)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'error'}
        )

        #Test Post response for Person

        response = self.client.post(url, person_post)
        p = Person.objects.get(first_name=person_post['first_name'])
        self.assertEqual(p.first_name, person_post['first_name'])
        self.assertEqual(p.last_name, person_post['last_name'])
        self.assertEqual(p.email, person_post['email'])
        self.assertEqual(p.position, person_post['position'])

        #Test Post response for Evaluation
        response = self.client.post(url, evaluation_post)
        e = Evaluation.objects.get(message = evaluation_post['message'])
        ep = Evaluation.objects.get(person = p)
        self.assertEqual(e.message, evaluation_post['message'])
        self.assertEqual(', '.join(choices), e.referral)
        self.assertEqual(e.person, ep.person)

        self.assertGoodView(create)


    def test_submit_newsletter_view(self):
        test_email = 'mytest@gmail.com'
        url = reverse('submit_newsletter')
        newsletter_post = {'email': test_email, 'newsletter': 'yes'}

        # Test Get Request
        json_response = self.client.get(url).json()
        self.assertEqual(json_response.get('status'), 'error')

        # Test Post response for submitting an email
        json_response = self.client.post(url, newsletter_post).json()
        self.assertEqual(json_response.get("status"), 'success')

        email_created_or_exists = False
        if json_response.get('newsletter_response').get('list_id') or (json_response.get('newsletter_response').get('status') == 400):
            email_created_or_exists = True

        self.assertTrue(email_created_or_exists)
        self.assertGoodView(submit_newsletter)


    def test_submit_referral(self):
        url = reverse('submit_referral')
        choices = tuple([tupl[0] for tupl in REFERRAL_CHOICES])
        post_data = {'referral': choices}

        #Test Get
        json_response = self.client.get(url).json()
        self.assertEqual(json_response.get('status'), 'error')

        #Test Post
        json_response = self.client.post(url, post_data).json()
        self.assertEqual(json_response.get('status'), 'success') # Should succeed in creating a RandomReferral

        json_response = self.client.post(url, post_data).json()
        self.assertEqual(json_response.get('status'), 'error')  # Should fail the second time from cookie checking.

        # Test Object creation
        self.assertEqual(len(RandomReferral.objects.all()), 1) # Should have created only one referral object.
