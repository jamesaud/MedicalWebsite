from django.test import TestCase
from test_plus.test import TestCase
from django.core.urlresolvers import reverse
from medweb.homepage.views import *
from medweb.homepage.models import *
from django.test import Client

# AssertGoodView tests for 200 response, database calls under 50, etc.
# Read test_plus documentation for more details

class BaseHomepageTestCase(TestCase):

    def setUp(self):
        self.client = Client()


class TestCreate(BaseHomepageTestCase):

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertGoodView(index)


    def test_create_view(self):
        url = reverse('create')
        person_post = {'first_name':'test', 'last_name': 'test', 'email':'test@test.com', 'position':'test'}
        evaluation_post = {'message':'hello', 'ehr_likes': 'test'}

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
        self.assertEqual(e.person, ep.person)

        self.assertGoodView(create)





