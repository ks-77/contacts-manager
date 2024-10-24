# Django REST Contact manager API

This application has a simple functionality for viewing and managing the contact list.
With IP access restriction, and Google authentication required for access to the API.

### Contributions Google Oauth2

The basis of the functionality of restricting access to the API using Google authentication is taken from the 
[repository](https://github.com/shklqm/django-rest-google/) more general information about how it works,
and what is the basis of writing this functionality you can find there.
Modified for a specific task, updated for use under latest versions of libraries and the LTS 4.2 version of Django framework.

### IP Access Mixin

I also introduced functionality for restricting access to the API using a simple mixin with a .dispatch() method.
These perform any actions that need to occur before or after calling the handler methods such as .get(), .post(), put(), patch() and .delete().
This mixin used to collect user's IP address before switching to the API and using the 
[IPAPI](https://github.com/ipapi-co/ipapi-python?tab=readme-ov-file) library converts it to a region code,
the presence of which is checked in the list of acceptable regions.
For more competent use of the functionality, you can transfer the list of regions allowing access to the API to the env file,
I left them in the mixin, for greater clarity

### QuickStart
1. Clone the source code and setup an virtual environment
    ```bash
    git clone https://github.com/ks-77/contacts-manager
    cd contact-manager/
    python -m venv venv
    venv\Scripts\activate
    ```
2. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
3. Create env file in which you will store secure values. Generate Django secret key with the command:
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

    Get the `key` and `secret` at [google console](https://console.developers.google.com/apis/credentials)
    , set the callback url to 127.0.0.1:8000/accounts/google/login/callback
    and update the env file: 
    ```
    DJANGO_SECRET_KEY=your django secret
    GOOGLE_OAUTH2_KEY=your google app key
    GOOGLE_OAUTH2_SECRET=your google app secret
    ```
4. Finnaly run migrations and start the server
    ```bash
   python .\src\manage.py migrate
   python .\src\manage.py runserver 
   ```
5. Go to [localhost](http://127.0.0.1:8000/accounts/google/login/) and try
   to login. Upon successful login you should be redirected to
  `LOGIN_SUCCESS_URL` path. then you will have access to the [API](http://127.0.0.1:8000/contacts/)
