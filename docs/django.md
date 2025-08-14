========================
CODE SNIPPETS
========================
TITLE: Verify Python Installation
DESCRIPTION: This snippet demonstrates how to verify a Python installation by launching the Python interpreter and checking the version. It shows the typical output seen in a Pycon session.

SOURCE: https://github.com/django/django/blob/main/docs/intro/install.txt#_snippet_0

LANGUAGE: pycon
CODE:
```
Python 3.x.y
[GCC 4.x] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

----------------------------------------

TITLE: Setup Virtual Environment and Install Dependencies
DESCRIPTION: Steps to create and activate a Python virtual environment and install project dependencies using pip.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-documentation.txt#_snippet_1

LANGUAGE: shell
CODE:
```
python -m venv .venv
source .venv/bin/activate
```

----------------------------------------

TITLE: Django App README and Quick Start
DESCRIPTION: Provides a README file for the Django polls app, including a quick start guide with instructions on adding the app to `INSTALLED_APPS`, including URLs, running migrations, and starting the development server.

SOURCE: https://github.com/django/django/blob/main/docs/intro/reusable-apps.txt#_snippet_2

LANGUAGE: rst
CODE:
```
============
django-polls
============

django-polls is a Django app to conduct web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_polls",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("polls/", include("django_polls.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a poll.

5. Visit the ``/polls/`` URL to participate in the poll.
```

----------------------------------------

TITLE: Check Git Installation and Get Help
DESCRIPTION: Verify if Git is installed on your system by running the 'git' command. If Git is not found, you will need to install it. You can also access Git's command documentation by typing 'git help'.

SOURCE: https://github.com/django/django/blob/main/docs/intro/contributing.txt#_snippet_0

LANGUAGE: bash
CODE:
```
git
```

LANGUAGE: bash
CODE:
```
git help
```

----------------------------------------

TITLE: Install Django Official Release with Pip
DESCRIPTION: Installs the latest official release of Django using pip. This is the recommended method and should be performed within a virtual environment for isolation.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_3

LANGUAGE: bash
CODE:
```
$ python -m pip install Django

```

----------------------------------------

TITLE: ldconfig Command Example
DESCRIPTION: Demonstrates the use of the `ldconfig` command on Linux platforms after installing libraries from source. This command updates the shared library cache, ensuring newly installed libraries are discoverable.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/geolibs.txt#_snippet_3

LANGUAGE: shell
CODE:
```
$ sudo make install
$ sudo ldconfig
```

----------------------------------------

TITLE: Django runserver IP and Port Examples
DESCRIPTION: Provides examples of how to start the Django development server on different IP addresses and ports, including IPv4, IPv6, and localhost configurations.

SOURCE: https://github.com/django/django/blob/main/docs/ref/django-admin.txt#_snippet_26

LANGUAGE: bash
CODE:
```
# Port 8000 on IP address 127.0.0.1
django-admin runserver

# Port 8000 on IP address 1.2.3.4
django-admin runserver 1.2.3.4:8000

# Port 7000 on IP address 127.0.0.1
django-admin runserver 7000

# Port 7000 on IP address 1.2.3.4
django-admin runserver 1.2.3.4:7000

# Port 8000 on IPv6 address ::1
django-admin runserver -6

# Port 7000 on IPv6 address ::1
django-admin runserver -6 7000

# Port 7000 on IPv6 address 2001:0db8:1234:5678::9
django-admin runserver [2001:0db8:1234:5678::9]:7000

# Port 8000 on IPv4 address of host localhost
django-admin runserver localhost:8000

# Port 8000 on IPv6 address of host localhost
django-admin runserver -6 localhost:8000
```

----------------------------------------

TITLE: Install Django Development Version (Editable)
DESCRIPTION: Installs the cloned Django development version in an editable mode using pip. This makes Django's code importable and is useful for contributing to Django or testing the latest changes.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_5

LANGUAGE: bash
CODE:
```
$ python -m pip install -e django/

```

----------------------------------------

TITLE: Install and Run Pre-commit Hooks
DESCRIPTION: Instructions for installing the pre-commit framework and its git hooks to automate code quality checks before committing. This helps catch issues early and ensures consistency.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-code/coding-style.txt#_snippet_0

LANGUAGE: shell
CODE:
```
python -m pip install pre-commit
pre-commit install
```

----------------------------------------

TITLE: Verify Django Installation
DESCRIPTION: This snippet shows how to verify that Django is installed and accessible within a Python environment. It involves importing the Django module and printing its version.

SOURCE: https://github.com/django/django/blob/main/docs/intro/install.txt#_snippet_1

LANGUAGE: python
CODE:
```
>>> import django
>>> print(django.get_version())
|version|
```

----------------------------------------

TITLE: Clone Django Development Version
DESCRIPTION: Clones the Django source code from the official GitHub repository using Git. This allows access to the latest development version for testing or contribution.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_4

LANGUAGE: bash
CODE:
```
$ git clone https://github.com/django/django.git

```

----------------------------------------

TITLE: Install GeoDjango Prerequisites with Homebrew
DESCRIPTION: Installs essential GeoDjango prerequisites on macOS using the Homebrew package manager. This includes PostgreSQL, PostGIS, GDAL, and libgeoip.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_7

LANGUAGE: shell
CODE:
```
$ brew install postgresql
$ brew install postgis
$ brew install gdal
$ brew install libgeoip
```

----------------------------------------

TITLE: Build Django HTML Documentation (Unix/macOS)
DESCRIPTION: Guides users on how to build the HTML version of the Django documentation using the provided Makefile. This process requires GNU Make and Sphinx to be installed.

SOURCE: https://github.com/django/django/blob/main/docs/intro/whatsnext.txt#_snippet_2

LANGUAGE: shell
CODE:
```
cd path/to/django/docs
make html
```

----------------------------------------

TITLE: Django Admin Utility
DESCRIPTION: The `django-admin` command-line utility is available for managing Django projects. It provides various management commands for tasks like creating projects, running the development server, and managing database migrations.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_6

LANGUAGE: Shell
CODE:
```
django-admin
```

----------------------------------------

TITLE: Python Database Bindings for Django
DESCRIPTION: Lists essential Python packages required for Django to connect to specific database servers. These bindings act as the interface between Django's ORM and the database.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_2

LANGUAGE: APIDOC
CODE:
```
Required Python Packages:
  - PostgreSQL: psycopg or psycopg2
  - MySQL/MariaDB: mysqlclient
  - Oracle: oracledb
```

----------------------------------------

TITLE: Install and Run isort for Import Sorting
DESCRIPTION: Demonstrates how to install the isort package and run it recursively to automatically sort Python imports according to specified guidelines. This tool helps maintain consistent import order.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-code/coding-style.txt#_snippet_3

LANGUAGE: console
CODE:
```
$ python -m pip install "isort >= 5.1.0"
$ isort .
```

----------------------------------------

TITLE: Django Prefetching with GenericPrefetch Example
DESCRIPTION: Illustrates the usage of GenericPrefetch for efficient querying with GenericForeignKeys, showing object creation and setup for prefetching.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/contenttypes.txt#_snippet_20

LANGUAGE: pycon
CODE:
```
>>> from django.contrib.contenttypes.prefetch import GenericPrefetch
>>> bookmark = Bookmark.objects.create(url="https://www.djangoproject.com/")
>>> animal = Animal.objects.create(name="lion", weight=100)
>>> TaggedItem.objects.create(tag="great", content_object=bookmark)
```

----------------------------------------

TITLE: Install psycopg via pip
DESCRIPTION: Installs the psycopg Python module, which provides the interface between Python and the PostgreSQL database, using pip within a virtual environment.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_12

LANGUAGE: doscon
CODE:
```
...\> py -m pip install psycopg
```

----------------------------------------

TITLE: Install binutils on Debian/Ubuntu
DESCRIPTION: Installs the binutils package, which includes objdump, a utility required by Python's ctypes for verifying shared libraries on GNU/Linux systems.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_3

LANGUAGE: shell
CODE:
```
$ sudo apt-get install binutils
```

----------------------------------------

TITLE: Install binutils on Red Hat/CentOS
DESCRIPTION: Installs the binutils package, which includes objdump, a utility required by Python's ctypes for verifying shared libraries on GNU/Linux systems.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_4

LANGUAGE: shell
CODE:
```
$ sudo yum install binutils
```

----------------------------------------

TITLE: Install uWSGI using pip
DESCRIPTION: Installs the uWSGI application server using pip. It shows how to install the current stable version or a long-term support (LTS) version from a specific URL.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/wsgi/uwsgi.txt#_snippet_0

LANGUAGE: console
CODE:
```
$ python -m pip install uwsgi

# Or install LTS (long term support).
$ python -m pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz
```

----------------------------------------

TITLE: Django Development Server Output
DESCRIPTION: Example output from the Django development server when started. It indicates system checks, migration status, Django version, and the server address.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial01.txt#_snippet_4

LANGUAGE: text
CODE:
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

|today| - 15:50:53
Django version |version|, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/|version|/howto/deployment/
```

----------------------------------------

TITLE: Install Local Django Copy
DESCRIPTION: Installs the Django project from a local clone in editable mode, allowing immediate reflection of code changes.

SOURCE: https://github.com/django/django/blob/main/docs/intro/contributing.txt#_snippet_3

LANGUAGE: Shell
CODE:
```
python -m pip install -e /path/to/your/local/clone/django/
```

----------------------------------------

TITLE: Django Client GET Request Example
DESCRIPTION: Demonstrates making a GET request using Django's test Client with query parameters and custom headers.

SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/tools.txt#_snippet_5

LANGUAGE: pycon
CODE:
```
>>> c = Client()
>>> c.get("/customers/details/", query_params={"name": "fred", "age": 7})
>>> c.get(
...     "/customers/details/",
...     query_params={"name": "fred", "age": 7},
...     headers={"accept": "application/json"},
... )
```

----------------------------------------

TITLE: Install GeoDjango Prerequisites with MacPorts
DESCRIPTION: Installs essential GeoDjango prerequisites on macOS using the MacPorts package manager. This includes specific versions of PostgreSQL, GEOS, PROJ, PostGIS, GDAL, and libgeoip.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_8

LANGUAGE: shell
CODE:
```
$ sudo port install postgresql14-server
$ sudo port install geos
$ sudo port install proj6
$ sudo port install postgis3
$ sudo port install gdal
$ sudo port install libgeoip
```

----------------------------------------

TITLE: Get Homebrew Prefix Path
DESCRIPTION: Retrieves the installation prefix path for Homebrew packages on macOS. This path is used to construct the full path to the SpatiaLite library.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/spatialite.txt#_snippet_6

LANGUAGE: console
CODE:
```
$ brew --prefix
```

----------------------------------------

TITLE: Django Basic Test Client Example
DESCRIPTION: A fundamental example of using Django's `Client` within a `unittest.TestCase`. It shows how to instantiate the client, make a GET request to a URL, and assert the HTTP status code and context data of the response.

SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/tools.txt#_snippet_30

LANGUAGE: python
CODE:
```
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get("/customer/details/")

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context["customers"]), 5)
```

----------------------------------------

TITLE: Install ReportLab using pip
DESCRIPTION: Installs the ReportLab library, a powerful Python PDF generation toolkit, using the pip package installer. Ensure Python and pip are correctly set up on your system before running this command.

SOURCE: https://github.com/django/django/blob/main/docs/howto/outputting-pdf.txt#_snippet_0

LANGUAGE: console
CODE:
```
$ python -m pip install reportlab
```

----------------------------------------

TITLE: Django URL Configuration Example
DESCRIPTION: Illustrates a basic URL pattern configuration in Django, mapping a URL prefix to an admin site's URLs. This is a common setup in Django projects.

SOURCE: https://github.com/django/django/blob/main/docs/releases/1.9.txt#_snippet_109

LANGUAGE: python
CODE:
```
url(r"^admin/", admin.site.urls),
```

----------------------------------------

TITLE: GEOS Build and Install from Source
DESCRIPTION: Provides instructions for building and installing the GEOS library from source on UNIX-like systems. This involves downloading the source, configuring the build using CMake, compiling, and installing the library.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/geolibs.txt#_snippet_1

LANGUAGE: shell
CODE:
```
wget https://download.osgeo.org/geos/geos-X.Y.Z.tar.bz2
tar xjf geos-X.Y.Z.tar.bz2
cd geos-X.Y.Z
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
sudo cmake --build . --target install
```

----------------------------------------

TITLE: Django Database Backend Settings
DESCRIPTION: Specifies the database engine to be used by Django. This setting determines which database adapter Django will utilize for interacting with your database server.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_0

LANGUAGE: APIDOC
CODE:
```
DATABASES['default']['ENGINE']:
  - 'django.db.backends.sqlite3'
  - 'django.db.backends.postgresql'
  - 'django.db.backends.mysql'
  - 'django.db.backends.oracle'
  - Other backends are also available via third-party packages.
```

----------------------------------------

TITLE: Running Django Shell
DESCRIPTION: Demonstrates how to start the Django management shell in different console environments.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-documentation.txt#_snippet_16

LANGUAGE: console
CODE:
```
$ python manage.py shell
```

LANGUAGE: doscon
CODE:
```
...\> py manage.py shell
```

----------------------------------------

TITLE: Install Documentation Dependencies
DESCRIPTION: Installs the necessary Python packages for building the Django documentation from the requirements file. This is a prerequisite for local documentation building.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-documentation.txt#_snippet_2

LANGUAGE: bash
CODE:
```
python -m pip install -r docs/requirements.txt
```

----------------------------------------

TITLE: Django TestCase Example
DESCRIPTION: Demonstrates writing a test case using Django's `TestCase` class, which inherits from `unittest.TestCase`. It includes a `setUp` method for test data initialization and a test method to verify model behavior. This approach ensures each test runs in a clean database transaction.

SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/overview.txt#_snippet_0

LANGUAGE: python
CODE:
```
from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
```

----------------------------------------

TITLE: Django View Example Usage
DESCRIPTION: Demonstrates how to implement a simple Django view by inheriting from the base `View` class and defining a `get` method. Includes examples for both `views.py` and `urls.py`.

SOURCE: https://github.com/django/django/blob/main/docs/ref/class-based-views/base.txt#_snippet_1

LANGUAGE: Python
CODE:
```
from django.http import HttpResponse
from django.views import View


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
```

LANGUAGE: Python
CODE:
```
from django.urls import path

from myapp.views import MyView

urlpatterns = [
    path("mine/", MyView.as_view(), name="my-view"),
]
```

----------------------------------------

TITLE: Django Console Directive for Command Examples
DESCRIPTION: Explains the custom 'console' directive in Django documentation for presenting command-line examples, which supports both Unix and Windows prompts.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-documentation.txt#_snippet_15

LANGUAGE: rst
CODE:
```
Django's documentation uses a custom ``console`` directive for documenting command-line examples involving ``django-admin``, ``manage.py``, ``python``, etc.). In the HTML documentation, it renders a two-tab UI, with one tab showing a Unix-style command prompt and a second tab showing a Windows prompt.

For example, you can replace this fragment:

.. code-block:: rst

    use this command:

    .. code-block:: console

        $ python manage.py shell

with this one:

.. code-block:: rst

    use this command:

    .. console::

        $ python manage.py shell

Notice two things:

* You usually will replace occurrences of the ``.. code-block:: console`` directive.
* You don't need to change the actual content of the code example. You still write it assuming a Unix-y environment (i.e. a ``'$'`` prompt symbol,
```

----------------------------------------

TITLE: Build PROJ with CMake
DESCRIPTION: Builds and installs the PROJ library using CMake. This involves creating a build directory, configuring the build, and then executing the build and install commands.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/geolibs.txt#_snippet_7

LANGUAGE: shell
CODE:
```
$ cd proj-X.Y.Z
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
$ sudo cmake --build . --target install
```

----------------------------------------

TITLE: Django Test Setup Databases Keyword-Only Arguments
DESCRIPTION: Keyword arguments to setup_databases are now keyword-only.

SOURCE: https://github.com/django/django/blob/main/docs/releases/3.2.txt#_snippet_83

LANGUAGE: APIDOC
CODE:
```
django.test.utils.setup_databases
  Parameters:
    *args, **options
  Behavior Change:
    All keyword arguments passed to this function are now keyword-only.
  Impact:
    This enforces clearer usage and prevents potential argument misinterpretation, especially as the function evolves.
  Example:
    # Correct usage:
    setup_databases(verbosity=1, keepdb=True)
    # Incorrect usage (will raise TypeError):
    # setup_databases(1, True)
```

----------------------------------------

TITLE: Django DATABASES Configuration Example
DESCRIPTION: An example of a Django settings dictionary defining multiple databases. This configuration includes a 'default' database, an 'auth_db' for authentication and contenttypes apps, and a primary/replica setup ('primary', 'replica1', 'replica2') for other applications.

SOURCE: https://github.com/django/django/blob/main/docs/topics/db/multi-db.txt#_snippet_6

LANGUAGE: python
CODE:
```
DATABASES = {
    "default": {},
    "auth_db": {
        "NAME": "auth_db_name",
        "ENGINE": "django.db.backends.mysql",
        "USER": "mysql_user",
        "PASSWORD": "swordfish",
    },
    "primary": {
        "NAME": "primary_name",
        "ENGINE": "django.db.backends.mysql",
        "USER": "mysql_user",
        "PASSWORD": "spam",
    },
    "replica1": {
        "NAME": "replica1_name",
        "ENGINE": "django.db.backends.mysql",
        "USER": "mysql_user",
        "PASSWORD": "eggs",
    },
    "replica2": {
        "NAME": "replica2_name",
        "ENGINE": "django.db.backends.mysql",
        "USER": "mysql_user",
        "PASSWORD": "bacon",
    },
}
```

----------------------------------------

TITLE: Start Development Server Command
DESCRIPTION: Command to start the Django development server. This allows you to access your site, including the admin interface, locally.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial02.txt#_snippet_17

LANGUAGE: shell
CODE:
```
$ python manage.py runserver

```

----------------------------------------

TITLE: Example uWSGI INI configuration
DESCRIPTION: An example INI file for configuring the uWSGI server. This file specifies essential settings like the project directory, WSGI module, master process, PID file, and daemonization.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/wsgi/uwsgi.txt#_snippet_2

LANGUAGE: ini
CODE:
```
[uwsgi]
chdir=/path/to/your/project
module=mysite.wsgi:application
master=True
pidfile=/tmp/project-master.pid
vacuum=True
max-requests=5000
daemonize=/var/log/uwsgi/yourproject.log
```

----------------------------------------

TITLE: GeoDjango Test Settings Example
DESCRIPTION: An example bare-bones Django settings file configured with PostGIS spatial backends for both 'default' and 'other' databases. This setup allows the execution of the entire Django test suite, including GeoDjango specific tests.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/testing.txt#_snippet_5

LANGUAGE: python
CODE:
```
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "geodjango",
        "USER": "geodjango",
    },
    "other": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "other",
        "USER": "geodjango",
    },
}

SECRET_KEY = "django_tests_secret_key"
```

----------------------------------------

TITLE: Configure PATH and Library Path for MacPorts
DESCRIPTION: Sets up the PATH environment variable to access MacPorts executables and configures DYLD_FALLBACK_LIBRARY_PATH for library discovery on macOS.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_9

LANGUAGE: shell
CODE:
```
export PATH=/opt/local/bin:/opt/local/lib/postgresql14/bin
export DYLD_FALLBACK_LIBRARY_PATH=/opt/local/lib:$DYLD_FALLBACK_LIBRARY_PATH
```

----------------------------------------

TITLE: Create Django Project
DESCRIPTION: Command to bootstrap a new Django project named 'mysite' within a directory called 'djangotutorial'. This command generates the initial project structure and configuration files.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial01.txt#_snippet_1

LANGUAGE: bash
CODE:
```
$ django-admin startproject mysite djangotutorial
```

----------------------------------------

TITLE: Install Colorama for Colored Output
DESCRIPTION: Installs the 'colorama' library, which is required for colored terminal output on older Windows versions or legacy terminals. It ensures syntax coloring works correctly.

SOURCE: https://github.com/django/django/blob/main/docs/howto/windows.txt#_snippet_4

LANGUAGE: doscon
CODE:
```
...\> py -m pip install "colorama >= 0.4.6"
```

----------------------------------------

TITLE: Install Hypercorn
DESCRIPTION: Installs the Hypercorn ASGI server using pip. This is a prerequisite for running Django with Hypercorn.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/asgi/hypercorn.txt#_snippet_0

LANGUAGE: shell
CODE:
```
python -m pip install hypercorn
```

----------------------------------------

TITLE: Install Release Dependencies
DESCRIPTION: Installs the necessary Python packages (`build`, `twine`) required for creating and uploading release artifacts to PyPI.

SOURCE: https://github.com/django/django/blob/main/docs/internals/howto-release-django.txt#_snippet_0

LANGUAGE: shell
CODE:
```
python -m pip install build twine
```

----------------------------------------

TITLE: Django startproject Management Command
DESCRIPTION: The `startproject` management command in Django automatically sets up a default ASGI configuration for new projects. This includes creating the `asgi.py` file and configuring basic settings.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/asgi/index.txt#_snippet_3

LANGUAGE: bash
CODE:
```
django-admin startproject myproject
```

LANGUAGE: APIDOC
CODE:
```
djadmin:startproject
  - Creates a new Django project.
  - Sets up default ASGI configuration in `asgi.py`.
  - Initializes project structure and essential files.
```

----------------------------------------

TITLE: Update Django Source Code with Git
DESCRIPTION: To update your local copy of the Django source code, navigate to the `django` directory and execute the `git pull` command. This command downloads any changes from the remote repository.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_7

LANGUAGE: Shell
CODE:
```
git pull
```

----------------------------------------

TITLE: Run Django Development Server
DESCRIPTION: Starts the Django development server for local testing. This command is essential for previewing your project's changes and verifying URL routing and view functionality.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial01.txt#_snippet_9

LANGUAGE: bash
CODE:
```
$ python manage.py runserver
```

----------------------------------------

TITLE: Start uWSGI server for Django
DESCRIPTION: Starts a uWSGI server process for a Django project. This command configures the working directory, WSGI module, environment variables, socket, worker processes, and logging.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/wsgi/uwsgi.txt#_snippet_1

LANGUAGE: shell
CODE:
```
uwsgi --chdir=/path/to/your/project \
    --module=mysite.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=mysite.settings \
    --master --pidfile=/tmp/project-master.pid \
    --socket=127.0.0.1:49152 \
    --processes=5 \
    --uid=1000 --gid=2000 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum \
    --home=/path/to/virtual/env \
    --daemonize=/var/log/uwsgi/yourproject.log
```

----------------------------------------

TITLE: Install Jinja2 Template Engine (Console)
DESCRIPTION: Installs the Jinja2 templating engine, a prerequisite for using Django's Jinja2 backend. Ensure you have Python and pip installed.

SOURCE: https://github.com/django/django/blob/main/docs/topics/templates.txt#_snippet_17

LANGUAGE: console
CODE:
```
$ python -m pip install Jinja2
```

----------------------------------------

TITLE: QuerySet.explain() with Options Example
DESCRIPTION: Shows how to use additional parameters like 'verbose' and 'analyze' with the explain() method to get more detailed execution plan information, which may have side effects on some databases.

SOURCE: https://github.com/django/django/blob/main/docs/ref/models/querysets.txt#_snippet_102

LANGUAGE: python
CODE:
```
print(Blog.objects.filter(title="My Blog").explain(verbose=True, analyze=True))
```

----------------------------------------

TITLE: Run Django Development Server
DESCRIPTION: Starts Django's lightweight development server. This command is intended for development and testing purposes only and is not suitable for production deployments.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/index.txt#_snippet_0

LANGUAGE: CLI
CODE:
```
djadmin runserver
```

----------------------------------------

TITLE: Install Django Flatpages App
DESCRIPTION: Steps to install the flatpages app, including adding it to INSTALLED_APPS and configuring SITE_ID. It also requires running database migrations.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/flatpages.txt#_snippet_0

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    # ...
    'django.contrib.sites',
    'django.contrib.flatpages',
    # ...
]

SITE_ID = 1

# After adding to settings, run migrations:
# python manage.py migrate
```

----------------------------------------

TITLE: Install Sphinx Documentation Generator
DESCRIPTION: Installs the Sphinx documentation system using pip. This is a prerequisite for building the project's documentation.

SOURCE: https://github.com/django/django/blob/main/docs/README.rst#_snippet_0

LANGUAGE: python
CODE:
```
python -m pip install Sphinx
```

----------------------------------------

TITLE: Deploy Django with Gunicorn and Uvicorn Worker
DESCRIPTION: Starts Gunicorn using the Uvicorn worker class to run a Django ASGI application. This setup is recommended for production environments.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/asgi/uvicorn.txt#_snippet_3

LANGUAGE: shell
CODE:
```
python -m gunicorn myproject.asgi:application -k uvicorn_worker.UvicornWorker
```

----------------------------------------

TITLE: Django SQLite Database Name Configuration
DESCRIPTION: Defines the name or path for the SQLite database file. When using SQLite, this should be the full absolute path to the database file, which Django will create if it doesn't exist.

SOURCE: https://github.com/django/django/blob/main/docs/topics/install.txt#_snippet_1

LANGUAGE: APIDOC
CODE:
```
DATABASES['default']['NAME']:
  - For SQLite: The full absolute path to the database file (e.g., BASE_DIR / 'db.sqlite3').
  - Django creates the file automatically if it doesn't exist.
```

----------------------------------------

TITLE: Configure, Build, and Install SpatiaLite
DESCRIPTION: Configures, builds, and installs the SpatiaLite library from source. For macOS, use the --target=macosx option during configuration.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/spatialite.txt#_snippet_4

LANGUAGE: shell
CODE:
```
$ ./configure
$ make
$ sudo make install
```

----------------------------------------

TITLE: Run Django Test Suite
DESCRIPTION: Commands to navigate to the Django tests directory, install necessary test dependencies, and execute the main test suite script.

SOURCE: https://github.com/django/django/blob/main/docs/intro/contributing.txt#_snippet_4

LANGUAGE: Shell
CODE:
```
cd tests
```

LANGUAGE: Shell
CODE:
```
python -m pip install -r requirements/py3.txt
```

LANGUAGE: Shell
CODE:
```
./runtests.py
```

----------------------------------------

TITLE: Install Django App Locally
DESCRIPTION: This shell command installs the built Django application package locally using pip. It installs the package from the generated tarball, making it available for use in your project.

SOURCE: https://github.com/django/django/blob/main/docs/intro/reusable-apps.txt#_snippet_7

LANGUAGE: shell
CODE:
```
python -m pip install --user django-polls/dist/django_polls-0.1.tar.gz
```

----------------------------------------

TITLE: Install Django using pip
DESCRIPTION: Installs the latest version of the Django web framework using pip, the Python package installer. This command should be run within an activated virtual environment.

SOURCE: https://github.com/django/django/blob/main/docs/howto/windows.txt#_snippet_3

LANGUAGE: doscon
CODE:
```
...\> py -m pip install Django
```

----------------------------------------

TITLE: Install Sphinx for Django Docs
DESCRIPTION: Instructions for installing the Sphinx documentation generator, a key dependency for building HTML versions of the Django documentation. It can be installed using pip.

SOURCE: https://github.com/django/django/blob/main/docs/intro/whatsnext.txt#_snippet_1

LANGUAGE: python
CODE:
```
python -m pip install Sphinx
```

----------------------------------------

TITLE: Configure PATH for Postgres.app on macOS
DESCRIPTION: Adds the Postgres.app's bin directory to the PATH environment variable in .bash_profile, allowing command-line execution of PostgreSQL programs. Replace X.Y with the actual version number.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_6

LANGUAGE: bash
CODE:
```
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/X.Y/bin
```

----------------------------------------

TITLE: Find Django Installation Path
DESCRIPTION: This console command helps locate the installation path of the Django project on your system, which is useful for finding default template files or source code.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial07.txt#_snippet_11

LANGUAGE: console
CODE:
```
$ python -c "import django; print(django.__path__)"
```

----------------------------------------

TITLE: Database Session Setup
DESCRIPTION: For database-backed sessions, ensure 'django.contrib.sessions' is in INSTALLED_APPS and run the 'migrate' command to create the necessary session table. This is the default and most common setup.

SOURCE: https://github.com/django/django/blob/main/docs/topics/http/sessions.txt#_snippet_2

LANGUAGE: bash
CODE:
```
python manage.py migrate
```

----------------------------------------

TITLE: Update PATH for macOS Python
DESCRIPTION: Modifies the PATH environment variable in the .profile file to ensure the newly installed Python version is used when 'python' is entered at the command line.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_5

LANGUAGE: shell
CODE:
```
export PATH=/Library/Frameworks/Python.framework/Versions/Current/bin:$PATH
```

----------------------------------------

TITLE: Get Item GUID - Django Feed Generator
DESCRIPTION: Specifies how to generate a unique identifier (GUID) for a feed item. This method takes an item object and should return the item's ID. If not provided, the item's link is used as the default GUID.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/syndication.txt#_snippet_32

LANGUAGE: Python
CODE:
```
def item_guid(self, obj):
    """
    Takes an item, as return by items(), and returns the item's ID.
    """
    pass
```

----------------------------------------

TITLE: Basic Settings Configuration Example
DESCRIPTION: A simple example demonstrating how to manually configure Django's `DEBUG` setting to `True` using `settings.configure()`.

SOURCE: https://github.com/django/django/blob/main/docs/topics/settings.txt#_snippet_11

LANGUAGE: python
CODE:
```
from django.conf import settings

settings.configure(DEBUG=True)

# Now you can access settings
print(f"DEBUG is: {settings.DEBUG}")
```

----------------------------------------

TITLE: Python: Safely Initialize Django with django.setup()
DESCRIPTION: Demonstrates the correct way to call `django.setup()` in a standalone Python script to initialize Django settings and applications. This function should only be called once to avoid errors, typically within an `if __name__ == "__main__":` block.

SOURCE: https://github.com/django/django/blob/main/docs/topics/settings.txt#_snippet_13

LANGUAGE: python
CODE:
```
import django

if __name__ == "__main__":
    django.setup()
```

----------------------------------------

TITLE: Configure Linux Library Path
DESCRIPTION: Adds a custom library path to ld.so.conf and updates the shared library cache on GNU/Linux systems. This ensures newly installed libraries are discoverable by the system.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_1

LANGUAGE: shell
CODE:
```
$ sudo echo /usr/local/lib >> /etc/ld.so.conf
$ sudo ldconfig
```

----------------------------------------

TITLE: Check Django Version
DESCRIPTION: Command to check the installed Django version. This helps verify the installation and identify the version being used for the tutorial.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial01.txt#_snippet_0

LANGUAGE: bash
CODE:
```
$ python -m django --version
```

----------------------------------------

TITLE: Create and Activate Virtual Environment
DESCRIPTION: Steps to create a Python virtual environment for isolating project dependencies and then activate it for use. Includes commands for Linux/macOS and Windows.

SOURCE: https://github.com/django/django/blob/main/docs/intro/contributing.txt#_snippet_2

LANGUAGE: Shell
CODE:
```
python3 -m venv ~/.virtualenvs/djangodev
```

LANGUAGE: Shell
CODE:
```
source ~/.virtualenvs/djangodev/bin/activate
```

LANGUAGE: Shell
CODE:
```
. ~/.virtualenvs/djangodev/bin/activate
```

LANGUAGE: Batch
CODE:
```
%HOMEPATH%\.virtualenvs\djangodev\Scripts\activate.bat
```

----------------------------------------

TITLE: Class-Based View Setup Method
DESCRIPTION: Demonstrates the structure of a Django class-based view that can be tested by manually calling its `setup` method. The `setup` method is crucial for initializing the view instance with a request object before calling other methods like `get_context_data`.

SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/advanced.txt#_snippet_3

LANGUAGE: python
CODE:
```
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        kwargs["environment"] = "Production"
        return super().get_context_data(**kwargs)
```

----------------------------------------

TITLE: Django: Class-Based View Request Lifecycle
DESCRIPTION: Details the core methods involved in processing a request with a Django class-based view. This includes the `as_view()` entry point, `setup()` for initialization, `dispatch()` for method routing, and the specific HTTP method handlers (e.g., `get`, `post`).

SOURCE: https://github.com/django/django/blob/main/docs/topics/class-based-views/intro.txt#_snippet_3

LANGUAGE: apidoc
CODE:
```
View.as_view():
  - Class method that returns a callable function.
  - This function is passed to the URL resolver.
  - Internally, it creates an instance of the view class.
  - Calls `setup()` on the instance.
  - Calls `dispatch()` on the instance.

View.setup(request):
  - Initializes the view instance with the request object.
  - Sets `self.request` and `self.args`, `self.kwargs`.

View.dispatch(request, *args, **kwargs):
  - Determines the HTTP request method (e.g., 'GET', 'POST').
  - Calls the corresponding method (e.g., `get(request, *args, **kwargs)`).
  - If no matching method is found, raises `HttpResponseNotAllowed`.

HTTP Method Handlers (e.g., get, post, put, delete):
  - Instance methods that contain the actual view logic for specific HTTP methods.
  - Must return an `HttpResponse` object.
  - Example: `def get(self, request, *args, **kwargs):`

HttpResponseNotAllowed:
  - Exception raised by `dispatch` when a request method does not have a corresponding handler method in the view class.
```

----------------------------------------

TITLE: Run Django Development Server
DESCRIPTION: Command to start the Django development server. This command is used to test your project locally during development. It provides feedback on system checks and server status.

SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial01.txt#_snippet_3

LANGUAGE: bash
CODE:
```
$ python manage.py runserver
```

----------------------------------------

TITLE: Create Django Project
DESCRIPTION: Initializes a new Django project using the django-admin command-line utility. This command creates the basic directory structure and configuration files for a Django project.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/tutorial.txt#_snippet_0

LANGUAGE: shell
CODE:
```
django-admin startproject geodjango
```

----------------------------------------

TITLE: Install Geospatial Libraries on Debian/Ubuntu
DESCRIPTION: Installs essential geospatial libraries for GeoDjango on Debian/Ubuntu systems using the `apt-get` package manager. This command ensures that the necessary binutils, PROJ development files, and GDAL binaries are available.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/geolibs.txt#_snippet_0

LANGUAGE: console
CODE:
```
$ sudo apt-get install binutils libproj-dev gdal-bin
```

----------------------------------------

TITLE: Activate Virtual Environment (Windows)
DESCRIPTION: Activates the previously created virtual environment. Once activated, the prompt will indicate the active environment, and installed packages will be specific to it.

SOURCE: https://github.com/django/django/blob/main/docs/howto/windows.txt#_snippet_2

LANGUAGE: doscon
CODE:
```
...\> project-name\Scripts\activate.bat
```

----------------------------------------

TITLE: QUnit Test Module Example
DESCRIPTION: Demonstrates how to write a QUnit test module for Django's JavaScript. It includes setup with `beforeEach` and assertions for testing button click behavior using `removeOnClick` and `copyOnClick` functions. It utilizes `django.jQuery` for DOM manipulation.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-code/javascript.txt#_snippet_0

LANGUAGE: javascript
CODE:
```
QUnit.module('magicTricks', {
    beforeEach: function() {
        const $ = django.jQuery;
        $('#qunit-fixture').append('<button class="button"></button>');
    }
});

QUnit.test('removeOnClick removes button on click', function(assert) {
    const $ = django.jQuery;
    removeOnClick('.button');
    assert.equal($('.button').length, 1);
    $('.button').click();
    assert.equal($('.button').length, 0);
});

QUnit.test('copyOnClick adds button on click', function(assert) {
    const $ = django.jQuery;
    copyOnClick('.button');
    assert.equal($('.button').length, 1);
    $('.button').click();
    assert.equal($('.button').length, 2);
});
```

----------------------------------------

TITLE: Django ORM: Interactive Example - Spanning Relationships
DESCRIPTION: Provides an interactive Python console (pycon) example demonstrating the difference between single and chained filter calls when spanning multi-valued relationships, including setup and expected query results.

SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_27

LANGUAGE: pycon
CODE:
```
>>> from datetime import date
>>> beatles = Blog.objects.create(name="Beatles Blog")
>>> pop = Blog.objects.create(name="Pop Music Blog")
>>> Entry.objects.create(
...     blog=beatles,
...     headline="New Lennon Biography",
...     pub_date=date(2008, 6, 1),
... )
<Entry: New Lennon Biography>
>>> Entry.objects.create(
...     blog=beatles,
...     headline="New Lennon Biography in Paperback",
...     pub_date=date(2009, 6, 1),
... )
<Entry: New Lennon Biography in Paperback>
>>> Entry.objects.create(
...     blog=pop,
...     headline="Best Albums of 2008",
...     pub_date=date(2008, 12, 15),
... )
<Entry: Best Albums of 2008>
>>> Entry.objects.create(
...     blog=pop,
...     headline="Lennon Would Have Loved Hip Hop",
...     pub_date=date(2020, 4, 1),
... )
<Entry: Lennon Would Have Loved Hip Hop>
>>> Blog.objects.filter(
...     entry__headline__contains="Lennon",
...     entry__pub_date__year=2008,
... )
<QuerySet [<Blog: Beatles Blog>]>
>>> Blog.objects.filter(
...     entry__headline__contains="Lennon",
... ).filter(
...     entry__pub_date__year=2008,
... )
<QuerySet [<Blog: Beatles Blog>, <Blog: Beatles Blog>, <Blog: Pop Music Blog>]>
```

----------------------------------------

TITLE: Configure, Build, and Install SQLite with R*Tree
DESCRIPTION: Configures the SQLite build with the R*Tree module enabled using CFLAGS, compiles it, and installs the library. This step is crucial if the system's SQLite lacks R*Tree support.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/spatialite.txt#_snippet_2

LANGUAGE: shell
CODE:
```
$ CFLAGS="-DSQLITE_ENABLE_RTREE=1" ./configure
$ make
$ sudo make install
$ cd ..
```

----------------------------------------

TITLE: Install Dependencies and Run Tests
DESCRIPTION: Ensures test requirements are up-to-date by installing npm packages and then executes the test suite using npm.

SOURCE: https://github.com/django/django/blob/main/docs/internals/contributing/writing-code/unit-tests.txt#_snippet_7

LANGUAGE: shell
CODE:
```
npm install && npm test
```

----------------------------------------

TITLE: Install Daphne (Shell)
DESCRIPTION: Installs the Daphne ASGI server using pip. This command is executed in a shell environment.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/asgi/daphne.txt#_snippet_0

LANGUAGE: shell
CODE:
```
python -m pip install daphne
```

----------------------------------------

TITLE: Install Uvicorn with Pip
DESCRIPTION: Installs the Uvicorn ASGI server using pip. This is the first step to using Uvicorn with Python applications.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/asgi/uvicorn.txt#_snippet_0

LANGUAGE: shell
CODE:
```
python -m pip install uvicorn
```

----------------------------------------

TITLE: Set LD_LIBRARY_PATH Environment Variable
DESCRIPTION: This snippet demonstrates how to set the LD_LIBRARY_PATH environment variable in a bash profile. This is crucial for the operating system to locate external shared libraries required by GeoDjango, especially when they are installed from source in non-standard directories like /usr/local/lib.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_0

LANGUAGE: shell
CODE:
```
export LD_LIBRARY_PATH=/usr/local/lib
```

----------------------------------------

TITLE: Configure Windows Environment Variables for GeoDjango
DESCRIPTION: Sets up essential Windows environment variables (OSGEO4W_ROOT, GDAL_DATA, PROJ_LIB, PATH) required for GeoDjango to function correctly. Administrator privileges are needed, and a system restart or logout/login is recommended for changes to take effect.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/install/index.txt#_snippet_11

LANGUAGE: bat
CODE:
```
set OSGEO4W_ROOT=C:\OSGeo4W
set GDAL_DATA=%OSGEO4W_ROOT%\apps\gdal\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"
```

----------------------------------------

TITLE: Configure HTTP Proxy
DESCRIPTION: Sets environment variables for HTTP proxy configuration in the command prompt. This is necessary when installing packages behind a proxy server to avoid connection issues.

SOURCE: https://github.com/django/django/blob/main/docs/howto/windows.txt#_snippet_5

LANGUAGE: doscon
CODE:
```
...\> set http_proxy=http://username:password@proxyserver:proxyport
```

----------------------------------------

TITLE: Verify Python Installation
DESCRIPTION: Checks if Python is installed and accessible from the command prompt. This command is crucial after installing Python to ensure the environment is set up correctly.

SOURCE: https://github.com/django/django/blob/main/docs/howto/windows.txt#_snippet_0

LANGUAGE: doscon
CODE:
```
...\> py --version
```

----------------------------------------

TITLE: Django Test Case setUp() Method
DESCRIPTION: The setUp() method is a standard part of Python's unittest framework, often used in Django tests to prepare the test environment before each test method runs. It's typically overridden to set up common objects or data needed for tests.

SOURCE: https://github.com/django/django/blob/main/docs/releases/1.2.5.txt#_snippet_3

LANGUAGE: Python
CODE:
```
def setUp(self):
    # Setup code here
```

----------------------------------------

TITLE: WKBWriter.write_hex() Example
DESCRIPTION: Shows how to use WKBWriter.write_hex() to get the Well-Known Binary representation of a Point geometry as a hexadecimal string.

SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/gis/geos.txt#_snippet_40

LANGUAGE: pycon
CODE:
```
>>> from django.contrib.gis.geos import Point, WKBWriter
>>> pnt = Point(1, 1)
>>> wkb_w = WKBWriter()
>>> wkb_w.write_hex(pnt)
'0101000000000000000000F03F000000000000F03F'
```

----------------------------------------

TITLE: RequestFactory Usage Example
DESCRIPTION: This example demonstrates how to use Django's RequestFactory to create a GET request, simulate a logged-in user by setting the request.user attribute, and then pass this request to a view function or class-based view. It highlights the need to manually set user attributes as middleware is not supported.

SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/advanced.txt#_snippet_1

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import MyView, my_view


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get("/customer/details")

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = my_view(request)
        # Use this syntax for class-based views.
        response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 200)
```

----------------------------------------

TITLE: Install Uvicorn and Gunicorn
DESCRIPTION: Installs Uvicorn, the Uvicorn worker, and Gunicorn. This is necessary for deploying Django with Uvicorn in a production environment managed by Gunicorn.

SOURCE: https://github.com/django/django/blob/main/docs/howto/deployment/asgi/uvicorn.txt#_snippet_2

LANGUAGE: shell
CODE:
```
python -m pip install uvicorn uvicorn-worker gunicorn
```

----------------------------------------

TITLE: Django Client GET Method Documentation
DESCRIPTION: Details the `Client.get()` method for making GET requests in Django tests. It covers parameter handling (query_params, headers, extra), redirect following, secure request emulation, and provides examples of constructing requests and interpreting responses, including redirect chains.

SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/tools.txt#_snippet_3

LANGUAGE: APIDOC
CODE:
```
Client.get(path, data=None, follow=False, secure=False, *, headers=None, query_params=None, **extra)

  Makes a GET request on the provided ``path`` and returns a ``Response`` object.

  Parameters:
    - path: The URL path to request.
    - data: Optional dictionary for GET arguments (less preferred than query_params).
    - follow: If True, follows redirects. The ``redirect_chain`` attribute on the response will contain intermediate URLs and status codes.
    - secure: If True, emulates an HTTPS request.
    - headers: Dictionary of HTTP headers to send with the request (e.g., {"accept": "application/json"}).
    - query_params: Dictionary of key-value pairs to be used for query strings (e.g., {"name": "fred", "age": 7}).
    - **extra: Arbitrary keyword arguments set WSGI environ variables (e.g., SCRIPT_NAME="/app/").

  Returns:
    A ``Response`` object.

  Examples:
    >>> c = Client()
    >>> c.get("/customers/details/", query_params={"name": "fred", "age": 7})
    >>> c.get("/", SCRIPT_NAME="/app/")
    >>> response = c.get("/redirect_me/", follow=True)
    >>> response.redirect_chain
    [('http://testserver/next/', 302), ('http://testserver/final/', 302)]
```

----------------------------------------

TITLE: Django Settings Module Example
DESCRIPTION: Illustrates the expected format for the DJANGO_SETTINGS_MODULE environment variable, which should point to a fully-qualified Python module.

SOURCE: https://github.com/django/django/blob/main/docs/faq/usage.txt#_snippet_0

LANGUAGE: python
CODE:
```
mysite.settings
```
