========================
CODE SNIPPETS
========================
TITLE: Install markdown-toc Dependency using npm
DESCRIPTION: This command installs the 'markdown-toc' package using the npm package manager. This package is a required dependency for the 'update_toc.py' script, which uses it internally to generate the table of contents.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/tools/README.md#_snippet_0

LANGUAGE: Shell
CODE:
```
npm install markdown-toc
```

----------------------------------------

TITLE: Raising Django Http404 - Python
DESCRIPTION: An example function demonstrating raising Django's `Http404` exception, typically used when an object is not found. The custom handler translates this.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_64

LANGUAGE: python
CODE:
```
from django.http import Http404

def some_service():
    raise Http404()
```

----------------------------------------

TITLE: Defining File Direct Upload Service Class in Django Python
DESCRIPTION: This class defines a service for managing the direct file upload flow, acting as a namespace for related operations like `start` and `finish`. The `start` method creates the file object and generates necessary upload data (presigned S3 URL or local URL), while the `finish` method marks the upload as complete. Both methods are wrapped in `@transaction.atomic` for data consistency. Requires `BaseUser`, `File`, `settings`, `FileUploadStorage`, `s3_generate_presigned_post`, `file_generate_local_upload_url`, `file_generate_name`, `file_generate_upload_path`, and `timezone`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_13

LANGUAGE: python
CODE:
```
# https://github.com/HackSoftware/Django-Styleguide-Example/blob/master/styleguide_example/files/services.py


class FileDirectUploadService:
    """
    This also serves as an example of a service class,
    which encapsulates a flow (start & finish) + one-off action (upload_local) into a namespace.

    Meaning, we use the class here for:

    1. The namespace
    """
    def __init__(self, user: BaseUser):
        self.user = user

    @transaction.atomic
    def start(self, *, file_name: str, file_type: str) -> Dict[str, Any]:
        file = File(
            original_file_name=file_name,
            file_name=file_generate_name(file_name),
            file_type=file_type,
            uploaded_by=self.user,
            file=None
        )
        file.full_clean()
        file.save()

        upload_path = file_generate_upload_path(file, file.file_name)

        """
        We are doing this in order to have an associated file for the field.
        """
        file.file = file.file.field.attr_class(file, file.file.field, upload_path)
        file.save()

        presigned_data: Dict[str, Any] = {}

        if settings.FILE_UPLOAD_STORAGE == FileUploadStorage.S3:
            presigned_data = s3_generate_presigned_post(
                file_path=upload_path, file_type=file.file_type
            )

        else:
            presigned_data = {
                "url": file_generate_local_upload_url(file_id=str(file.id)),
            }

        return {"id": file.id, **presigned_data}

    @transaction.atomic
    def finish(self, *, file: File) -> File:
        # Potentially, check against user
        file.upload_finished_at = timezone.now()
        file.full_clean()
        file.save()

        return file
```

----------------------------------------

TITLE: Conditional Sentry Integration Setup (Python)
DESCRIPTION: Shows how to conditionally configure an integration (Sentry) based on whether a specific environment variable (`SENTRY_DSN`) is set. This allows integrations to be easily enabled or disabled via environment configuration without modifying code, promoting modularity.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_36

LANGUAGE: python
CODE:
```
from config.env import env

SENTRY_DSN = env('SENTRY_DSN', default='')

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.celery import CeleryIntegration

    # ... we proceed with sentry settings here ...
    # View the full file here - https://github.com/HackSoftware/Styleguide-Example/blob/master/config/settings/sentry.py
```

----------------------------------------

TITLE: Implementing Model Validation with clean Method
DESCRIPTION: Shows how to add custom validation logic to a Django model by implementing the `clean` method. This example validates that the `start_date` of a `Course` model is not on or after the `end_date`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_2

LANGUAGE: python
CODE:
```
class Course(BaseModel):
    name = models.CharField(unique=True, max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("End date cannot be before start date")
```

----------------------------------------

TITLE: Triggering Custom Application Error - Python
DESCRIPTION: Demonstrates raising a custom 'ApplicationError' with a message and extra data. This is an example of an application-specific exception that the custom handler is designed to specifically format.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_58

LANGUAGE: python
CODE:
```
from styleguide_example.core.exceptions import ApplicationError


def trigger_application_error():
    raise ApplicationError(message="Something is not correct", extra={"type": "RANDOM"})
```

----------------------------------------

TITLE: Creating Simple Django List APIView
DESCRIPTION: This example shows a basic list API inheriting `APIView`. It defines an nested `OutputSerializer` to structure the response data and uses a selector (`user_list`) to fetch the data, serializing the result before returning a DRF `Response`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_19

LANGUAGE: python
CODE:
```
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from styleguide_example.users.selectors import user_list
from styleguide_example.users.models import BaseUser


class UserListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        email = serializers.CharField()

    def get(self, request):
        users = user_list()

        data = self.OutputSerializer(users, many=True).data

        return Response(data)
```

----------------------------------------

TITLE: Initializing django-environ Environment Object (Python)
DESCRIPTION: Initializes the `env` object from `django-environ`, which is used throughout the project to read environment variables and values from a .env file. This setup is typically placed in a central file like `config/env.py` to be imported elsewhere.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_33

LANGUAGE: python
CODE:
```
import environ

env = environ.Env()
```

----------------------------------------

TITLE: Raising Django Permission Denied - Python
DESCRIPTION: An example function raising Django's standard `PermissionDenied` exception. The custom handler translates this into a DRF `PermissionDenied` exception before processing.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_62

LANGUAGE: python
CODE:
```
from django.core.exceptions import PermissionDenied

def some_service():
    raise PermissionDenied()
```

----------------------------------------

TITLE: Raising DRF Throttled Exception - Python
DESCRIPTION: An example function raising DRF's `Throttled` exception, used to indicate rate limiting. The custom handler processes this like other standard DRF exceptions.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_72

LANGUAGE: python
CODE:
```
from rest_framework import exceptions


def some_service():
    raise exceptions.Throttled()
```

----------------------------------------

TITLE: Implementing Advanced Serialization Function - Python
DESCRIPTION: This example shows an advanced serialization function that takes raw data (a list of FeedItem objects), re-fetches the data with query optimizations (select_related, prefetch_related), uses caching for additional data, adds calculated fields to objects, and then serializes each item using a standard DRF Serializer.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_30

LANGUAGE: python
CODE:
```
class FeedItemSerializer(serializers.Serializer):
    ... some fields here ...
    calculated_field = serializers.IntegerField(source="_calculated_field")


def some_feed_serialize(feed: List[FeedItem]):
    feed_ids = [feed_item.id for feed_item in feed]

    # Refetch items with more optimizations
    # Based on the relations that are going in
    objects = FeedItem.objects.select_related(
      # ... as complex as you want ...
    ).prefetch_related(
      # ... as complex as you want ...
    ).filter(
      id__in=feed_ids
    ).order_by(
      "-some_timestamp"
    )

    some_cache = get_some_cache(feed_ids)

    result = []

    for feed_item in objects:
        # An example, adding additional fields for the serializer
        # That are based on values outside of our current object
        # This may be some optimization to save queries
        feed_item._calculated_field = some_cache.get(feed_item.id)

        result.append(FeedItemSerializer(feed_item).data)

    return result
```

----------------------------------------

TITLE: Example Basic API Error Response Format
DESCRIPTION: This JSON snippet illustrates a simple desired format for API error responses, consisting of a single JSON object with a 'message' key containing the error description. This structure serves as a baseline for defining consistent API error interfaces.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_45

LANGUAGE: json
CODE:
```
{
  "message": "Some error message here"
}
```

----------------------------------------

TITLE: Raising Django Validation Error (Model full_clean) - Python
DESCRIPTION: An example function demonstrating raising Django's `ValidationError` through a model's `full_clean()` method. The custom handler is configured to catch and format this.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_74

LANGUAGE: python
CODE:
```
def some_service():
    user = BaseUser()
    user.full_clean()
```

----------------------------------------

TITLE: Defining Django Model Properties - Python
DESCRIPTION: Defines a Django `Course` model with basic fields and two `@property` methods (`has_started`, `has_finished`) that check if the course start or end date is in the past using `timezone.now()`. It also includes a `clean` method for date validation.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_5

LANGUAGE: python
CODE:
```
from django.utils import timezone
from django.core.exceptions import ValidationError


class Course(BaseModel):
    name = models.CharField(unique=True, max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("End date cannot be before start date")

    @property
    def has_started(self) -> bool:
        now = timezone.now()

        return self.start_date <= now.date()

    @property
    def has_finished(self) -> bool:
        now = timezone.now()

        return self.end_date <= now.date()
```

----------------------------------------

TITLE: Implementing Model Validation with Constraints
DESCRIPTION: Demonstrates using Django's model `constraints` to enforce data integrity at the database level. This example adds a `CheckConstraint` to the `Course` model's `Meta` class, ensuring the `start_date` field is strictly less than the `end_date`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_4

LANGUAGE: python
CODE:
```
class Course(BaseModel):
    name = models.CharField(unique=True, max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="start_date_before_end_date",
                check=Q(start_date__lt=F("end_date"))
            )
        ]
```

----------------------------------------

TITLE: Raising DRF Validation Error (String Detail) - Python
DESCRIPTION: An example function raising a DRF `ValidationError` with a simple string detail. The custom handler processes this to fit the standard format.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_66

LANGUAGE: python
CODE:
```
def some_service():
    raise RestValidationError("Some error message")
```

----------------------------------------

TITLE: Raising Django Validation Error in Service - Python
DESCRIPTION: An example function demonstrating how a Django `ValidationError` might be raised within a service layer. The custom handler is responsible for catching and formatting this exception into the standard API response.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_60

LANGUAGE: python
CODE:
```
def some_service():
    raise DjangoValidationError("Some error message")
```

----------------------------------------

TITLE: Implementing Class-Based Django APIView
DESCRIPTION: This snippet shows a basic class-based API inheriting from a custom `BaseApi`. It defines a standard HTTP GET method that retrieves data and returns an HTTP response using DRF's `Response` object.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_17

LANGUAGE: python
CODE:
```
class SomeApi(BaseApi):
    def get(self, request):
        data = something()

        return Response(data)
```

----------------------------------------

TITLE: Raising DRF Validation Error (Dict Detail) - Python
DESCRIPTION: An example function raising a DRF `ValidationError` with a dictionary detail, simulating field-specific errors. The custom handler processes this structure.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_68

LANGUAGE: python
CODE:
```
def some_service():
    raise RestValidationError(detail={"error": "Some error message"})
```

----------------------------------------

TITLE: Defining Django Model Method with Argument - Python
DESCRIPTION: Extends the `Course` model with an `is_within` method that takes a date argument `x` and checks if `x` falls between the course's start and end dates. This demonstrates adding methods that require input parameters to model instances.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_6

LANGUAGE: python
CODE:
```
from django.core.exceptions import ValidationError
from django.utils import timezone


class Course(BaseModel):
    name = models.CharField(unique=True, max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("End date cannot be before start date")

    @property
    def has_started(self) -> bool:
        now = timezone.now()

        return self.start_date <= now.date()

    @property
    def has_finished(self) -> bool:
        now = timezone.now()

        return self.end_date <= now.date()

    def is_within(self, x: date) -> bool:
        return self.start_date <= x <= self.end_date
```

----------------------------------------

TITLE: Example Validation Error Response Structure - JSON
DESCRIPTION: Illustrates the standard JSON error format specifically for validation errors. The 'extra' field contains a 'fields' dictionary detailing errors for individual fields, mapping field names to lists of error messages or nested error structures.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_56

LANGUAGE: json
CODE:
```
{
  "message": "Validation error.",
  "extra": {
    "fields": {
      "password": ["This field cannot be blank."],
      "email": ["This field cannot be blank."]
    }
  }
}
```

----------------------------------------

TITLE: Selecting User List using Function-Based Selector in Django Python
DESCRIPTION: This function defines a selector responsible for fetching a list of `User` objects visible to the `fetched_by` user. It calls another selector (`user_get_visible_for`) to get allowed user IDs and then filters the `User` queryset accordingly. It returns an iterable of `User` objects. Requires `User`, `Iterable`, `Q` (presumably from `django.db.models`), and `user_get_visible_for`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_14

LANGUAGE: python
CODE:
```
def user_list(*, fetched_by: User) -> Iterable[User]:
    user_ids = user_get_visible_for(user=fetched_by)

    query = Q(id__in=user_ids)

    return User.objects.filter(query)
```

----------------------------------------

TITLE: Testing Item Buy Service in Django Python
DESCRIPTION: This `TestCase` class contains tests for the `item_buy` service, demonstrating how to cover business logic while hitting the database. It shows how to use `@patch` to mock external dependencies like selectors (`items_get_for_user`) and asynchronous tasks (`payment_charge.delay`), and asserts that the service correctly handles validation errors, creates the expected database objects, and calls dependent tasks. Requires `unittest.mock.patch`, `Mock`, `django.test.TestCase`, `django.contrib.auth.models.User`, `django.core.exceptions.ValidationError`, `django_styleguide.payments.services.item_buy`, `django_styleguide.payments.models.Payment`, `Item`, and test helper functions like `given_a_user` and `given_a_item`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_16

LANGUAGE: python
CODE:
```
from unittest.mock import patch, Mock

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django_styleguide.payments.services import item_buy
from django_styleguide.payments.models import Payment, Item


class ItemBuyTests(TestCase):
    @patch('project.payments.services.items_get_for_user')
    def test_buying_item_that_is_already_bought_fails(
        self, items_get_for_user_mock: Mock
    ):
        """
        Since we already have tests for `items_get_for_user`,
        we can safely mock it here and give it a proper return value.
        """
        user = User(username='Test User')
        item = Item(
            name='Test Item',
            description='Test Item description',
            price=10.15
        )

        items_get_for_user_mock.return_value = [item]

        with self.assertRaises(ValidationError):
            item_buy(user=user, item=item)

    @patch('project.payments.services.payment_charge.delay')
    def test_buying_item_creates_a_payment_and_calls_charge_task(
        self,
        payment_charge_mock: Mock
    ):
        # How we prepare our tests is a topic for a different discussion
        user = given_a_user(username="Test user")
        item = given_a_item(
            name='Test Item',
            description='Test Item description',
            price=10.15
        )

        self.assertEqual(0, Payment.objects.count())

        payment = item_buy(user=user, item=item)

        self.assertEqual(1, Payment.objects.count())
        self.assertEqual(payment, Payment.objects.first())

        self.assertFalse(payment.successful)

        payment_charge_mock.assert_called_once()
```

----------------------------------------

TITLE: Importing Settings Modules in base.py (Python)
DESCRIPTION: Demonstrates how settings from various integration-specific or modular configuration files within `config/settings` are imported into the main `config/django/base.py` file. This aggregates all settings into the base configuration. `noqa` is used to suppress linting warnings about wildcard imports.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_35

LANGUAGE: python
CODE:
```
from config.settings.cors import *  # noqa
from config.settings.sessions import *  # noqa
from config.settings.celery import *  # noqa
from config.settings.sentry import *  # noqa
```

----------------------------------------

TITLE: Implementing Function-Based Django Service - Python
DESCRIPTION: Shows a simple function-based service `user_create` that encapsulates the business logic for creating a new user. It takes keyword-only arguments, performs validation and saving, and orchestrates calls to other related services (`profile_create`, `confirmation_email_send`).

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_9

LANGUAGE: python
CODE:
```
def user_create(
    *,
    email: str,
    name: str
) -> User:
    user = User(email=email)
    user.full_clean()
    user.save()

    profile_create(user=user, name=name)
    confirmation_email_send(user=user)

    return user
```

----------------------------------------

TITLE: Setting Up Django Celery Beat Periodic Tasks - Management Command
DESCRIPTION: Implements a Django management command (`setup_periodic_tasks`) designed to programmatically define and set up Celery Beat periodic tasks using the `django-celery-beat` models. It clears existing periodic task configurations and creates new ones based on a hardcoded list, primarily using `CrontabSchedule` to define schedules. This command is typically run during deployment.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_80

LANGUAGE: Python
CODE:
```
from django.core.management.base import BaseCommand
from django.db import transaction

from django_celery_beat.models import IntervalSchedule, CrontabSchedule, PeriodicTask

from project.app.tasks import some_periodic_task


class Command(BaseCommand):
    help = f"""
    Setup celery beat periodic tasks.

    Following tasks will be created:

    - {some_periodic_task.name}
    """

    @transaction.atomic
    def handle(self, *args, **kwargs):
        print('Deleting all periodic tasks and schedules...\n')

        IntervalSchedule.objects.all().delete()
        CrontabSchedule.objects.all().delete()
        PeriodicTask.objects.all().delete()

        periodic_tasks_data = [
            {
                'task': some_periodic_task,
                'name': 'Do some peridoic stuff',
                # https://crontab.guru/#15_*_*_*_*
                'cron': {
                    'minute': '15',
                    'hour': '*',
                    'day_of_week': '*',
                    'day_of_month': '*',
                    'month_of_year': '*'
                },
                'enabled': True
            },
        ]

        for periodic_task in periodic_tasks_data:
            print(f'Setting up {periodic_task["task"].name}')

            cron = CrontabSchedule.objects.create(
                **periodic_task['cron']
            )

            PeriodicTask.objects.create(
                name=periodic_task['name'],
                task=periodic_task['task'].name,
                crontab=cron,
                enabled=periodic_task['enabled']
            )
```

----------------------------------------

TITLE: Structuring API with Separated Fetching and Serialization - Django REST Framework - Python
DESCRIPTION: This API view demonstrates a pattern where the initial data fetching (`some_feed_get`) is kept simple, and complex serialization and optimization logic is delegated to a separate serializer function (`some_feed_serialize`) after fetching the initial data.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_29

LANGUAGE: python
CODE:
```
class SomeGenericFeedApi(BaseApi):
    def get(self, request):
        feed = some_feed_get(
            user=request.user,
        )

        data = some_feed_serialize(feed)

        return Response(data)
```

----------------------------------------

TITLE: Creating Object Fetching Utility - Python
DESCRIPTION: This utility function wraps Django's `get_object_or_404` helper. It attempts to fetch an object based on the provided model/queryset and keyword arguments, returning the object on success or `None` if a `Http404` exception occurs.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_27

LANGUAGE: python
CODE:
```
def get_object(model_or_queryset, **kwargs):
    """
    Reuse get_object_or_404 since the implementation supports both Model && queryset.
    Catch Http404 & return None
    """
    try:
        return get_object_or_404(model_or_queryset, **kwargs)
    except Http404:
        return None
```

----------------------------------------

TITLE: Implementing Class-Based Django Service - Python
DESCRIPTION: Presents a class-based service `FileStandardUploadService` with `create` and `update` methods for handling file uploads. It demonstrates encapsulating related logic within a class namespace and reusing an internal helper method (`_infer_file_name_and_type`). Methods use the `django.db.transaction.atomic` decorator for database transactions.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_10

LANGUAGE: python
CODE:
```
# https://github.com/HackSoftware/Django-Styleguide-Example/blob/master/styleguide_example/files/services.py


class FileStandardUploadService:
    """
    This also serves as an example of a service class,
    which encapsulates 2 different behaviors (create & update) under a namespace.

    Meaning, we use the class here for:

    1. The namespace
    2. The ability to reuse `_infer_file_name_and_type` (which can also be an util)
    """
    def __init__(self, user: BaseUser, file_obj):
        self.user = user
        self.file_obj = file_obj

    def _infer_file_name_and_type(self, file_name: str = "", file_type: str = "") -> Tuple[str, str]:
        file_name = file_name or self.file_obj.name

        if not file_type:
            guessed_file_type, encoding = mimetypes.guess_type(file_name)
            file_type = guessed_file_type or ""

        return file_name, file_type

    @transaction.atomic
    def create(self, file_name: str = "", file_type: str = "") -> File:
        _validate_file_size(self.file_obj)

        file_name, file_type = self._infer_file_name_and_type(file_name, file_type)

        obj = File(
            file=self.file_obj,
            original_file_name=file_name,
            file_name=file_generate_name(file_name),
            file_type=file_type,
            uploaded_by=self.user,
            upload_finished_at=timezone.now()
        )

        obj.full_clean()
        obj.save()

        return obj

    @transaction.atomic
    def update(self, file: File, file_name: str = "", file_type: str = "") -> File:
        _validate_file_size(self.file_obj)

        file_name, file_type = self._infer_file_name_and_type(file_name, file_type)

        file.file = self.file_obj
        file.original_file_name = file_name
        file.file_name = file_generate_name(file_name)
        file.file_type = file_type
        file.uploaded_by = self.user
        file.upload_finished_at = timezone.now()

        file.full_clean()
        file.save()

        return file
```

----------------------------------------

TITLE: Handling Create API Request - Django REST Framework - Python
DESCRIPTION: This snippet defines a Django REST Framework API view for creating a new Course object. It uses an inner InputSerializer to validate incoming request data and calls a service function `course_create` with the validated data.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_25

LANGUAGE: python
CODE:
```
class CourseCreateApi(SomeAuthenticationMixin, APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        start_date = serializers.DateField()
        end_date = serializers.DateField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)
```

----------------------------------------

TITLE: Test Case: Raising Django Http404 with Custom Handler
DESCRIPTION: This Python snippet demonstrates a test case where Django's `Http404` exception is raised. The custom handler should convert this to DRF's `NotFound` exception, resulting in a 404 status code and a response body standardized with the 'detail' key.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_49

LANGUAGE: python
CODE:
```
from django.http import Http404

def some_service():
    raise Http404()
```

----------------------------------------

TITLE: Handling Detail API Request - Django REST Framework - Python
DESCRIPTION: This snippet defines a Django REST Framework API view for fetching and returning details of a single Course object. It uses an inner OutputSerializer to define the structure of the response data and fetches the course object using a service function `course_get`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_24

LANGUAGE: python
CODE:
```
class CourseDetailApi(SomeAuthenticationMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        start_date = serializers.DateField()
        end_date = serializers.DateField()

    def get(self, request, course_id):
        course = course_get(id=course_id)

        serializer = self.OutputSerializer(course)

        return Response(serializer.data)
```

----------------------------------------

TITLE: Updating User with Service Pattern (Python)
DESCRIPTION: This Python snippet demonstrates a common pattern for updating a Django model instance (User) using a service function. It utilizes a generic `model_update` service for fields without side effects and reserves space for handling side-effect fields and additional tasks within the dedicated user update service. It requires an existing `User` model and the `model_update` service.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_81

LANGUAGE: python
CODE:
```
def user_update(*, user: User, data) -> User:
    non_side_effect_fields = ['first_name', 'last_name']

    user, has_updated = model_update(
        instance=user,
        fields=non_side_effect_fields,
        data=data
    )

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user
```

----------------------------------------

TITLE: Organizing URLs with Nested Includes - Django - Python
DESCRIPTION: This snippet demonstrates an alternative way to structure Django URL configurations using nested `include` calls directly within `urlpatterns`. This approach visually represents the URL tree structure directly in the main urls.py file.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_32

LANGUAGE: python
CODE:
```
from django.urls import path, include

from styleguide_example.files.apis import (
    FileDirectUploadApi,

    FilePassThruUploadStartApi,
    FilePassThruUploadFinishApi,
    FilePassThruUploadLocalApi,
)


urlpatterns = [
    path(
        "upload/",
        include((
            [
                path(
                    "direct/",
                    FileDirectUploadApi.as_view(),
                    name="direct"
                ),
                path(
                    "pass-thru/",
                    include((
                        [
                            path(
                                "start/",
                                FilePassThruUploadStartApi.as_view(),
                                name="start"
                            ),
                            path(
                                "finish/",
                                FilePassThruUploadFinishApi.as_view(),
                                name="finish"
                            ),
                            path(
                                "local/<str:file_id>/",
                                FilePassThruUploadLocalApi.as_view(),
                                name="local"
                            )
                        ], "pass-thru"
                    ))
                )
            ], "upload"
        ))
    )
]
```

----------------------------------------

TITLE: Reading .env File with django-environ (Python)
DESCRIPTION: Configures `django-environ` to read settings from a .env file located at the project root. This allows developers to use a local .env file for development configuration, which is loaded before other settings are read from the environment.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_37

LANGUAGE: python
CODE:
```
# That's in the beginning of base.py

import os

from config.env import env, environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = environ.Path(__file__) - 3

env.read_env(os.path.join(BASE_DIR, ".env"))
```

----------------------------------------

TITLE: Buying Item using Function-Based Service in Django Python
DESCRIPTION: This function defines a service for the "item buy" operation. It first validates if the user already owns the item by calling a selector (`items_get_for_user`), creates a `Payment` object, and then schedules an asynchronous task (`payment_charge`) to process the payment only after the database transaction successfully commits. It returns the created `Payment` object. Requires `User`, `ValidationError`, `transaction`, `items_get_for_user`, `Item`, `Payment`, and `payment_charge`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_15

LANGUAGE: python
CODE:
```
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction

from project.payments.selectors import items_get_for_user
from project.payments.models import Item, Payment
from project.payments.tasks import payment_charge


@transaction.atomic
def item_buy(
    *,
    item: Item,
    user: User,
) -> Payment:
    if item in items_get_for_user(user=user):
        raise ValidationError(f'Item {item} already in {user} items.')

    payment = Payment(
        item=item,
        user=user,
        successful=False
    )
    payment.full_clean()
    payment.save()

    # Run the task once the transaction has commited,
    # guaranteeing the object has been created.
    transaction.on_commit(
        lambda: payment_charge.delay(payment_id=payment.id)
    )

    return payment
```

----------------------------------------

TITLE: Response for Django Permission Denied - JSON
DESCRIPTION: Shows the JSON response when Django's `PermissionDenied` is raised. The handler translates it and the DRF default handler provides the standard 'You do not have permission' message.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_63

LANGUAGE: json
CODE:
```
{
  "message": "You do not have permission to perform this action.",
  "extra": {}
}
```

----------------------------------------

TITLE: Raising DRF NotFound Exception (Python)
DESCRIPTION: Demonstrates raising a `rest_framework.exceptions.NotFound` exception. Unlike `ValidationError`, this results in a consistent JSON response format of `{"detail": "..."}`, further illustrating the varying response structures for different DRF built-in exceptions.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_40

LANGUAGE: python
CODE:
```
from rest_framework import exceptions


def some_service():
    raise exceptions.NotFound()
```

----------------------------------------

TITLE: Organizing URLs with Separate Patterns List - Django - Python
DESCRIPTION: This snippet shows how to structure Django URL configurations by grouping related paths into a separate list (`course_patterns`) and then including that list in the main `urlpatterns`. This promotes modularity and organization.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_31

LANGUAGE: python
CODE:
```
from django.urls import path, include

from project.education.apis import (
    CourseCreateApi,
    CourseUpdateApi,
    CourseListApi,
    CourseDetailApi,
    CourseSpecificActionApi,
)


course_patterns = [
    path('', CourseListApi.as_view(), name='list'),
    path('<int:course_id>/', CourseDetailApi.as_view(), name='detail'),
    path('create/', CourseCreateApi.as_view(), name='create'),
    path('<int:course_id>/update/', CourseUpdateApi.as_view(), name='update'),
    path(
        '<int:course_id>/specific-action/',
        CourseSpecificActionApi.as_view(),
        name='specific-action'
    ),
]

urlpatterns = [
    path('courses/', include((course_patterns, 'courses'))),
]
```

----------------------------------------

TITLE: Run update_toc.py Script using Python
DESCRIPTION: This command executes the 'update_toc.py' script using the Python interpreter. When run from the root directory of the project, this script will automatically update the table of contents within the 'README.md' file based on its headers.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/tools/README.md#_snippet_1

LANGUAGE: Shell
CODE:
```
python update_toc.py
```

----------------------------------------

TITLE: Calling full_clean Before Saving in a Service
DESCRIPTION: Illustrates the recommended pattern for ensuring model validation is triggered. This Python function, representing a service, creates a `Course` instance and explicitly calls `full_clean()` before calling `save()`, ensuring the `clean` method is executed.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_3

LANGUAGE: python
CODE:
```
def course_create(*, name: str, start_date: date, end_date: date) -> Course:
    obj = Course(name=name, start_date=start_date, end_date=end_date)

    obj.full_clean()
    obj.save()

    return obj
```

----------------------------------------

TITLE: Importing django-environ Environment Object (Python)
DESCRIPTION: Imports the pre-initialized `env` object from the `config.env` module. This allows other parts of the application, such as settings files, to easily access environment-specific configuration values via the `env` object.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_34

LANGUAGE: python
CODE:
```
from config.env import env
```

----------------------------------------

TITLE: Implementing Paginated/Filtered Django List APIView
DESCRIPTION: This advanced list API demonstrates handling request filters and pagination with `APIView`. It includes nested `FilterSerializer` for validating query parameters, a `Pagination` class for controlling pagination logic, and uses a utility function (`get_paginated_response`) to format the final, paginated response.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_20

LANGUAGE: python
CODE:
```
from rest_framework.views import APIView
from rest_framework import serializers

from styleguide_example.api.mixins import ApiErrorsMixin
from styleguide_example.api.pagination import get_paginated_response, LimitOffsetPagination

from styleguide_example.users.selectors import user_list
from styleguide_example.users.models import BaseUser


class UserListApi(ApiErrorsMixin, APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        # Important: If we use BooleanField, it will default to False
        is_admin = serializers.NullBooleanField(required=False)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        email = serializers.CharField()
        is_admin = serializers.BooleanField()

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self
        )
```

----------------------------------------

TITLE: Implementing Django Paginated Response Utility
DESCRIPTION: This utility function (`get_paginated_response`) handles the logic for creating a paginated DRF response. It takes pagination and serializer classes, a queryset, request, and view, applies pagination, serializes the resulting page, and returns the paginator's formatted response.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_22

LANGUAGE: python
CODE:
```
from rest_framework.response import Response


def get_paginated_response(*, pagination_class, serializer_class, queryset, request, view):
    paginator = pagination_class()

    page = paginator.paginate_queryset(queryset, request, view=view)

    if page is not None:
        serializer = serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True)

    return Response(data=serializer.data)
```

----------------------------------------

TITLE: Response for Django Http404 - JSON
DESCRIPTION: Shows the JSON response when Django's `Http404` is raised. The handler translates it and the DRF default handler provides the standard 'Not found.' message.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_65

LANGUAGE: json
CODE:
```
{
  "message": "Not found.",
  "extra": {}
}
```

----------------------------------------

TITLE: Inheriting from BaseModel
DESCRIPTION: Demonstrates how to define a new Django model, `SomeModel`, by inheriting from the custom `BaseModel`. This allows the new model to automatically include the `created_at` and `updated_at` fields defined in the base class.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_1

LANGUAGE: python
CODE:
```
class SomeModel(BaseModel):
    pass
```

----------------------------------------

TITLE: Handling File Direct Upload API Request in Django REST Framework Python
DESCRIPTION: This Django REST Framework API View handles POST requests for direct file uploads. It instantiates `FileDirectUploadService` with the user and uploaded file, calls its `create` method to perform the upload logic, and returns the ID of the created file object with a 201 status code. Requires Django REST Framework, `ApiAuthMixin`, and the `FileDirectUploadService`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_11

LANGUAGE: python
CODE:
```
class FileDirectUploadApi(ApiAuthMixin, APIView):
    def post(self, request):
        service = FileDirectUploadService(
            user=request.user,
            file_obj=request.FILES["file"]
        )
        file = service.create()

        return Response(data={"id": file.id}, status=status.HTTP_201_CREATED)
```

----------------------------------------

TITLE: Response for DRF Throttled Exception - JSON
DESCRIPTION: Shows the JSON response when a DRF `Throttled` exception is raised. The DRF default handler provides the message, and the custom handler fits it into the standard format.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_73

LANGUAGE: json
CODE:
```
{
  "message": "Request was throttled.",
  "extra": {}
}
```

----------------------------------------

TITLE: Testing Django Model Validation - Python
DESCRIPTION: Provides a Django unit test class `CourseTests` demonstrating how to test model validation (`full_clean`) without hitting the database. It specifically tests the `clean` method's validation for the `start_date` and `end_date` relationship using `assertRaises(ValidationError)`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_8

LANGUAGE: python
CODE:
```
from datetime import timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from project.some_app.models import Course


class CourseTests(TestCase):
    def test_course_end_date_cannot_be_before_start_date(self):
        start_date = timezone.now()
        end_date = timezone.now() - timedelta(days=1)

        course = Course(start_date=start_date, end_date=end_date)

        with self.assertRaises(ValidationError):
            course.full_clean()
```

----------------------------------------

TITLE: Implementing Function-Based Django API View
DESCRIPTION: This snippet demonstrates a function-based API using a hypothetical `base_api` decorator (similar in concept to DRF's `@api_view`). It defines a view function that accepts a request, fetches data, and returns a DRF `Response`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_18

LANGUAGE: python
CODE:
```
@base_api(["GET"])
def some_api(request):
    data = something()
    return Response(data)
```

----------------------------------------

TITLE: Triggering Email Service with Celery Task - Basic
DESCRIPTION: Defines a simple Celery shared task `email_send` that takes an email ID, fetches the corresponding `Email` model instance from the database, and then calls the core `email_send` service function (from snippet 1) to perform the actual email sending business logic.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_77

LANGUAGE: Python
CODE:
```
from celery import shared_task

from styleguide_example.emails.models import Email


@shared_task
def email_send(email_id):
    email = Email.objects.get(id=email_id)

    from styleguide_example.emails.services import email_send
    email_send(email)
```

----------------------------------------

TITLE: Test Case: Raising DRF Throttled Exception with Custom Handler
DESCRIPTION: This Python snippet is a test case raising a standard DRF exception, `exceptions.Throttled`. The custom handler should process this exception and format its default detail message under the 'detail' key in the API response.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_53

LANGUAGE: python
CODE:
```
from rest_framework import exceptions


def some_service():
    raise exceptions.Throttled()
```

----------------------------------------

TITLE: Response for Custom Application Error - JSON
DESCRIPTION: Shows the expected JSON response when the custom 'ApplicationError' is raised and processed by the handler. The message and extra data from the exception are directly included in the standard error format.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_59

LANGUAGE: json
CODE:
```
{
  "message": "Something is not correct",
  "extra": {
    "type": "RANDOM"
  }
}
```

----------------------------------------

TITLE: Sending Email Service with Django
DESCRIPTION: Defines a service function `email_send` that handles the core logic of sending an email using Django's mail utilities. It checks the email status, constructs the message, sends it, and updates the email object's status and sent time using a `model_update` service, wrapped in an atomic transaction.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_76

LANGUAGE: Python
CODE:
```
from django.db import transaction
from django.core.mail import EmailMultiAlternatives

from styleguide_example.core.exceptions import ApplicationError
from styleguide_example.common.services import model_update
from styleguide_example.emails.models import Email


@transaction.atomic
def email_send(email: Email) -> Email:
    if email.status != Email.Status.SENDING:
        raise ApplicationError(f"Cannot send non-ready emails. Current status is {email.status}")

    subject = email.subject
    from_email = "styleguide-example@hacksoft.io"
    to = email.to

    html = email.html
    plain_text = email.plain_text

    msg = EmailMultiAlternatives(subject, plain_text, from_email, [to])
    msg.attach_alternative(html, "text/html")

    msg.send()

    email, _ = model_update(
        instance=email,
        fields=["status", "sent_at"],
        data={
            "status": Email.Status.SENT,
            "sent_at": timezone.now()
        }
    )
    return email
```

----------------------------------------

TITLE: Advanced Custom DRF Exception Handler for Standardized Output
DESCRIPTION: This Python function provides a more advanced custom exception handler for DRF. It maps `DjangoValidationError`, `Http404`, and `PermissionDenied` to their DRF equivalents and, critically, ensures that the final response data is wrapped within a 'detail' key for consistency, regardless of the original exception type.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_46

LANGUAGE: python
CODE:
```
from django.core.exceptions import ValidationError as DjangoValidationError, PermissionDenied
from django.http import Http404

from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.serializers import as_serializer_error


def drf_default_with_modifications_exception_handler(exc, ctx):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response

    if isinstance(exc.detail, (list, dict)):
        response.data = {
            "detail": response.data
        }

    return response
```

----------------------------------------

TITLE: Defining Django Model Method for Attribute Setting - Python
DESCRIPTION: Defines a Django `Token` model and a `set_new_secret` method that generates a new random secret string and sets the `expiry` date based on a configurable timedelta (`settings.TOKEN_EXPIRY_TIMEDELTA`). This method encapsulates logic for interdependent attribute updates.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_7

LANGUAGE: python
CODE:
```
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone


class Token(BaseModel):
    secret = models.CharField(max_length=255, unique=True)
    expiry = models.DateTimeField(blank=True, null=True)

    def set_new_secret(self):
        now = timezone.now()

        self.secret = get_random_string(255)
        self.expiry = now + settings.TOKEN_EXPIRY_TIMEDELTA

        return self
```

----------------------------------------

TITLE: Test Case: Raising Django PermissionDenied with Custom Handler
DESCRIPTION: This Python snippet represents a test case where Django's `PermissionDenied` exception is raised. The custom handler is expected to intercept this, convert it to DRF's `PermissionDenied`, and return a response formatted with the 'detail' key.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_48

LANGUAGE: python
CODE:
```
from django.core.exceptions import PermissionDenied

def some_service():
    raise PermissionDenied()
```

----------------------------------------

TITLE: Enqueuing Celery Task on Transaction Commit - Django Service
DESCRIPTION: Shows a Django service function `user_complete_onboarding` that illustrates how to trigger a Celery task (`email_send_task`) from within a service. It imports the task with a suffix and uses `transaction.on_commit` to ensure the task is only enqueued if the current database transaction successfully commits, preventing issues with uncommitted data.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_78

LANGUAGE: Python
CODE:
```
from django.db import transaction

# ... more imports here ...

from styleguide_example.emails.tasks import email_send as email_send_task


@transaction.atomic
def user_complete_onboarding(user: User) -> User:
    # ... some code here

    email = email_get_onboarding_template(user=user)

    transaction.on_commit(lambda: email_send_task.delay(email.id))

    return user
```

----------------------------------------

TITLE: Defining Custom Limit/Offset Pagination Class
DESCRIPTION: This snippet defines a custom `LimitOffsetPagination` class, inheriting from DRF's built-in version. It overrides the `get_paginated_data` and `get_paginated_response` methods to include `limit` and `offset` fields in the response data, providing more context for frontend clients.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_23

LANGUAGE: python
CODE:
```
from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination as _LimitOffsetPagination
from rest_framework.response import Response


class LimitOffsetPagination(_LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    def get_paginated_data(self, data):
        return OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])

    def get_paginated_response(self, data):
        """
        We redefine this method in order to return `limit` and `offset`.
        This is used by the frontend to construct the pagination itself.
        """
        return Response(OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
```

----------------------------------------

TITLE: Saving File Model in Django Admin using Service Python
DESCRIPTION: This `save_model` method within a Django Admin `ModelAdmin` uses the `FileDirectUploadService` to handle file creation or update logic when saving a `File` instance. It retrieves data from the form, calls the service's `create` or `update` method, and handles `ValidationError` by displaying an error message to the user. Requires Django Admin and `FileDirectUploadService`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_12

LANGUAGE: python
CODE:
```
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    # ... other code here ...
    # https://github.com/HackSoftware/Django-Styleguide-Example/blob/master/styleguide_example/files/admin.py

    def save_model(self, request, obj, form, change):
        try:
            cleaned_data = form.cleaned_data

            service = FileDirectUploadService(
                file_obj=cleaned_data["file"],
                user=cleaned_data["uploaded_by"]
            )

            if change:
                service.update(file=obj)
            else:
                service.create()
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
```

----------------------------------------

TITLE: Defining a Django BaseModel
DESCRIPTION: Defines an abstract base model `BaseModel` that includes common fields like `created_at` and `updated_at`. This model is designed to be inherited by other models to automatically provide these fields.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_0

LANGUAGE: python
CODE:
```
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

----------------------------------------

TITLE: Creating Django Selector with django-filter
DESCRIPTION: This snippet shows a selector function (`user_list`) responsible for fetching and filtering data, used by the list API. It utilizes the `django-filter` library to apply filters passed from the API to the Django queryset, returning the filtered queryset.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_21

LANGUAGE: python
CODE:
```
import django_filters

from styleguide_example.users.models import BaseUser


class BaseUserFilter(django_filters.FilterSet):
    class Meta:
        model = BaseUser
        fields = ('id', 'email', 'is_admin')


def user_list(*, filters=None):
    filters = filters or {}

    qs = BaseUser.objects.all()

    return BaseUserFilter(filters, qs).qs
```

----------------------------------------

TITLE: Response for DRF Validation Error (String Detail) - JSON
DESCRIPTION: Illustrates the JSON output when a DRF `ValidationError` with a string detail is raised. The handler formats it under `extra.fields`.

SOURCE: https://github.com/hacksoftware/django-styleguide/blob/master/README.md#_snippet_67

LANGUAGE: json
CODE:
```
{
  "message": "Validation error",
  "extra": {
    "fields": ["Some error message"]
  }
}
```
