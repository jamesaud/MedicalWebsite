import environ
env = environ.Env()

HOME_PASSWORD = env('HOME_PASSWORD', default='default')
