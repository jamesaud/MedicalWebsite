import requests
import hashlib

class Client:
    """
    Wrapper around the mailchimp api to prevent redundant code.
    """
    def __init__(self, api_key, username, data_center):
        """
        :param api_key: the api key to the account
        :param username: the username (probably email) to log into mailchimp
        :param data_center: the datacenter in the url for your mailchimp server.
         In the url upon logging in the browser
        """
        self.api_key = api_key
        self.username = username
        self.base_url = 'https://{}.api.mailchimp.com/3.0/'.format(data_center)
        self.auth = requests.auth.HTTPBasicAuth(
                                  username,
                                  api_key)

    def _lists_endpoint(self, list_id):
        return self.base_url + 'lists/{}/members/'.format(list_id)

    @staticmethod
    def _md5hash(string):
        string = string.lower().encode('utf8')
        m = hashlib.md5()
        m.update(string)
        return m.hexdigest()

    def subscribe_user(self, list_id, email_address, status='subscribed', merge_fields={}):
        """
        Subscribes a user to a given list
        :param list_id: str, id of the list to subscribe to
        :param email_address: str, address to subscribe
        :param status: value to set the status to
        :param merge_fields: extra fields for the user
        :return: dict, details of the response
        """

        data = {"email_address": email_address,
                "status": status,
                "merge_fields": merge_fields,
        }
        r = requests.post(self._lists_endpoint(list_id), json=data, auth=self.auth)
        return r.json()

    def unsubscribe_user(self, list_id, email_address, status='unsubscribed'):
        email_hash = self._md5hash(email_address)
        data = {'status': status}
        r = requests.patch(self._lists_endpoint(list_id) + email_hash, json=data, auth=self.auth)
        return r.json()

    def delete_user(self, list_id, email_address):
        email_hash = self._md5hash(email_address)
        r = requests.delete(self._lists_endpoint(list_id) + email_hash, auth=self.auth)

        if r.content:  # Return the failed json response
            return r.json()
        else:  # If the content is empty, it sucessfully deleted. However, .json raises a JSONDecodeError
            return {'status': 200} # Return a 200 success code if succeeded

    def get_user(self, list_id, email_address):
        email_hash = self._md5hash(email_address)
        r = requests.get(self._lists_endpoint(list_id) + email_hash, auth=self.auth)
        return r.json()
