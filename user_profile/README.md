# Django Customize User Creation With Confirmation Email

Make sure your django project is setup already. Follow Tetum documentation of how to create new project using Django ([https://onydev.pykafe.org/tet/detail/kria-projetu-uza-django/](https://onydev.pykafe.org/tet/detail/kria-projetu-uza-django/))

### Let's Get started
Git clone this repository into your existing django project
```
git clone https://github.com/marobo/user_profile.git
```

Remove git from "user_profile" to prevent double git from this repository in your project:
```
rm -rf user_profile/.git
rm user_profile/.gitignore
```

To include the app in your project, you need to add a reference to its configuration class in the **INSTALLED_APPS** section in `setting.py`. 

Edit the `your_project/settings.py` file and add the `user_profile` app to the **INSTALLED_APPS** setting. It’ll look like this:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_profile', # New app
]
```

We need to configure the email host server as well in the `settings.py` for confirmation mail. Add below configuration into `your_project/settings.py` file. So when the sign up form is submitted successfully it will be send out the text confirmation mail via terminal on your running server 

```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

Add `user_profile` app url to the project/base configuration URL in `yourproject/urls.py` 
```
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_profile.urls')), # New app urls
    path('accounts/', include('django.contrib.auth.urls')), # New or maybe you have added already
]
```

Let's run server and then try to Sign Up:
```
python manage.py runserver
http://localhost:8000/create-account
```

When the Sign Up form is submitted successfully you'll see the feedback message `Please check your email!`.
Now go to the terminal server you running, you'll see email confirmation messages as example as showing below:
```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Welcome to localhost:8000
From: webmaster@localhost
To: emailyouresgistered@gmail.com
Date: Mon, 11 Mar 2024 05:21:28 -0000
Message-ID: <171013448854.74991.4945198941969335774@onorios-air.busa>


Hello username,

Please verify your email by clicking on the following link.
Link: http://localhost:8000/activate/Mw/c3pljs-4d8452e391dee5d266616a6bfa7ace8a


Many Thanks
Dev Team

-------------------------------------------------------------------------------
```



# Note
This is just for playing in locally. If you like to send the confirmation email to the real email address you enter in the sign up from then you need to change:
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" to EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
```
and add those email variable in the `settings.py` file
```
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'youremail@gmail.com'  
EMAIL_HOST_PASSWORD = 'yourpassword'  
EMAIL_PORT = 587
```

Please don't use your real email password in EMAIL_HOST_PASSWORD for security reason. Try generate it from gmail app password.


To Generate/create an app password in Gmail, you can do the following:
1. Log in to your Google account
2. Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Select Security
4. Under "Signing in to Google," select 2-Step Verification
5. At the bottom of the page, select App passwords
6. Select Other from the Select app drop-down
7. Name the app password
8. Click Generate
9. Copy the new app password to the EMAIL_HOST_PASSWORD = 'yournewpassword' in settings.py file
10. Click Done

Visit this more instruction [https://support.google.com/mail/answer/185833?sjid=4090351568356337842-AP](https://support.google.com/mail/answer/185833?sjid=4090351568356337842-AP)
