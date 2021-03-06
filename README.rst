Medical Website
==============================

Live Preview of the Site:

http://104.236.125.205/


INSTRUCTIONS TO SET UP AND VIEW LOCALLY (Must have docker and docker-compose installed):

> git clone https://github.com/jamesaud/MedicalWebsite

> cd MedicalWebsite

> docker-compose -f dev.yml build

> docker-compose -f dev.yml up

Find your docker machine ip address (> docker-machine ip) if running docker machine, otherwise use your local computer's ip.

Visit port 8000 in your browser.

For example, if my docker machine ip was 256.34.23.12, the url would be:

256.34.23.12:8000

==============================

medical website

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django



Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test


Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html




Deployment
----------



Heroku
^^^^^^

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html





Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

More help: https://realpython.com/blog/python/development-and-deployment-of-cookiecutter-django-via-docker/


Mailchimp v3 API
^^^^^^^^^^^^^^
https://github.com/charlesthk/python-mailchimp


Extra Tutorials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a fixture from the an app - in this case 'homepage'
::
    $ docker-compose -f dev.yml  run django python manage.py dumpdata --format=yaml --indent=4 homepage > $(pwd)/medweb/fixtures/initial_data.yaml


