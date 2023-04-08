# Contents

[Matte Black](#matte-black)

[Project Goals](#project-goals)

[Planning](#planning)

[Testing](#testing)
+ [Code Validator Testing](#code-validator-testing)
+ [Manual Testing](#manual-testing)

[Bugs](#bugs)
+ [Fixed Bugs](#fixed-bugs)
+ [Unfixed Bugs](#unfixed-bugs)

[Technologies Used](#technologies-used)

[Deployment](#deployment)

[References](#references)

[Acknowledgements](#acknowledgements)



# Matte Black

[![Matte Black](/readme/images/responsive.png)](https://matte-black.herokuapp.com/)

Live Site: [Click Here](https://matte-black.herokuapp.com/)
Github Frontend: [Click Here](https://github.com/PritenMakwana44/matte-black)
Github Backend: [Click Here](https://github.com/PritenMakwana44/mb-api)

# Project Goals
The purpose of this website was to give tech lovers a place to share posts about their tech and aesthetic looking pictures of their tech setups.
Along with this the agenda was to build a community where like minded tech enthusiats can come togther to discuss and share their favourite tech.

The application was built on HTML, CSS, Javascript, React.js, Bootstrap and Django REST Framework.

# Planning

Here is my database schema:

![matteblackschema](/readme/images/matteblackschema.png)

# Testing

## Code Validator Testing
I used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate all my code. There was a built in validator too but I ran it through the linter just incase.
Only 1 issue was picked up which is in my settings.py:
"line too long (83 > 79 characters)"
I was unable to find any way of shortening the line any more.

## Manual Testing

I used the following Table to test my backend apps.


![Testing table](/readme/images/testing/test_table.png)

---

Here are the series of tests manually conducted:

## Posts Testing

Add Post testing

![Add Post Testing](/readme/images/testing/1-be-testing-addpost.png)

Read Post testing

![Read Post Testing](/readme/images/testing/2-be-testing-readpost.png)

Edit Post testing

![Edit Post Testing](/readme/images/testing/3-be-testing-editpost.png)

Edit Post after testing

![Edit Post after Testing](/readme/images/testing/4-be-testing-editpostafter.png)

Delete Post testing

![Delete Post Testing](/readme/images/testing/5-be-testing-deletepost.png)

Delete Post after testing

![Delete Post after Testing](/readme/images/testing/6-be-testing-deletepostafter.png)

---

## Profile Testing

Create User testing

![create user](/readme/images/testing/7-be-testing-createuser.png)

Profile edit testing

![Profile edit](/readme/images/testing/8-be-testing-profileedit.png)

Profile read testing

![profile read](/readme/images/testing/9-be-testing-profileread.png)

Profile read detail testing

![profile read detail](/readme/images/testing/10-be-testing-profileread.png)

---

## Gallerypost Testing

Gallery post add testing

![gallerypost add](/readme/images/testing/11-be-testing-gallerypostadd.png)

Gallery post read testing

![gallerypost read](/readme/images/testing/12-be-testing-gallerypostread.png)

Gallery post edit testing

![gallery post edit1](/readme/images/testing/13-be-testing-gallerypostedit.png)

![gallery post edit2](/readme/images/testing/14-be-testing-gallerypostedit2.png)

![gallery post edit after](/readme/images/testing/15-be-testing-galleryposteditafter.png)

Gallery post delete testing

![gallery post delete](/readme/images/testing/16-be-testing-gallerypostdelete.png)

![gallery post delete after](/readme/images/testing/17-be-testing-gallerypostdeleteafter.png)

---

## Follower Testing

Follower read testing

![follower read](/readme/images/testing/18-be-testing-followerread.png)

Follower create testing

![follower create](/readme/images/testing/19-be-testing-followercreate.png)

Follower delete testing

![follower delete](/readme/images/testing/20-be-testing-followerdelete.png)
![follower delete after](/readme/images/testing/21-be-testing-followerdeleteafter.png)

---

## Contact Testing

Contact create testing

![contact create](/readme/images/testing/22-be-testing-contactcreate.png)

Contact read testing

![contact read](/readme/images/testing/23-be-testing-contactread.png)

---

## Comment Testing

Comment create testing

![comment create](/readme/images/testing/24-be-testing-commentcreate.png)

Comment read testing

![comment read](/readme/images/testing/25-be-testing-commentread.png)

Comment edit testing

![comment edit](/readme/images/testing/26-be-testing-commentedit.png)

![comment edit after](/readme/images/testing/27-be-testing-commentreditafter.png)

Comment delete testing

![comment delete](/readme/images/testing/28-be-testing-commentdelete.png)

![comment delete after](/readme/images/testing/29-be-testing-commentdeleteafter.png)


---

## Gallery Comment Testing

Gallery comment create testing

![Gallery comment create](/readme/images/testing/30-be-testing-gallerycommentcreate.png)

Gallery comment read testing

![Gallery comment read](/readme/images/testing/31-be-testing-gallerycommentread.png)

Gallery comment edit testing

![Gallery comment edit](/readme/images/testing/32-be-testing-gallerycommentedit.png)

![Gallery comment edit after](/readme/images/testing/33-be-testing-gallerycommenteditafter.png)

Gallery comment delete testing

![Gallery comment delete](/readme/images/testing/34-be-testing-gallerycommentdelete.png)

![Gallery comment delete after](/readme/images/testing/35-be-testing-gallerycommentdeleteafter.png)

---

## Save Testing

Save create testing

![Save create](/readme/images/testing/36-be-testing-savecreate.png)

Save read testing

![Save read](/readme/images/testing/37-be-testing-saveread.png)

Save delete testing

![Save delete](/readme/images/testing/38-be-testing-savedelete.png)

![Save delete after](/readme/images/testing/39-be-testing-saverdeleteafter.png)

---


# Bugs
## Fixed Bugs

More bugs can be found in my front end readme

1. Error when creating new user. Fix: delete local database

![createuser bug](readme/images/bugs/createuser_bug.png)
    

---

## Unfixed Bugs

More bugs can be found in my front end readme

Due to time constrains we were unable to fix these following bugs:

1. When going into gallery posts with an id number I get a double form as shown below.

![createuser bug](readme/images/bugs/doubleinput_bugs.png)

---

# Technologies Used

- Django Rest framework
- Python
- Cloudinary
- ElephanSQL postgress
- CORS Headers
- Pillow
- Allauth
- Gunicorn

## Modules:

- asgiref==3.6.0
- cloudinary==1.32.0
- dj-database-url==0.5.0
- dj-rest-auth==2.1.9
- Django==3.2.18
- django-allauth==0.44.0
- django-cloudinary-storage==0.3.0
- django-cors-headers==3.14.0
- django-filter==22.1
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2
- gunicorn==20.1.0
- oauthlib==3.2.2
- Pillow==9.4.0
- psycopg2==2.9.5
- PyJWT==2.6.0
- python3-openid==3.2.0
- pytz==2022.7.1
- requests-oauthlib==1.3.1
- sqlparse==0.4.3


# Deployment

## Project setup for Backend:
Github:
1. Go to Code Insitite Template [CI template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Create project using template
Project setup:
3. Install Django using the pip3 install 'django<4' command in terminal
4. Create project using django-admin startproject 'projectname'
5. Install cloudinary and Pillow via pip install django-cloudinary-storage==0.3.0 and pip install Pillow==8.2.0
6. Add the following to your installed apps in your settings.py " 'cloudinary_storage','django.contrib.staticfiles' and'cloudinary. Make sure they are added in that order top to bottom:

```
INSTALLED_APPS = [
    (...)
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
]

```

7. Create a env.py in root of directory with import.os and os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"

```
import os
os.environ['CLOUDINARY_URL'] = 'cloudinary://<cloudinary_key>'

```

8. Add following to your settings.py:

```
from pathlib import Path
import os
if os.path.exists('env.py'):
    import env
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

```

9. Git add, commit and push

Deployment:

10. Install JSON web token auth via command pip3 install dj-rest-auth==2.1.9
11. Add 'rest_framework.authtoken' and 'dj_rest_auth' into settings.py under installed apps:

```
INSTALLED_APPS = [
    ...
    'django_filters',

    'rest_framework.authtoken', 
    'dj_rest_auth', 

    ‘profiles’,
    ...
]
```

12. Add "path('dj-rest-auth/', include('dj_rest_auth.urls'))," into your project app urls.py

```
urlpatterns = [
    …,
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    
    path('', include('profiles.urls')),
    ....,
]

```

13. Enter command python manage.py migrate
14. Install Django auth via pip install 'dj-rest-auth[with_social]'
15. Add following into settings.py 'django.contrib.sites', 'allauth', 'allauth.account', 'allauth.socialaccount', 'dj_rest_auth.registration',

```
INSTALLED_APPS = [
    …,
    'dj_rest_auth',
     
    'django.contrib.sites', 
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'dj_rest_auth.registration',

    'profiles',
    ...,
]
```

16. Add SITE_ID = 1 under installed apps list in settings.py

```
SITE_ID = 1

```
17. Add  path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), to your project app urls.py

```
urlpatterns = [
    …,
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('', include('profiles.urls')),
   …,
]

```

18. In terminal install your simplejwt package via pip install djangorestframework-simplejwt==4.7.2
19. Add the following to your env.py

```
os.environ['DEV'] = '1'

```

20. Add following to settings.py.

```
​​REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [( 
        'rest_framework.authentication.SessionAuthentication' 
        if 'DEV' in os.environ 
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
    }

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_SECURE = True
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

```

21. Create serializers.py in your project app directory e.g mb_api/serializers.py
22. Add following to your serializers.py file:

```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile_id', 'profile_image')

```

23. In settings.py add: 
```
REST_AUTH_SERIALIZERS = {'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'}

```

This will overwrite this:

```
USER_DETAILS_SERIALIZER
Place under JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

```

24. In terminal run python manage.py migrate and pip freeze > requirements.txt
25. git add, commit, push

26. Create views.py in project app e.g MB-API/views.py
27. Add following into views.py:

```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({"message": "Welcome to my django rest framework API!"})

```
28. In the project app urls.py add imports at top and urlpatterns under:

```
…
from .views import root_route


urlpatterns = [
    …,
    path('', root_route)
]

```

29. Add pagination in settings.py: 

```
REST_FRAMEWORK = {
    ...,
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    }


```

30.  Add following under last block of code but no part of same code:

```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'restframework.renderers.JSONRenderer'
    ]

```

31. In settings.py add date and time formatting:

```
REST_FRAMEWORK = {
   ...
    'DATETIME_FORMAT': '%d %b %Y'
    }

```

32. To add datetime you can add the following to comments for method to show when comment was posted or updated as per the below. But can be used in any serializer. Don't forget the import above too!

```
from django.contrib.humanize.templatetags.humanize import naturaltime

created_at = serializers.SerializerMethodField()
updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

```

33. Git add, commit, push

Heroku deployment:

34. Create new app in Heroku choosing an appropriate name and region
35. Log in to ElephantSQL or create an account 
36. Create new instance in ElephantSQL and select free plan and appropriate name and region.
37. Click into created database and copy URL which should begin with postgres:// 
38. In Heroku open app
39. Go to settings.
40. Click reveal config Vars
41. Add DATABASE_URL Key with url which is the postgres:// url.
42. Head back to your project and use pip install dj_database_url in terminal to install dj database.
43. Add import and Databse as per the below:

```
… 
import dj_database_url



DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}
```
44. Install Gunicorn via pip install gunicorn
45. Create Procfile in root of project and add the following lines:
```
release: python manage.py makemigrations && python manage.py migrate

web: gunicorn drf_api.wsgi

```
46. Head to your settings.py adn add:

```
ALLOWED_HOSTS = ['<YOURAPPNAME>.herokuapp.com', 'localhost']

```

47. Install cors via pip install django-cors-headers
48. In your settings.py add the following into your installed apps:

```
INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',

    'profiles',
    ...
]

```
49. Add following to the top of the middleware list in your settings.py:

```
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

```

50. Add following under your middleware list:

```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]


CORS_ALLOW_CREDENTIALS = True
JWT_AUTH_SAMESITE = 'None'

```

51. In your env.py set:

```
os.environ['SECRET_KEY'] = 'CreateRandomValue'

```

52. In your settings.py add:
```
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = 'DEV' in os.environ
```

53. In Heroku config vars add matching values to what is in your env.py e.g CLOUDINARY_URL, SECRET_KEY and add DISABLE_COLLECTSTATIC = 1
54. In project terminal run pip freeze > requirements.txt
55. Git add, commit and push.
56. Go into app and find the deploy tab
57. Link to Github under deployment method
58. Then search for your repo in Github and link.
59. Scroll down and hit deploy and open app to see if it works!
60. Back to project to git add, commit and push to make sure latest version had been deployed. 


# References
All Refrences are in my Frontend Readme


# Acknowledgements
All acknowledgements are in my Frontend Readme