========================
CODE SNIPPETS
========================
TITLE: Project Setup and Installation
DESCRIPTION: Commands to create a Django project, set up a virtual environment, install Django REST framework, and create a new app.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_0

LANGUAGE: bash
CODE:
```
mkdir tutorial
cd tutorial
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install djangorestframework
django-admin startproject tutorial .
cd tutorial
django-admin startapp quickstart
cd ..
```

----------------------------------------

TITLE: Project Layout in Quickstart
DESCRIPTION: The project layout has been added to the quickstart guide, providing new users with a better understanding of the project structure.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_232

LANGUAGE: APIDOC
CODE:
```
Quickstart Guide:
  Project layout added.
```

----------------------------------------

TITLE: Django REST Framework Tutorials and Guides
DESCRIPTION: A collection of tutorials and guides for learning Django REST Framework, covering various aspects from basic setup to advanced features.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/tutorials-and-resources.md#_snippet_0

LANGUAGE: Python
CODE:
```
https://code.tutsplus.com/tutorials/beginners-guide-to-the-django-rest-framework--cms-19786
https://blog.kevinastone.com/django-rest-framework-and-angular-js
https://mourafiq.com/2013/07/01/end-to-end-web-app-with-django-angular-1.html
https://richardtier.com/2014/02/25/django-rest-framework-user-endpoint/
https://richardtier.com/2014/03/06/110/
https://www.dabapps.com/blog/api-performance-profiling-django-rest-framework/
https://bnotions.com/news-and-insights/api-development-with-django-and-django-rest-framework/
https://web.archive.org/web/20180104205117/http://machinalis.com/blog/pandas-django-rest-framework-bokeh/
https://web.archive.org/web/20180104205043/https://machinalis.com/blog/controlling-uncertainty-on-web-applications-and-apis/
https://web.archive.org/web/20180104205059/http://machinalis.com/blog/full-text-search-on-django-rest-framework/
https://web.archive.org/web/20180104205054/http://machinalis.com/blog/oauth2-authentication/
https://web.archive.org/web/20180104205109/http://machinalis.com/blog/nested-resources-with-django/
https://web.archive.org/web/20180104205048/http://machinalis.com/blog/image-fields-with-django-rest-framework/
https://chatbotslife.com/chatbot-using-django-rest-framework-api-ai-slack-part-1-3-69c7e38b7b1e#.g2aceuncf
https://blog.levit.be/new-django-admin-with-emberjs-what-are-the-news/
https://drf-schema-adapter.readthedocs.io/en/latest/
https://www.andreagrandi.it/posts/creating-production-ready-api-python-django-rest-framework-part-1/
https://www.andreagrandi.it/posts/creating-a-production-ready-api-with-python-and-django-rest-framework-part-2/
https://www.andreagrandi.it/posts/creating-a-production-ready-api-with-python-and-django-rest-framework-part-3/
https://www.andreagrandi.it/posts/creating-a-production-ready-api-with-python-and-django-rest-framework-part-4/
https://learndjango.com/tutorials/django-polls-tutorial-api
https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api
https://realpython.com/blog/python/django-rest-framework-quick-start/
https://tests4geeks.com/django-rest-framework-tutorial/
https://agiliq.com/blog/2014/12/building-a-restful-api-with-django-rest-framework/
```

----------------------------------------

TITLE: Setup Virtual Environment and Run Tests
DESCRIPTION: Commands to set up a Python virtual environment, install dependencies, and run the project's tests. This includes activating the environment and executing the test runner script.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/contributing.md#_snippet_2

LANGUAGE: shell
CODE:
```
# Setup the virtual environment
python3 -m venv env
source env/bin/activate
pip install -e .
pip install -r requirements.txt

# Run the tests
./runtests.py
```

----------------------------------------

TITLE: Installing HTTPie Client - Bash
DESCRIPTION: This shell command uses pip to install `httpie`, a user-friendly command-line HTTP client. Httpie is recommended for testing the Web API endpoints. Prerequisites include Python and pip installed.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_28

LANGUAGE: bash
CODE:
```
pip install httpie
```

----------------------------------------

TITLE: Running Django Development Server - Bash
DESCRIPTION: This shell command starts Django's built-in development server. This server is used for testing the application locally and serves the defined API endpoints. Prerequisites include a working Django project setup and the project's virtual environment activated (if used).

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_27

LANGUAGE: bash
CODE:
```
python manage.py runserver
```

----------------------------------------

TITLE: Basic ListCreateAPIView Example
DESCRIPTION: Demonstrates a typical setup for a generic API view using `ListCreateAPIView`. It shows how to define the queryset, serializer class, and permission classes for a user list endpoint.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/generic-views.md#_snippet_0

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
```

----------------------------------------

TITLE: Install HTTPie Command-Line Client
DESCRIPTION: Installs HTTPie, a user-friendly command-line HTTP client, using pip. HTTPie simplifies sending HTTP requests and viewing responses.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_23

LANGUAGE: Python
CODE:
```
pip install httpie
```

----------------------------------------

TITLE: Install httpie
DESCRIPTION: Installs the httpie command-line HTTP client using pip, a user-friendly alternative to curl for testing APIs.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_16

LANGUAGE: bash
CODE:
```
pip install httpie
```

----------------------------------------

TITLE: Install CoreAPI Python Client
DESCRIPTION: Installs the CoreAPI Python client library using pip. This library is used to interact with APIs documented using CoreAPI, often integrated with Django REST Framework.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/rest_framework/templates/rest_framework/docs/langs/python-intro.html#_snippet_0

LANGUAGE: bash
CODE:
```
# Install the Python client library
$ pip install coreapi
```

----------------------------------------

TITLE: Install Django REST Framework with Optional Packages
DESCRIPTION: Installs the Django REST Framework package using pip. It also shows how to install optional packages for Markdown support and filtering.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/index.md#_snippet_4

LANGUAGE: bash
CODE:
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

----------------------------------------

TITLE: Installing and Configuring External Packages
DESCRIPTION: Instructions for installing and configuring packages that have been moved out of the core Django REST Framework. This includes installing the package via pip and updating the `REST_FRAMEWORK` settings.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.1-announcement.md#_snippet_8

LANGUAGE: bash
CODE:
```
pip install djangorestframework-xml

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer'
    ]
}
```

----------------------------------------

TITLE: Database Migration and Superuser Creation
DESCRIPTION: Commands to migrate the database and create an initial superuser for authentication.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_1

LANGUAGE: bash
CODE:
```
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```

----------------------------------------

TITLE: Install coreapi-cli
DESCRIPTION: Installs the coreapi command-line client using pip. This client is often used for interacting with REST APIs.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/rest_framework/templates/rest_framework/docs/langs/shell-intro.html#_snippet_0

LANGUAGE: bash
CODE:
```
# Install the command line client
$ pip install coreapi-cli
```

----------------------------------------

TITLE: Start Django Development Server
DESCRIPTION: Starts Django's built-in development server to serve the application. It validates models and indicates the server address and port.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_15

LANGUAGE: bash
CODE:
```
python manage.py runserver
```

----------------------------------------

TITLE: Install Transifex Client
DESCRIPTION: Installs the official Transifex client using pip. This client is essential for uploading and downloading translation files.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/project-management.md#_snippet_7

LANGUAGE: bash
CODE:
```
pip install transifex-client
```

----------------------------------------

TITLE: Request Example for Unsupported Media Type
DESCRIPTION: Demonstrates an HTTP GET request to an API endpoint with an unsupported Accept header and a specified Accept-Language header. This illustrates how the framework handles such requests.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.1-announcement.md#_snippet_4

LANGUAGE: http
CODE:
```
GET /api/users HTTP/1.1
Accept: application/xml
Accept-Language: es-es
Host: example.org
```

----------------------------------------

TITLE: Test API with httpie
DESCRIPTION: Shows how to test the API using the `httpie` command-line tool, which provides a more user-friendly interface for making HTTP requests, including authentication.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_10

LANGUAGE: bash
CODE:
```
http -a admin http://127.0.0.1:8000/users/
```

----------------------------------------

TITLE: Install and Run Pre-commit Hooks
DESCRIPTION: Steps to install and set up pre-commit hooks for ensuring code adheres to PEP 8 style conventions. This is done using pip and the pre-commit command.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/contributing.md#_snippet_1

LANGUAGE: shell
CODE:
```
python -m pip install pre-commit
pre-commit install
```

----------------------------------------

TITLE: API Request Example
DESCRIPTION: An example HTTP GET request to an API endpoint, demonstrating the use of `Accept-Language` header to request content in Spanish (`es-es`). This is how clients can specify their preferred language.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/topics/internationalization.md#_snippet_2

LANGUAGE: http
CODE:
```
GET /api/users HTTP/1.1
Accept: application/xml
Accept-Language: es-es
Host: example.org
```

----------------------------------------

TITLE: Setting up a new environment
DESCRIPTION: Creates a new virtual environment using venv, installs Django, Django REST Framework, and Pygments for code highlighting.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_0

LANGUAGE: bash
CODE:
```
python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
pip install pygments
```

----------------------------------------

TITLE: Basic Django REST Framework Usage
DESCRIPTION: Illustrates a basic setup for using Django REST framework, likely involving defining serializers and views. This is a foundational example for API development.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/index.md#_snippet_3

LANGUAGE: Python
CODE:
```
# Example of a serializer
from rest_framework import serializers

class MyModelSerializer(serializers.Serializer):
    field1 = serializers.CharField(max_length=100)
    field2 = serializers.IntegerField()

# Example of a view
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    def get(self, request, format=None):
        content = {'detail': 'Hello, world!'}
        return Response(content)
```

----------------------------------------

TITLE: API Guide Links
DESCRIPTION: References to API guide documentation for various features.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.1-announcement.md#_snippet_11

LANGUAGE: APIDOC
CODE:
```
custom-exception-handler: ../api-guide/exceptions.md#custom-exception-handling
pagination: ../api-guide/pagination.md
versioning: ../api-guide/versioning.md
internationalization: ../topics/internationalization.md
customizing-field-mappings: ../api-guide/serializers.md#customizing-field-mappings
```

----------------------------------------

TITLE: Install Django REST framework
DESCRIPTION: Installs the Django REST framework package using pip and adds 'rest_framework' to the INSTALLED_APPS setting in Django.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/README.md#_snippet_0

LANGUAGE: bash
CODE:
```
pip install djangorestframework
```

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

----------------------------------------

TITLE: MultipleFieldLookupMixin Documentation Example
DESCRIPTION: The documentation example for `MultipleFieldLookupMixin` has been corrected to properly demonstrate object-level permission checks.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_225

LANGUAGE: APIDOC
CODE:
```
MultipleFieldLookupMixin:
  Documentation example updated to correctly show object-level permission checks.
```

----------------------------------------

TITLE: OpenAPI Schema Generation: Docstring Example
DESCRIPTION: Demonstrates how OpenAPI operation descriptions are extracted from class docstrings for GET and POST methods in an APIView.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.11-announcement.md#_snippet_0

LANGUAGE: python
CODE:
```
class DocStringExampleListView(APIView):
    """
    get: A description of my GET operation.
    post: A description of my POST operation.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        ...
```

----------------------------------------

TITLE: CursorPagination - OpenAPI `examples` and `format`
DESCRIPTION: Includes `examples` and `format` in the OpenAPI schema for `CursorPagination`. This provides more detailed information about the pagination parameters and their expected values.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_67

LANGUAGE: APIDOC
CODE:
```
CursorPagination:
  parameters:
    - in: query
      name: cursor
      schema:
        type: string
      required: false
      description: The cursor for pagination.
      examples:
        - "gAAAAAB..."
        - "hAAAAAB..."
      format: "string"

```

----------------------------------------

TITLE: Testing Snippet List Endpoint with HTTPie - Bash
DESCRIPTION: This shell command uses `httpie` to send a GET request to the `/snippets/` endpoint of the locally running Django development server. It retrieves and displays the list of all code snippets in JSON format. Prerequisites include the Django server running and `httpie` installed.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_29

LANGUAGE: bash
CODE:
```
http GET http://127.0.0.1:8000/snippets/ --unsorted
```

----------------------------------------

TITLE: Test API with curl
DESCRIPTION: Demonstrates how to fetch user data from the API using the `curl` command-line tool, including basic authentication and JSON content negotiation.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_9

LANGUAGE: bash
CODE:
```
curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
```

----------------------------------------

TITLE: Define a Basic ModelViewSet for Accounts
DESCRIPTION: Provides an example of a ModelViewSet subclass for managing accounts. It demonstrates the typical setup requiring queryset and serializer_class attributes, along with optional permission_classes.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/viewsets.md#_snippet_17

LANGUAGE: python
CODE:
```
class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
```

----------------------------------------

TITLE: PageNumberPagination Request/Response Example
DESCRIPTION: Illustrates a typical GET request using page number pagination and the corresponding JSON response structure.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/pagination.md#_snippet_4

LANGUAGE: http
CODE:
```
GET https://api.example.org/accounts/?page=4

HTTP 200 OK
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?page=5",
    "previous": "https://api.example.org/accounts/?page=3",
    "results": [
       …
    ]
}
```

----------------------------------------

TITLE: Install dj-rest-auth
DESCRIPTION: Installs the dj-rest-auth package using pip. This package provides REST API endpoints for user registration, authentication, and management.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_28

LANGUAGE: bash
CODE:
```
pip install dj-rest-auth
```

----------------------------------------

TITLE: Setup.py Error Fix
DESCRIPTION: Resolves a setup.py error that occurred on certain platforms, improving the installation process.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_321

LANGUAGE: python
CODE:
```
# No code snippet available, this is a description of a change.
```

----------------------------------------

TITLE: Add Django REST Framework to INSTALLED_APPS
DESCRIPTION: Includes 'rest_framework' in the `INSTALLED_APPS` setting to enable its features within a Django project.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_8

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

----------------------------------------

TITLE: Permissions.md get_object() Example Update
DESCRIPTION: The example for `get_object()` in `permissions.md` has been updated for clarity and accuracy.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_226

LANGUAGE: APIDOC
CODE:
```
permissions.md:
  get_object() example updated.
```

----------------------------------------

TITLE: Serve Documentation Locally with MkDocs
DESCRIPTION: Instructions on how to build and serve the project documentation locally for preview in a browser. This command starts a local development server that automatically reloads on changes.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/contributing.md#_snippet_11

LANGUAGE: Shell
CODE:
```
mkdocs serve
```

----------------------------------------

TITLE: Start Django Development Server
DESCRIPTION: Initiates the Django development server, making the web application accessible locally via HTTP. This command is essential for testing Django projects during development.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_22

LANGUAGE: Python
CODE:
```
python manage.py runserver
```

----------------------------------------

TITLE: ModelViewSet Example
DESCRIPTION: Illustrates the basic setup for a `ModelViewSet`, which provides default implementations for CRUD operations. It requires `queryset` and `serializer_class` attributes to be defined.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/viewsets.md#_snippet_11

LANGUAGE: python
CODE:
```
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
```

----------------------------------------

TITLE: Testing Snippet Detail Endpoint with HTTPie - Bash
DESCRIPTION: This shell command uses `httpie` to send a GET request to the `/snippets/2/` endpoint, targeting the snippet with ID 2. It retrieves and displays the details of that specific code snippet in JSON format. Prerequisites include the Django server running, `httpie` installed, and a snippet with ID 2 existing in the database.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_30

LANGUAGE: bash
CODE:
```
http GET http://127.0.0.1:8000/snippets/2/ --unsorted
```

----------------------------------------

TITLE: Update get_object() Example in permissions.md
DESCRIPTION: The example for `get_object()` in `permissions.md` has been updated.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_249

LANGUAGE: APIDOC
CODE:
```
permissions.md:
  get_object() example updated.
```

----------------------------------------

TITLE: Building Documentation
DESCRIPTION: Commands to build and serve the documentation for Django REST Framework using MkDocs. Ensure MkDocs is installed via pip.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/contributing.md#_snippet_5

LANGUAGE: Shell
CODE:
```
pip install mkdocs

mkdocs build

mkdocs serve
```

----------------------------------------

TITLE: CoreAPI Client Initialization and Action
DESCRIPTION: This snippet shows how to initialize the CoreAPI client, define an API action, and execute it with optional parameters. It assumes `coreapi.js` and `schema.js` are loaded and that `schema` and `section_key`/`link_key` are available in the global scope. The example demonstrates a basic interaction pattern for REST Framework APIs.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/rest_framework/templates/rest_framework/docs/langs/javascript.html#_snippet_0

LANGUAGE: javascript
CODE:
```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = [{% if section_key %}"{{ section_key }}", {% endif %}"{{ link_key }}"]
{% if link.fields %}var params = {
{% for field in link.fields %}    {{ field.name }}: ...{% if not loop.last %},{% endif %}
{% endfor %}} {% endif %}
client.action(schema, action{% if link.fields %}, params{% endif %}).then(function(result) {
    // Return value is in 'result'
})
```

----------------------------------------

TITLE: Test Django REST API with httpie
DESCRIPTION: This bash snippet illustrates how to query a Django REST Framework API endpoint using the `httpie` command-line tool, including authentication and displaying the HTTP response header and JSON body.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_11

LANGUAGE: bash
CODE:
```
bash: http -a admin http://127.0.0.1:8000/users/
http: password for admin@127.0.0.1:8000::
$HTTP/1.1 200 OK
...
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "email": "admin@example.com",
            "groups": [],
            "url": "http://127.0.0.1:8000/users/1/",
            "username": "admin"
        }
    ]
}
```

----------------------------------------

TITLE: User ViewSet Implementation
DESCRIPTION: Implements a ViewSet for the User model, allowing users to be viewed or edited via the API.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_4

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
```

----------------------------------------

TITLE: Install Django OAuth Toolkit
DESCRIPTION: Installs the Django OAuth Toolkit package using pip. This package provides OAuth 2.0 support for Django.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_23

LANGUAGE: bash
CODE:
```
pip install django-oauth-toolkit
```

----------------------------------------

TITLE: Install djangorestframework-oauth
DESCRIPTION: Installs the djangorestframework-oauth package using pip. This package provides OAuth1 and OAuth2 support for REST framework.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_25

LANGUAGE: bash
CODE:
```
pip install djangorestframework-oauth
```

----------------------------------------

TITLE: Install djangorestframework-xml
DESCRIPTION: Provides the pip command to install the `djangorestframework-xml` package, which adds support for a simple informal XML format in Django REST Framework.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/renderers.md#_snippet_23

LANGUAGE: bash
CODE:
```
$ pip install djangorestframework-xml
```

----------------------------------------

TITLE: Curl Example for Token Authentication
DESCRIPTION: An example using `curl` to test an API endpoint secured with Token Authentication. It demonstrates how to pass the Authorization header.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_8

LANGUAGE: bash
CODE:
```
curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

----------------------------------------

TITLE: Install HawkREST
DESCRIPTION: Installs the HawkREST library using pip. This library enables Hawk HTTP authentication for Django REST Framework APIs.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_27

LANGUAGE: bash
CODE:
```
pip install HawkREST
```

----------------------------------------

TITLE: ViewSet standard actions example
DESCRIPTION: This example demonstrates the standard actions that will be handled by a router class. If you're using format suffixes, make sure to also include the `format=None` keyword argument for each action.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/viewsets.md#_snippet_4

LANGUAGE: python
CODE:
```
class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
```

----------------------------------------

TITLE: Django REST framework Versioning Example
DESCRIPTION: Example demonstrating how hyperlinked serializers resolve relationships to the same API version as the incoming request when using NamespaceVersioning.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.1-announcement.md#_snippet_1

LANGUAGE: python
CODE:
```
class AccountsSerializer(serializer.HyperlinkedModelSerializer):
    class Meta:
        model = Accounts
        fields = ['account_name', 'users']

# Example Usage:
# GET http://example.org/v2/accounts/10  # Version 'v2'
# {
#     "account_name": "europa",
#     "users": [
#         "http://example.org/v2/users/12",  # Version 'v2'
#         "http://example.org/v2/users/54",
#         "http://example.org/v2/users/87"
#     ]
# }
```

----------------------------------------

TITLE: Install and Configure XML Parser for Django REST Framework
DESCRIPTION: Instructions for integrating `djangorestframework-xml` to add XML parsing and rendering support. It covers installation via pip and configuration in `REST_FRAMEWORK` settings to set default parser and renderer classes.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/parsers.md#_snippet_11

LANGUAGE: shell
CODE:
```
$ pip install djangorestframework-xml
```

LANGUAGE: python
CODE:
```
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework_xml.parsers.XMLParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework_xml.renderers.XMLRenderer',
    ],
}
```

----------------------------------------

TITLE: Fix Example 'httpie' Call in Docs
DESCRIPTION: This update rectifies an incorrect 'httpie' command example provided in the documentation. 'httpie' is a command-line HTTP client, and this fix ensures users can correctly test API endpoints.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_5

LANGUAGE: bash
CODE:
```
# Original (incorrect) httpie command example:
# http GET /api/users/

# Corrected httpie command example:
# http GET http://localhost:8000/api/users/
# or with specific headers/data:
# http POST http://localhost:8000/api/users/ username=test password=test

```

----------------------------------------

TITLE: Django REST Framework API Guide Links
DESCRIPTION: Provides links to various sections of the Django REST Framework API guide, covering authentication, serializers, views, and more.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/README.md#_snippet_11

LANGUAGE: APIDOC
CODE:
```
API Guide Sections:
  Authentication:
    OAuth1: https://www.django-rest-framework.org/api-guide/authentication/#django-rest-framework-oauth
    OAuth2: https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit
  Serializers:
    Overview: https://www.django-rest-framework.org/api-guide/serializers/#serializers
    ModelSerializer: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
  Views:
    Function-based Views: https://www.django-rest-framework.org/api-guide/views/#function-based-views
    Generic Views: https://www.django-rest-framework.org/api-guide/generic-views/
    ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/
  Routers: https://www.django-rest-framework.org/api-guide/routers/
  Serializers (General): https://www.django-rest-framework.org/api-guide/serializers/
  Authentication (General): https://www.django-rest-framework.org/api-guide/authentication/
  Quickstart Image: https://www.django-rest-framework.org/img/quickstart.png
```

----------------------------------------

TITLE: Group ViewSet Implementation
DESCRIPTION: Implements a ViewSet for the Group model, allowing groups to be viewed or edited via the API.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_5

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

----------------------------------------

TITLE: Install djangorestframework-yaml
DESCRIPTION: Provides the pip command to install the `djangorestframework-yaml` package, which adds YAML parsing and rendering support to Django REST Framework.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/renderers.md#_snippet_21

LANGUAGE: bash
CODE:
```
$ pip install djangorestframework-yaml
```

----------------------------------------

TITLE: Fix Example for Serializer Field with Choices in Docs
DESCRIPTION: This documentation fix addresses an example demonstrating a serializer field that uses choices. It ensures the example accurately reflects how to define and use choices for serializer fields.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_6

LANGUAGE: python
CODE:
```
from rest_framework import serializers

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
)

class MyModelSerializer(serializers.Serializer):
    # Original (potentially incorrect) example might have missed choices definition
    # status = serializers.CharField()

    # Corrected example:
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

```

----------------------------------------

TITLE: Custom Throttle Implementation Example
DESCRIPTION: Provides an example of creating a custom throttle class by inheriting from `BaseThrottle` and implementing the `allow_request` method.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/throttling.md#_snippet_10

LANGUAGE: python
CODE:
```
import random
from rest_framework import throttling

class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
```

----------------------------------------

TITLE: Object-Level Validation Example
DESCRIPTION: Shows how to perform validation that involves multiple fields using the `.validate()` method in a serializer. This example checks if the 'start' datetime is before the 'finish' datetime, raising a ValidationError if the condition is not met. It returns the validated data dictionary.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/serializers.md#_snippet_9

LANGUAGE: python
CODE:
```
from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
```

----------------------------------------

TITLE: Full Theme and Navbar Customization Example
DESCRIPTION: This comprehensive HTML/Django template example shows how to simultaneously override both the Bootstrap theme and the navbar variant for the browsable API. It uses a CDN link for a Bootswatch theme.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/topics/browsable-api.md#_snippet_3

LANGUAGE: html
CODE:
```
{% extends "rest_framework/base.html" %}

{% block bootstrap_theme %}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@3.4.1/flatly/bootstrap.min.css" type="text/css">
{% endblock %}

{% block bootstrap_navbar_variant %}{% endblock %}
```

----------------------------------------

TITLE: Custom Versioning Scheme Example
DESCRIPTION: Provides an example of creating a custom versioning scheme by subclassing `URLPathVersioning` and defining custom `default_version`, `allowed_versions`, and `version_param` attributes.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/versioning.md#_snippet_5

LANGUAGE: python
CODE:
```
from rest_framework.versioning import URLPathVersioning
from rest_framework.views import APIView

class ExampleVersioning(URLPathVersioning):
    default_version = 'v2'
    allowed_versions = ['v1', 'v2']
    version_param = 'api_version'

class ExampleView(APIView):
    versioning_class = ExampleVersioning
```

----------------------------------------

TITLE: Allow PUT as Create Mixin Example
DESCRIPTION: Provides an example of a mixin class that enables the 'PUT as create' behavior for Django REST Framework views. This contrasts with the default '404' behavior introduced in version 3.0.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/generic-views.md#_snippet_13

LANGUAGE: python
CODE:
```
class AllowPUTAsCreateMixin:
    # Mixin implementation for PUT as create behavior
    pass
```

----------------------------------------

TITLE: Creating a Django Project and App
DESCRIPTION: Sets up a new Django project named 'tutorial' and creates a 'snippets' app within it.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_1

LANGUAGE: bash
CODE:
```
cd ~
django-admin startproject tutorial
cd tutorial
python manage.py startapp snippets
```

----------------------------------------

TITLE: Show Installed Django REST Framework Version
DESCRIPTION: Command to display the version of Django REST Framework currently installed in the Python environment. This is useful for verifying the upgrade or checking compatibility.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_1

LANGUAGE: bash
CODE:
```
pip show djangorestframework
```

----------------------------------------

TITLE: Install and Configure YAML Parser for Django REST Framework
DESCRIPTION: Instructions for integrating `djangorestframework-yaml` to add YAML parsing and rendering support. It covers installation via pip and configuration in `REST_FRAMEWORK` settings to set default parser and renderer classes.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/parsers.md#_snippet_10

LANGUAGE: shell
CODE:
```
$ pip install djangorestframework-yaml
```

LANGUAGE: python
CODE:
```
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework_yaml.parsers.YAMLParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework_yaml.renderers.YAMLRenderer',
    ],
}
```

----------------------------------------

TITLE: Django REST Framework Token Authentication Setup
DESCRIPTION: Demonstrates how to set up and use Token Authentication in Django REST Framework. This includes adding `rest_framework.authtoken` to INSTALLED_APPS, running migrations, and creating tokens.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_6

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```

LANGUAGE: python
CODE:
```
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)
```

----------------------------------------

TITLE: Install drf-social-oauth2
DESCRIPTION: Installs the drf-social-oauth2 package using pip. This framework facilitates authentication with social OAuth2 providers like Facebook and Google.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_29

LANGUAGE: bash
CODE:
```
pip install drf-social-oauth2
```

----------------------------------------

TITLE: Enable Django REST Framework Pagination
DESCRIPTION: Enables default pagination for the API by setting the `DEFAULT_PAGINATION_CLASS` and `PAGE_SIZE` in Django's settings.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_7

LANGUAGE: python
CODE:
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

----------------------------------------

TITLE: SerializerMethodField Example
DESCRIPTION: Example demonstrating the usage of SerializerMethodField to calculate and include the number of days since a user joined.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/fields.md#_snippet_32

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
```

----------------------------------------

TITLE: QueryParameterVersioning Example
DESCRIPTION: Demonstrates the QueryParameterVersioning scheme, where the API version is passed as a query parameter in the URL.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/versioning.md#_snippet_15

LANGUAGE: http
CODE:
```
GET /something/?version=0.1 HTTP/1.1
Host: example.com
Accept: application/json
```

----------------------------------------

TITLE: NamespaceVersioning Example
DESCRIPTION: Demonstrates the NamespaceVersioning scheme, which is similar to URLPathVersioning from the client's perspective but configured using URL namespaces in Django.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/versioning.md#_snippet_11

LANGUAGE: http
CODE:
```
GET /v1/something/ HTTP/1.1
Host: example.com
Accept: application/json
```

----------------------------------------

TITLE: Added Tutorial Links
DESCRIPTION: Includes links to new tutorials, specifically 'A Todo List API with React' and 'Blog API', to aid user learning.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_184

LANGUAGE: python
CODE:
```
# Added links to 'A Todo List API with React' and 'Blog API' tutorials [#5837][gh5837]
```

----------------------------------------

TITLE: Basic REST Framework Settings
DESCRIPTION: Example of how to configure REST Framework settings in Django's `settings.py` file, specifying default renderers and parsers.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/settings.md#_snippet_0

LANGUAGE: python
CODE:
```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```

----------------------------------------

TITLE: Instantiating DefaultRouter
DESCRIPTION: Demonstrates how to instantiate DefaultRouter, with an example of disabling trailing slashes.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/routers.md#_snippet_7

LANGUAGE: python
CODE:
```
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
```

----------------------------------------

TITLE: SimpleRouter Usage Example
DESCRIPTION: Demonstrates the basic usage of `SimpleRouter` to register viewsets and generate URL patterns. It shows how to instantiate a router, register viewsets with their prefixes, and access the generated URLs.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/routers.md#_snippet_0

LANGUAGE: python
CODE:
```
from rest_framework import routers\n\nrouter = routers.SimpleRouter()\nrouter.register(r'users', UserViewSet)\nrouter.register(r'accounts', AccountViewSet)\urlpatterns = router.urls
```

----------------------------------------

TITLE: Swagger UI Integration Example
DESCRIPTION: A minimal Django template for integrating Swagger UI to display API documentation. It requires a schema URL and sets up the Swagger UI bundle with basic configurations and a request interceptor for CSRF tokens.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/topics/documenting-your-api.md#_snippet_0

LANGUAGE: html
CODE:
```
<!DOCTYPE html>
<html>
  <head>
    <title>Swagger</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="//unpkg.com/swagger-ui-dist@3/swagger-ui.css" />
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
    <script>
    const ui = SwaggerUIBundle({
        url: "{% url schema_url %}",
        dom_id: '#swagger-ui',
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "BaseLayout",
        requestInterceptor: (request) => {
          request.headers['X-CSRFToken'] = "{{ csrf_token }}"
          return request;
        }
      })
    </script>
  </body>
</html>
```

----------------------------------------

TITLE: Basic Django REST Framework API Example
DESCRIPTION: Demonstrates setting up a simple model-backed API for users using Django REST framework. It includes defining a serializer for the User model and a ViewSet for handling user data, then registering it with a router.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/README.md#_snippet_1

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.

```

----------------------------------------

TITLE: Example OPTIONS Response
DESCRIPTION: Demonstrates a typical JSON response for an HTTP OPTIONS request, including allowed methods, content types, and schema information for actions.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/metadata.md#_snippet_0

LANGUAGE: http
CODE:
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json

{
    "name": "To Do List",
    "description": "List existing 'To Do' items, or create a new item.",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "note": {
                "type": "string",
                "required": false,
                "read_only": false,
                "label": "title",
                "max_length": 100
            }
        }
    }
}
```

----------------------------------------

TITLE: Tutorial @api_view Usage
DESCRIPTION: Uses a safer calling method for `@api_view` in the tutorial, improving example clarity.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_367

LANGUAGE: python
CODE:
```
# No code snippet available, this is a description of a change.
```

----------------------------------------

TITLE: LimitOffsetPagination Setup and Configuration
DESCRIPTION: Shows how to enable LimitOffsetPagination globally via Django settings and lists its configurable attributes for customization.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/pagination.md#_snippet_7

LANGUAGE: python
CODE:
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}
```

LANGUAGE: APIDOC
CODE:
```
LimitOffsetPagination Configuration:

* `default_limit`: Numeric value for the limit if not provided by client. Defaults to `PAGE_SIZE` setting.
* `limit_query_param`: String name for the "limit" query parameter. Defaults to `'limit'`.
* `offset_query_param`: String name for the "offset" query parameter. Defaults to `'offset'`.
* `max_limit`: Numeric value for the maximum allowable client-requested limit. Defaults to `None`.
* `template`: Template name for rendering pagination controls. Set to `None` to disable. Defaults to `"rest_framework/pagination/numbers.html"`.
```

----------------------------------------

TITLE: Basic APIView Example
DESCRIPTION: Demonstrates how to create a simple APIView that lists users. It includes authentication and permission checks, and returns a JSON response.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/views.md#_snippet_0

LANGUAGE: python
CODE:
```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

----------------------------------------

TITLE: Publish to PyPI
DESCRIPTION: Command to publish the package to PyPI using setup.py.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/project-management.md#_snippet_4

LANGUAGE: Shell
CODE:
```
./setup.py publish
```

----------------------------------------

TITLE: Install djangorestframework-simplejwt
DESCRIPTION: Installs the djangorestframework-simplejwt package using pip. This package provides JSON Web Token (JWT) authentication for Django REST Framework.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/authentication.md#_snippet_26

LANGUAGE: bash
CODE:
```
pip install djangorestframework-simplejwt
```

----------------------------------------

TITLE: Configuring INSTALLED_APPS
DESCRIPTION: Adds the 'rest_framework' and 'snippets' apps to the Django project's settings.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/1-serialization.md#_snippet_2

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]
```

----------------------------------------

TITLE: AcceptHeaderVersioning Example
DESCRIPTION: Demonstrates how to use the AcceptHeaderVersioning scheme by including the API version in the 'Accept' header. This is often considered a best practice for public APIs.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/versioning.md#_snippet_7

LANGUAGE: http
CODE:
```
GET /bookings/ HTTP/1.1
Host: example.com
Accept: application/json; version=1.0
```

----------------------------------------

TITLE: User Serializer Definition
DESCRIPTION: Defines a serializer for the User model using Django REST Framework's HyperlinkedModelSerializer.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/tutorial/quickstart.md#_snippet_2

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
```

----------------------------------------

TITLE: Example Usage of DRF Dynamic Fields Serializer
DESCRIPTION: This Python example demonstrates how to use the `DynamicFieldsModelSerializer`. It shows defining a `UserSerializer` that inherits from it and then initializing the serializer with and without the `fields` argument to dynamically control the output fields.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/serializers.md#_snippet_71

LANGUAGE: python
CODE:
```
>>> class UserSerializer(DynamicFieldsModelSerializer):
>>>     class Meta:
>>>         model = User
>>>         fields = ['id', 'username', 'email']
>>>
>>> print(UserSerializer(user))
{'id': 2, 'username': 'jonwatts', 'email': 'jon@example.com'}
>>>
>>> print(UserSerializer(user, fields=('id', 'email')))
{'id': 2, 'email': 'jon@example.com'}
```

----------------------------------------

TITLE: Run Tests Against Multiple Python/Django Environments with Tox
DESCRIPTION: Instructions on using the `tox` tool to execute tests across various supported Python and Django versions. This requires a global installation of `tox`.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/contributing.md#_snippet_4

LANGUAGE: shell
CODE:
```
tox
```

----------------------------------------

TITLE: HostNameVersioning Example
DESCRIPTION: Illustrates the HostNameVersioning scheme, where the API version is specified in the hostname of the URL.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/versioning.md#_snippet_13

LANGUAGE: http
CODE:
```
GET /bookings/ HTTP/1.1
Host: v1.example.com
Accept: application/json
```

----------------------------------------

TITLE: Live Testing with Requests or CoreAPI Clients
DESCRIPTION: Demonstrates how to switch WSGI client instances to actual `requests.Session` or `coreapi.Client` instances to enable test cases to make network calls against live services. This requires careful handling of setup and teardown for data isolation.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.5-announcement.md#_snippet_4

LANGUAGE: python
CODE:
```
from rest_framework.test import APIClient
import requests
import coreapi

# Example using requests.Session
client = APIClient()
client.session = requests.Session()

# Example using coreapi.Client
# client = APIClient()
# client.session = coreapi.Client()

```

----------------------------------------

TITLE: Install Schema Dependencies
DESCRIPTION: Installs the Python packages required for generating OpenAPI schemas with Django REST Framework. `pyyaml` is for YAML output, `uritemplate` for path parameter handling, and `inflection` for pluralization.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/schemas.md#_snippet_0

LANGUAGE: bash
CODE:
```
pip install pyyaml uritemplate inflection
```

----------------------------------------

TITLE: ModelRouter Registration Example
DESCRIPTION: Demonstrates registering a model with the ModelRouter provided by wq.db.rest, inferring defaults for URL prefix, serializer, and viewset.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/routers.md#_snippet_13

LANGUAGE: python
CODE:
```
from wq.db import rest
from myapp.models import MyModel

rest.router.register_model(MyModel)

```

----------------------------------------

TITLE: Fix Usage of Deprecated Django Function in Docs Example
DESCRIPTION: This change corrects an example in the documentation that used a deprecated Django function. The fix ensures that the example code is up-to-date and uses current Django best practices.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_4

LANGUAGE: python
CODE:
```
# Original (potentially deprecated) usage in docs:
# from django.utils.deprecation import deprecatd_function
# deprecatd_function()

# Corrected usage:
# (The specific replacement depends on the deprecated function)
# For example, if it was a specific setting or method:
# from django.conf import settings
# settings.NEW_SETTING = True

```

----------------------------------------

TITLE: Example Multiple Ordering Queries with OrderingFilter
DESCRIPTION: This HTTP example illustrates how to apply multiple ordering criteria by separating field names with commas, sorting first by 'account' then by 'username'.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/api-guide/filtering.md#_snippet_21

LANGUAGE: HTTP
CODE:
```
http://example.com/api/users?ordering=account,username
```

----------------------------------------

TITLE: Docstrings Code Highlighting
DESCRIPTION: Docstrings now feature code highlighting using Pygments, improving the readability of code examples within documentation.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/release-notes.md#_snippet_231

LANGUAGE: python
CODE:
```
# Docstrings now support code highlighting via Pygments.
```

----------------------------------------

TITLE: Optional Python Package Dependencies for Django REST Framework
DESCRIPTION: This snippet lists Python packages that are not strictly required for Django REST Framework but can be installed to enable additional features. For example, coreapi and coreschema are used for schema generation, django-filter for advanced filtering backends, django-guardian for object-level permissions, markdown and pygments for the browsable API, psycopg2-binary for PostgreSQL database support, and pyyaml for YAML parsing.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/requirements/requirements-optionals.txt#_snippet_0

LANGUAGE: Python
CODE:
```
coreapi==2.3.1
coreschema==0.0.4
django-filter
django-guardian>=2.4.0,<2.5
inflection==0.5.1
markdown>=3.3.7
psycopg2-binary>=2.9.5,<2.10
pygments~=2.17.0
pyyaml>=5.3.1,<5.4
```

----------------------------------------

TITLE: Read-only BaseSerializer Example
DESCRIPTION: Demonstrates how to implement a read-only serializer using `BaseSerializer` by overriding the `to_representation` method. Includes examples for serializing single and multiple model instances.

SOURCE: https://github.com/encode/django-rest-framework/blob/master/docs/community/3.0-announcement.md#_snippet_23

LANGUAGE: python
CODE:
```
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Assuming HighScore model is defined elsewhere
# class HighScore(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     player_name = models.CharField(max_length=10)
#     score = models.IntegerField()

class HighScoreSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'score': obj.score,
            'player_name': obj.player_name
        }

@api_view(['GET'])
def high_score(request, pk):
    # instance = HighScore.objects.get(pk=pk)
    # For demonstration, using a mock object
    instance = type('obj', (object,), {'score': 100, 'player_name': 'TestPlayer'})()
    serializer = HighScoreSerializer(instance)
    return Response(serializer.data)

@api_view(['GET'])
def all_high_scores(request):
    # queryset = HighScore.objects.order_by('-score')
    # For demonstration, using a mock queryset
    queryset = [type('obj', (object,), {'score': 100, 'player_name': 'TestPlayer1'})(),
                type('obj', (object,), {'score': 90, 'player_name': 'TestPlayer2'})()]
    serializer = HighScoreSerializer(queryset, many=True)
    return Response(serializer.data)
```
