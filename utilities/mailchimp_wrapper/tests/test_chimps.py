import unittest
from ..chimp import Client
import random
from functools import wraps  # Calling wraps inside a decorator keeps the docstring of the original function
from config.settings.common import MAILCHIMP_TEST_API_KEY, MAILCHIMP_TEST_LIST_REPORT_ID, \
    MAILCHIMP_TEST_LIST_NEWSLETTER_ID, MAILCHIMP_TEST_USERNAME, MAILCHIMP_TEST_DATA_CENTER


api_key = MAILCHIMP_TEST_API_KEY
list_id = MAILCHIMP_TEST_LIST_REPORT_ID
username = MAILCHIMP_TEST_USERNAME
data_center = MAILCHIMP_TEST_DATA_CENTER

class ClientTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client(api_key, username, data_center)
        # Random user, ensures mailchimp doesn't lock out user
        cls.email = 'justatest123{}@gmail.com'.format(str(random.randint(0, 1000000)))

    @classmethod
    def tearDownClass(cls):
        # Delete the user from list at the end.
        cls.client.delete_user(list_id, cls.email)

    def setUp(self):
        # Delete the user from list at the beginning of each test.
        self.client.delete_user(list_id, self.email)

    def first_subscribe(func):
        """
        Decorator to subscribe a user before running a test.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            ClientTests.client.subscribe_user(list_id, ClientTests.email, 'subscribed')
            return func(*args, **kwargs)
        return wrapper

    def test_initial(self):
        c = Client(api_key, username, data_center)
        self.assertEqual(c.base_url, 'https://us14.api.mailchimp.com/3.0/')

    def test_subscribe(self):
        email, status = self.email, 'subscribed'
        r = self.client.subscribe_user(list_id, email, 'subscribed', merge_fields={})
        self.assertEqual(r.get('email_address'), email)

    def test_subscribe_verify_data(self):
        merge = {'FNAME': 'John'}
        email, status = self.email, 'subscribed'
        r = self.client.subscribe_user(list_id, email, status, merge_fields=merge)
        self.assertEqual(r.get('email_address'), email)
        self.assertEqual(r.get('status'), status)
        for key, val in merge.items():
            self.assertEqual(r['merge_fields'].get(key), val)

    @first_subscribe
    def test_get(self):
        r = self.client.get_user(list_id, self.email)
        self.assertEqual(r.get('email_address'), self.email)

    @first_subscribe
    def test_delete(self):
        self.client.delete_user(list_id, self.email)
        r = self.client.get_user(list_id, self.email)
        self.assertEqual(r.get('status'), 404)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
