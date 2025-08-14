========================
CODE SNIPPETS
========================
TITLE: Install Celery from a source tarball
DESCRIPTION: Provides instructions for downloading, extracting, building, and installing Celery directly from a compressed source archive. This method is typically used for specific versions or when PyPI is not an option. The final installation step may require superuser privileges if not in a virtual environment.

SOURCE: https://github.com/celery/celery/blob/main/docs/includes/installation.txt#_snippet_2

LANGUAGE: console
CODE:
```
$ tar xvfz celery-0.0.0.tar.gz
$ cd celery-0.0.0
$ python setup.py build
# python setup.py install
```

----------------------------------------

TITLE: Celery Python: Example Configuration File
DESCRIPTION: This snippet provides a basic Celery configuration example, including broker settings, module imports, and result backend setup. It demonstrates how to configure Celery using `celeryconfig.py` for a simple setup.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_0

LANGUAGE: python
CODE:
```
## Broker settings.
broker_url = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
imports = ('myapp.tasks,')

## Using the database to store task state and results.
result_backend = 'db+sqlite:///results.db'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}
```

----------------------------------------

TITLE: Install Celery development version from GitHub using pip
DESCRIPTION: Installs the latest development snapshots of Celery and its core dependencies (billiard, amqp, kombu, vine) directly from their respective GitHub repositories. This is suitable for testing new features or contributing to the project.

SOURCE: https://github.com/celery/celery/blob/main/docs/includes/installation.txt#_snippet_3

LANGUAGE: console
CODE:
```
$ pip install https://github.com/celery/celery/zipball/main#egg=celery
```

LANGUAGE: console
CODE:
```
$ pip install https://github.com/celery/billiard/zipball/main#egg=billiard
```

LANGUAGE: console
CODE:
```
$ pip install https://github.com/celery/py-amqp/zipball/main#egg=amqp
```

LANGUAGE: console
CODE:
```
$ pip install https://github.com/celery/kombu/zipball/main#egg=kombu
```

LANGUAGE: console
CODE:
```
$ pip install https://github.com/celery/vine/zipball/main#egg=vine
```

----------------------------------------

TITLE: Start Celery Worker Consuming Specific Queues (CLI)
DESCRIPTION: Shows how to start a Celery worker instance and specify a comma-separated list of queues to consume from using the -Q option.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/workers.rst#_snippet_41

LANGUAGE: console
CODE:
```
$ celery -A proj worker -l INFO -Q foo,bar,baz
```

----------------------------------------

TITLE: Install Celery with Gevent Pool Dependencies
DESCRIPTION: This command installs the necessary Python packages: `gevent` for the asynchronous pool, `celery` for the distributed task queue, and `pybloom-live`.

SOURCE: https://github.com/celery/celery/blob/main/examples/gevent/README.rst#_snippet_0

LANGUAGE: bash
CODE:
```
$ python -m pip install gevent celery pybloom-live
```

----------------------------------------

TITLE: Start Celery Workers with Dedicated PID and Log Directories
DESCRIPTION: Demonstrates how to start Celery workers using "celery multi" while specifying dedicated directories for PID and log files to prevent conflicts and organize output.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_8

LANGUAGE: console
CODE:
```
$ mkdir -p /var/run/celery
$ mkdir -p /var/log/celery
$ celery multi start w1 -A proj -l INFO --pidfile=/var/run/celery/%n.pid --logfile=/var/log/celery/%n%I.log
```

----------------------------------------

TITLE: Install Celery via pip
DESCRIPTION: Installs the Celery distributed task queue library from the Python Package Index (PyPI) using pip, ensuring the package is updated to its latest stable version.

SOURCE: https://github.com/celery/celery/blob/main/docs/includes/installation.txt#_snippet_0

LANGUAGE: console
CODE:
```
$ pip install -U Celery
```

----------------------------------------

TITLE: Install and Configure Celery Consul K/V Store Backend
DESCRIPTION: Details the installation of the `python-consul2` library and provides examples for configuring Celery to use Consul as its result backend. It also explains the full URL syntax and its components, including the `one_client` option.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_95

LANGUAGE: console
CODE:
```
$ pip install python-consul2
```

LANGUAGE: Python
CODE:
```
CELERY_RESULT_BACKEND = 'consul://localhost:8500/'

or::

    result_backend = 'consul://localhost:8500/'
```

LANGUAGE: text
CODE:
```
consul://host:port[?one_client=1]
```

LANGUAGE: APIDOC
CODE:
```
Consul URL Components:
  host: Host name of the Consul server.
  port: The port the Consul server is listening to.
  one_client: By default, for correctness, the backend uses a separate client connection per operation. In cases of extreme load, the rate of creation of new connections can cause HTTP 429 "too many connections" error responses from the Consul server when under load. The recommended way to handle this is to enable retries in python-consul2 using the patch at https://github.com/poppyred/python-consul2/pull/31. Alternatively, if one_client is set, a single client connection will be used for all operations instead. This should eliminate the HTTP 429 errors, but the storage of results in the backend can become unreliable.
```

----------------------------------------

TITLE: Start Multiple Celery Workers with Custom Arguments using celery multi
DESCRIPTION: Illustrates starting multiple Celery workers with "celery multi", applying different queue and log level configurations to specific worker instances using advanced command-line syntax.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_9

LANGUAGE: console
CODE:
```
$ celery multi start 10 -A proj -l INFO -Q:1-3 images,video -Q:4,5 data
        -Q default -L:4,5 debug
```

----------------------------------------

TITLE: Example Celery Configuration Module
DESCRIPTION: Provides an example of a `celeryconfig.py` file, which defines configuration variables for a Celery application. This module can be loaded by `app.config_from_object()` to apply settings like `enable_utc` and `timezone`.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_9

LANGUAGE: python
CODE:
```
enable_utc = True
timezone = 'Europe/London'
```

----------------------------------------

TITLE: Install Celery with feature bundles via pip
DESCRIPTION: Installs Celery along with specific feature dependencies, known as bundles, using pip. This allows users to include support for various serializers, concurrency models, or transport/backend systems. Multiple bundles can be specified by separating them with commas inside the brackets.

SOURCE: https://github.com/celery/celery/blob/main/docs/includes/installation.txt#_snippet_1

LANGUAGE: console
CODE:
```
$ pip install "celery[librabbitmq]"
```

LANGUAGE: console
CODE:
```
$ pip install "celery[librabbitmq,redis,auth,msgpack]"
```

----------------------------------------

TITLE: Install Celery and Eventlet dependencies
DESCRIPTION: This command installs the necessary Python packages, `eventlet`, `celery`, and `pybloom-live`, required to run the Celery application with the Eventlet pool. It uses `pip` for package management.

SOURCE: https://github.com/celery/celery/blob/main/examples/eventlet/README.rst#_snippet_0

LANGUAGE: bash
CODE:
```
$ python -m pip install eventlet celery pybloom-live
```

----------------------------------------

TITLE: Install Celery with Consul result backend extension
DESCRIPTION: This command installs Celery along with the necessary dependencies to use Consul as a result backend, simplifying the setup process.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/whatsnew-4.0.rst#_snippet_34

LANGUAGE: console
CODE:
```
$ pip install celery[consul]
```

----------------------------------------

TITLE: Run Celery Event Capture via CLI
DESCRIPTION: This command line interface (CLI) example demonstrates how to start a Celery event consumer to capture events using a custom event handler. It specifies the Celery application, the event consumer class, and the frequency for event processing.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_36

LANGUAGE: bash
CODE:
```
celery -A proj events -c myapp.DumpCam --frequency=2.0
```

----------------------------------------

TITLE: Run RabbitMQ with Docker
DESCRIPTION: This Docker command starts a RabbitMQ container, mapping port 5672. It provides a quick way to get a RabbitMQ broker running for development or testing purposes.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_1

LANGUAGE: console
CODE:
```
$ docker run -d -p 5672:5672 rabbitmq
```

----------------------------------------

TITLE: Install setproctitle for Enhanced Celery Process Visibility
DESCRIPTION: This console command demonstrates how to install the `setproctitle` Python package. Installing this library allows Celery worker processes to display more descriptive names in `ps` listings, making it easier to identify different process types for debugging and management.

SOURCE: https://github.com/celery/celery/blob/main/docs/faq.rst#_snippet_19

LANGUAGE: Console
CODE:
```
$ pip install setproctitle
```

----------------------------------------

TITLE: Install Celery Flower Web Monitor
DESCRIPTION: This command uses pip, Python's package installer, to install the Flower web-based monitoring tool for Celery. It's a prerequisite for running Flower.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_19

LANGUAGE: console
CODE:
```
$ pip install flower
```

----------------------------------------

TITLE: Define a Simple Celery Application and Task
DESCRIPTION: This Python code demonstrates the most basic setup for a Celery application. It initializes a Celery instance named 'hello', configured to connect to an AMQP broker at localhost. A simple task, `hello`, is defined using the `@app.task` decorator, which returns the string 'hello world'. This example showcases Celery's ease of use and minimal configuration requirements.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/introduction.rst#_snippet_0

LANGUAGE: Python
CODE:
```
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'
```

----------------------------------------

TITLE: Run Celery HTTP Gateway Service
DESCRIPTION: Commands to start the Celery HTTP gateway service. The `syncdb` command is optional and only needed if using a database backend for Celery results. The `runserver` command starts the Django development server.

SOURCE: https://github.com/celery/celery/blob/main/examples/celery_http_gateway/README.rst#_snippet_0

LANGUAGE: Bash
CODE:
```
$ python manage.py syncdb
```

LANGUAGE: Bash
CODE:
```
$ python manage.py runserver
```

----------------------------------------

TITLE: Start Celery Flower with Custom Broker URL
DESCRIPTION: These commands demonstrate how to start the Flower web server while providing a custom broker URL. This is essential when Celery is configured to use a broker other than the default, such as RabbitMQ (AMQP) or Redis.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_22

LANGUAGE: console
CODE:
```
$ celery --broker=amqp://guest:guest@localhost:5672// flower
or
$ celery --broker=redis://guest:guest@localhost:6379/0 flower
```

----------------------------------------

TITLE: Install Celery with Amazon SQS Support
DESCRIPTION: Installs Celery along with its Amazon SQS dependencies using pip, leveraging the `celery[sqs]` bundle for a complete setup.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/backends-and-brokers/sqs.rst#_snippet_0

LANGUAGE: console
CODE:
```
$ pip install "celery[sqs]"
```

----------------------------------------

TITLE: Start Celery Workers in Background with celery multi
DESCRIPTION: Demonstrates how to start one or more Celery workers in the background using the "celery multi" command, specifying the application module and log level.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_4

LANGUAGE: console
CODE:
```
$ celery multi start w1 -A proj -l INFO
```

----------------------------------------

TITLE: Starting Celery Worker
DESCRIPTION: Command to start the Celery worker process. The `-A` flag specifies the Celery application instance to load, `worker` indicates the worker mode, and `-l INFO` sets the logging level to INFO for detailed output. The worker processes tasks from configured queues.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_2

LANGUAGE: console
CODE:
```
celery -A proj worker -l INFO
```

----------------------------------------

TITLE: Start Celery Worker with Gevent Pool
DESCRIPTION: This command starts the Celery worker in the `examples/gevent` directory, setting the log level to INFO, concurrency to 500, and specifying the `gevent` pool.

SOURCE: https://github.com/celery/celery/blob/main/examples/gevent/README.rst#_snippet_1

LANGUAGE: bash
CODE:
```
$ cd examples/gevent
$ celery worker -l INFO --concurrency=500 --pool=gevent
```

----------------------------------------

TITLE: Install RabbitMQ Server on Ubuntu/Debian
DESCRIPTION: This command installs the RabbitMQ message broker server on Ubuntu or Debian systems using `apt-get`. RabbitMQ is a stable and feature-complete choice for production environments.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_0

LANGUAGE: console
CODE:
```
$ sudo apt-get install rabbitmq-server
```

----------------------------------------

TITLE: Install and Configure Celery CouchDB Backend
DESCRIPTION: Provides instructions for installing the necessary Python library for the CouchDB backend and an example of how to configure Celery to use CouchDB as its result backend via a URL. It also details the components of the CouchDB connection URL.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_93

LANGUAGE: console
CODE:
```
$ pip install celery[couchdb]
```

LANGUAGE: Python
CODE:
```
result_backend = 'couchdb://username:password@host:port/container'
```

LANGUAGE: APIDOC
CODE:
```
CouchDB URL Components:
  username: User name to authenticate to the CouchDB server as (optional).
  password: Password to authenticate to the CouchDB server (optional).
  host: Host name of the CouchDB server. Defaults to localhost.
  port: The port the CouchDB server is listening to. Defaults to 8091.
  container: The default container the CouchDB server is writing to. Defaults to default.
```

----------------------------------------

TITLE: Run Celery Worker with Main Module Task
DESCRIPTION: Provides an example of a `tasks.py` file that defines a Celery task and includes logic to start a worker when the module is executed directly. This demonstrates how tasks are named with `__main__` when the module is run as a program.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_2

LANGUAGE: python
CODE:
```
from celery import Celery
app = Celery()

@app.task
def add(x, y): return x + y

if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)
```

----------------------------------------

TITLE: Link Celery tasks sequentially using chain
DESCRIPTION: Illustrates how to use `celery.chain` to link tasks together, so that the output of one task becomes the input of the next. Provides an example of a simple arithmetic chain.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_38

LANGUAGE: Python
CODE:
```
from celery import chain
from proj.tasks import add, mul

# (4 + 4) * 8
chain(add.s(4, 4) | mul.s(8))().get()
```

----------------------------------------

TITLE: Start Celery Multi-Node with Specific Concurrency per Index
DESCRIPTION: This Bash command demonstrates how to use "celery multi start" to launch multiple named nodes (A, B, C, D) and assign specific concurrency levels based on their index in the argument list. For example, node A (index 1) gets 4 processes, and nodes B, C, D (indices 2-4) each get 8 processes.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/changelog-3.1.rst#_snippet_28

LANGUAGE: bash
CODE:
```
celery multi start A B C D -c:1 4 -c:2-4 8
```

----------------------------------------

TITLE: Install Celery via pip
DESCRIPTION: This command installs the Celery library from PyPI using pip, the standard Python package installer. Celery is a Python-based task queue.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_3

LANGUAGE: console
CODE:
```
$ pip install celery
```

----------------------------------------

TITLE: Install django-celery-results Library
DESCRIPTION: This command installs the `django-celery-results` library, which provides result backends for Celery using Django's ORM or cache framework.

SOURCE: https://github.com/celery/celery/blob/main/docs/django/first-steps-with-django.rst#_snippet_9

LANGUAGE: console
CODE:
```
$ pip install django-celery-results
```

----------------------------------------

TITLE: Example Celery Configuration File (`celeryconfig.py`) (Python)
DESCRIPTION: Provides a comprehensive example of a `celeryconfig.py` file, defining essential Celery settings such as broker URL, result backend, task/result serialization, accepted content types, timezone, and UTC enablement. This file serves as a centralized configuration source.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_18

LANGUAGE: python
CODE:
```
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
```

----------------------------------------

TITLE: Start Celery Events Curses Interface
DESCRIPTION: Launches a curses-based interface for interactive monitoring of Celery events. This provides a more structured and real-time view of worker and task activities.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_54

LANGUAGE: console
CODE:
```
$ celery -A proj events
```

----------------------------------------

TITLE: Start Celery Flower Web Server (Custom Port)
DESCRIPTION: This command starts the Flower web server, explicitly specifying the port it should listen on using the `--port` argument. This is useful for avoiding port conflicts or running multiple instances.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_21

LANGUAGE: console
CODE:
```
$ celery -A proj flower --port=5555
```

----------------------------------------

TITLE: Get Celery CLI Help
DESCRIPTION: Displays a list of all available commands for the Celery command-line interface. This is useful for discovering new commands or recalling command syntax.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_0

LANGUAGE: console
CODE:
```
$ celery --help
```

----------------------------------------

TITLE: Installing Python Requirements for Celery Project
DESCRIPTION: This snippet provides the command to install all necessary Python dependencies for the Celery-Django project from the `requirements.txt` file. It assumes a local RabbitMQ server is running for message brokering.

SOURCE: https://github.com/celery/celery/blob/main/examples/django/README.rst#_snippet_0

LANGUAGE: console
CODE:
```
$ pip install -r requirements.txt
```

----------------------------------------

TITLE: Get Specific Celery Command Help
DESCRIPTION: Provides detailed help and usage information for a specific Celery command. Replace `<command>` with the name of the command you want to learn more about.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_1

LANGUAGE: console
CODE:
```
$ celery <command> --help
```

----------------------------------------

TITLE: Typical Celery Task State Progression
DESCRIPTION: Outlines the common state transitions for a typical Celery task. The 'STARTED' state is only recorded if `task_track_started` is enabled.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_26

LANGUAGE: Text
CODE:
```
PENDING -> STARTED -> SUCCESS
```

----------------------------------------

TITLE: Start Celery Events with Snapshot Camera
DESCRIPTION: This command starts the `celery events` monitor configured to use a specific snapshot camera class and a defined frequency for capturing events. Snapshot cameras are used for persistent event logging.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_26

LANGUAGE: console
CODE:
```
$ celery -A proj events --camera=<camera-class> --frequency=1.0
```

----------------------------------------

TITLE: Install and Configure Celery Couchbase Backend
DESCRIPTION: Instructions for installing the `couchbase` library for Celery and configuring the `result_backend` with a Couchbase connection URL.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_85

LANGUAGE: Shell
CODE:
```
$ pip install celery[couchbase]
```

LANGUAGE: Python
CODE:
```
result_backend = 'couchbase://username:password@host:port/bucket'
```

----------------------------------------

TITLE: Install Celery with Redis support
DESCRIPTION: This command installs Celery along with the necessary dependencies for Redis support, using the `celery[redis]` bundle via pip.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/backends-and-brokers/redis.rst#_snippet_0

LANGUAGE: console
CODE:
```
$ pip install -U "celery[redis]"
```

----------------------------------------

TITLE: Execute Celery `urlopen` Task for Single URL
DESCRIPTION: This snippet demonstrates how to navigate to the example directory and execute the `urlopen` task from an interactive Python session to fetch a URL and get its response body size.

SOURCE: https://github.com/celery/celery/blob/main/examples/gevent/README.rst#_snippet_2

LANGUAGE: bash
CODE:
```
$ cd examples/gevent
$ python
```

LANGUAGE: python
CODE:
```
>>> from tasks import urlopen
>>> urlopen.delay('https://www.google.com/').get()
```

----------------------------------------

TITLE: Example Celerybeat Configuration File
DESCRIPTION: Provides an example configuration for `/etc/default/celerybeat` for a Python project, specifying the Celery binary path, app instance, working directory, and additional beat options.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/daemonizing.rst#_snippet_5

LANGUAGE: bash
CODE:
```
# Absolute or relative path to the 'celery' command:
CELERY_BIN="/usr/local/bin/celery"
#CELERY_BIN="/virtualenvs/def/bin/celery"

# App instance to use
# comment out this line if you don't use an app
CELERY_APP="proj"
# or fully qualified:
#CELERY_APP="proj.tasks:app"

# Where to chdir at start.
CELERYBEAT_CHDIR="/opt/Myproject/"

# Extra arguments to celerybeat
CELERYBEAT_OPTS="--schedule=/var/run/celery/celerybeat-schedule"
```

----------------------------------------

TITLE: Instantiate Celery Application
DESCRIPTION: Demonstrates how to create a basic Celery application instance using the `Celery` class. The output shows the textual representation of the application object, including its class, main module, and memory address.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_0

LANGUAGE: pycon
CODE:
```
>>> from celery import Celery
>>> app = Celery()
>>> app
<Celery __main__:0x100469fd0>
```

----------------------------------------

TITLE: Console `celeryd-multi` Start Multiple Named Workers
DESCRIPTION: Example of using `celeryd-multi` to start multiple workers with custom, user-defined names, each running with a specified concurrency level.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/changelog-2.0.rst#_snippet_42

LANGUAGE: console
CODE:
```
$ celeryd-multi start image video data -c 3
celeryd -n image.myhost -c 3
celeryd -n video.myhost -c 3
celeryd -n data.myhost -c 3
```

----------------------------------------

TITLE: Full Celery Cassandra Backend Configuration Example (Python)
DESCRIPTION: This example provides a complete configuration for setting up Celery to use Cassandra as a result backend, specifying the backend URL, server addresses, keyspace, table, consistency levels, and entry TTL.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_63

LANGUAGE: Python
CODE:
```
result_backend = 'cassandra://'
cassandra_servers = ['localhost']
cassandra_keyspace = 'celery'
cassandra_table = 'tasks'
cassandra_read_consistency = 'QUORUM'
cassandra_write_consistency = 'QUORUM'
cassandra_entry_ttl = 86400
```

----------------------------------------

TITLE: Install Celery with Google Pub/Sub Support
DESCRIPTION: Install Celery and its Google Pub/Sub dependencies using pip. This command ensures all necessary packages are available for broker functionality.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/backends-and-brokers/gcpubsub.rst#_snippet_0

LANGUAGE: Shell
CODE:
```
pip install "celery[gcpubsub]"
```

----------------------------------------

TITLE: Define Custom Celery Inspect Command to Get Prefetch Count
DESCRIPTION: Demonstrates how to create a custom inspect command using the `@inspect_command` decorator. This example defines `current_prefetch_count`, which retrieves and returns the current task prefetch count from the worker's consumer state.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/workers.rst#_snippet_38

LANGUAGE: python
CODE:
```
from celery.worker.control import inspect_command

@inspect_command()
def current_prefetch_count(state):
    return {'prefetch_count': state.consumer.qos.value}
```

----------------------------------------

TITLE: Restart Celery Worker using celery multi
DESCRIPTION: Demonstrates how to start and restart a Celery worker instance using the `celery multi` command, suitable for development environments. It shows starting a worker with specific app, log level, and PID file, then restarting it.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/workers.rst#_snippet_8

LANGUAGE: console
CODE:
```
$ celery multi start 1 -A proj -l INFO -c4 --pidfile=/var/run/celery/%n.pid
$ celery multi restart 1 --pidfile=/var/run/celery/%n.pid
```

----------------------------------------

TITLE: Celery Task State: STARTED
DESCRIPTION: Describes the STARTED state for Celery tasks, indicating a task has begun execution. This state is not reported by default and requires enabling via `Task.track_started`. Includes metadata like process ID and hostname.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/tasks.rst#_snippet_51

LANGUAGE: APIDOC
CODE:
```
State: STARTED
Description: Task has been started.
Not reported by default, to enable please see @Task.track_started.
Meta-data: pid and hostname of the worker process executing the task.
```

----------------------------------------

TITLE: Install Celery from a downloaded source tarball
DESCRIPTION: Provides instructions for installing Celery by downloading and extracting its source code. This method involves building the package and then installing it, which may require privileged access if not using a virtual environment.

SOURCE: https://github.com/celery/celery/blob/main/README.rst#_snippet_5

LANGUAGE: Shell
CODE:
```
$ tar xvfz celery-0.0.0.tar.gz
$ cd celery-0.0.0
$ python setup.py build
# python setup.py install
```

----------------------------------------

TITLE: Celery Systemd Service Unit File Example
DESCRIPTION: This comprehensive example provides a `systemd` unit file (`celery.service`) for managing Celery as a background service. It defines the service's description, dependencies, execution type, user/group, working directory, and commands for starting, stopping, reloading, and restarting Celery workers, ensuring automatic restarts on failure.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/daemonizing.rst#_snippet_10

LANGUAGE: bash
CODE:
```
[Unit]
Description=Celery Service
After=network.target

[Service]
Type=forking
User=celery
Group=celery
EnvironmentFile=/etc/conf.d/celery
WorkingDirectory=/opt/celery
ExecStart=/bin/sh -c '${CELERY_BIN} -A $CELERY_APP multi start $CELERYD_NODES \
        --pidfile=${CELERYD_PID_FILE} --logfile=${CELERYD_LOG_FILE} \
        --loglevel="${CELERYD_LOG_LEVEL}" $CELERYD_OPTS'
ExecStop=/bin/sh -c '${CELERY_BIN} multi stopwait $CELERYD_NODES \
        --pidfile=${CELERYD_PID_FILE} --logfile=${CELERYD_LOG_FILE} \
        --loglevel="${CELERYD_LOG_LEVEL}"'
ExecReload=/bin/sh -c '${CELERY_BIN} -A $CELERY_APP multi restart $CELERYD_NODES \
        --pidfile=${CELERYD_PID_FILE} --logfile=${CELERYD_LOG_FILE} \
        --loglevel="${CELERYD_LOG_LEVEL}" $CELERYD_OPTS'
Restart=always

[Install]
WantedBy=multi-user.target
```

----------------------------------------

TITLE: Python Celery Single-Mode API Usage Example
DESCRIPTION: Provides an example of using Celery in its 'single-mode' API, which was prevalent before the introduction of the 'app' concept. This mode typically involves direct imports from Celery sub-modules and demonstrates a basic task definition.

SOURCE: https://github.com/celery/celery/blob/main/docs/internals/guide.rst#_snippet_4

LANGUAGE: python
CODE:
```
from celery import task
from celery.task.control import inspect

from .models import CeleryStats

@task
```

----------------------------------------

TITLE: Create a Basic Celery Application
DESCRIPTION: This snippet demonstrates how to initialize a minimal Celery application. It defines a Celery app instance, connects to a message broker (RabbitMQ in this example), and registers a simple task that returns 'hello world'.

SOURCE: https://github.com/celery/celery/blob/main/docs/includes/introduction.txt#_snippet_0

LANGUAGE: Python
CODE:
```
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'
```

----------------------------------------

TITLE: Initializing Celery App with app_or_default (Python)
DESCRIPTION: This example demonstrates using `celery.app.app_or_default` to initialize the app instance within a class. This function allows for an optional app argument, falling back to the default Celery app if none is provided. It ensures compatibility with both explicit app passing and module-based APIs.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_24

LANGUAGE: python
CODE:
```
from celery.app import app_or_default

class Scheduler:
        def __init__(self, app=None):
            self.app = app_or_default(app)
```

----------------------------------------

TITLE: Display Celery Command Line Help
DESCRIPTION: This command shows all available command-line options and arguments for the Celery program, providing comprehensive usage information.

SOURCE: https://github.com/celery/celery/blob/main/docs/django/first-steps-with-django.rst#_snippet_15

LANGUAGE: console
CODE:
```
$ celery --help
```

----------------------------------------

TITLE: Apply partial arguments to Celery task signatures
DESCRIPTION: Demonstrates how to apply partial arguments to a Celery task signature, prepending them to existing arguments to form a complete signature. Shows how to get the result of the delayed task.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_32

LANGUAGE: Python
CODE:
```
# resolves the partial: add(8, 2)
>>> res = s2.delay(8)
>>> res.get()
10
```

----------------------------------------

TITLE: Console: Starting Celery Worker with Specific Queues (`-Q`)
DESCRIPTION: This console command demonstrates how to start a Celery worker (`celeryd`) and specify the queues it should consume tasks from using the `-Q` option. In this example, the worker will process tasks from both 'video' and 'image' queues, enabling selective task routing.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/changelog-2.0.rst#_snippet_24

LANGUAGE: console
CODE:
```
$ celeryd -Q video, image
```

----------------------------------------

TITLE: Console `celeryd-multi` Start Multiple Workers with Queue and Log Level Configuration
DESCRIPTION: An advanced example demonstrating how to use `celeryd-multi` to start 10 workers with varied configurations. It shows assigning specific queues and log levels to different groups of workers.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/changelog-2.0.rst#_snippet_40

LANGUAGE: console
CODE:
```
$ celeryd-multi start 10 -l INFO -Q:1-3 images,video -Q:4,5:data -Q default -L:4,5 DEBUG
```

----------------------------------------

TITLE: Install Celery with Setuptools Extra Requirements using Pip
DESCRIPTION: This command demonstrates how to install Celery with specific extra requirements using pip's setuptools extras format. By specifying extras like 'redis' and 'mongodb' in brackets, users can install dependencies for various transports and result backends.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/whatsnew-3.1.rst#_snippet_14

LANGUAGE: console
CODE:
```
$ pip install celery[redis,mongodb]
```

----------------------------------------

TITLE: Install Documentation Build Dependencies
DESCRIPTION: Installs all necessary Python dependencies for building the project documentation, including both docs-specific requirements from `requirements/docs.txt` and default requirements.

SOURCE: https://github.com/celery/celery/blob/main/CONTRIBUTING.rst#_snippet_22

LANGUAGE: console
CODE:
```
pip install -U -r requirements/docs.txt
pip install -U -r requirements/default.txt
```

----------------------------------------

TITLE: Start Celery Flower Web Server (Default Port)
DESCRIPTION: This command initiates the Flower web server for a Celery project. It will typically run on the default port 5555, providing a real-time monitoring interface.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_20

LANGUAGE: console
CODE:
```
$ celery -A proj flower
```

----------------------------------------

TITLE: Celery Installation Bundles Reference
DESCRIPTION: A comprehensive reference of available Celery installation bundles, categorized by their function (serializers, concurrency, transports, and backends). Each entry describes the purpose of the bundle and the specific technology or feature it enables.

SOURCE: https://github.com/celery/celery/blob/main/README.rst#_snippet_4

LANGUAGE: APIDOC
CODE:
```
Serializers:
  celery[auth]: for using the auth security serializer.
  celery[msgpack]: for using the msgpack serializer.
  celery[yaml]: for using the yaml serializer.

Concurrency:
  celery[eventlet]: for using the eventlet pool.
  celery[gevent]: for using the gevent pool.

Transports and Backends:
  celery[amqp]: for using the RabbitMQ amqp python library.
  celery[redis]: for using Redis as a message transport or as a result backend.
  celery[sqs]: for using Amazon SQS as a message transport.
  celery[tblib]: for using the task_remote_tracebacks feature.
  celery[memcache]: for using Memcached as a result backend (using pylibmc)
  celery[pymemcache]: for using Memcached as a result backend (pure-Python implementation).
  celery[cassandra]: for using Apache Cassandra/Astra DB as a result backend with the DataStax driver.
  celery[azureblockblob]: for using Azure Storage as a result backend (using azure-storage)
  celery[s3]: for using S3 Storage as a result backend.
  celery[gcs]: for using Google Cloud Storage as a result backend.
  celery[couchbase]: for using Couchbase as a result backend.
  celery[arangodb]: for using ArangoDB as a result backend.
  celery[elasticsearch]: for using Elasticsearch as a result backend.
  celery[riak]: for using Riak as a result backend.
  celery[cosmosdbsql]: for using Azure Cosmos DB as a result backend (using pydocumentdb)
  celery[zookeeper]: for using Zookeeper as a message transport.
  celery[sqlalchemy]: for using SQLAlchemy as a result backend (supported).
  celery[pyro]: for using the Pyro4 message transport (experimental).
  celery[slmq]: for using the SoftLayer Message Queue transport (experimental).
  celery[consul]: for using the Consul.io Key/Value store as a message transport or result backend (experimental).
  celery[django]: specifies the lowest version possible for Django support. You should probably not use this in your requirements, it's here for informational purposes only.
  celery[gcpubsub]: for using Google Pub/Sub as a message transport.
```

----------------------------------------

TITLE: Display Celery Events Command Help
DESCRIPTION: This command shows the full list of available options and arguments for the `celery events` command. It's a standard way to get detailed usage information directly from the command line.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/monitoring.rst#_snippet_28

LANGUAGE: console
CODE:
```
$ celery events --help
```

----------------------------------------

TITLE: Install and Configure Celery ArangoDB Backend
DESCRIPTION: Instructions for installing the `pyArango` library for Celery and configuring the `result_backend` with an ArangoDB connection URL.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_87

LANGUAGE: Shell
CODE:
```
$ pip install celery[arangodb]
```

LANGUAGE: Python
CODE:
```
result_backend = 'arangodb://username:password@host:port/database/collection'
```

----------------------------------------

TITLE: Celery Task State Progression with Retries
DESCRIPTION: Illustrates the more complex state transitions for a Celery task that is retried multiple times, showing how 'RETRY' states are interleaved with 'STARTED' states.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_27

LANGUAGE: Text
CODE:
```
PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS
```

----------------------------------------

TITLE: Celery CLI: Displaying Help for Worker and Main Commands
DESCRIPTION: These console commands demonstrate how to access the help documentation for the Celery worker and the main Celery command-line interface. They provide a comprehensive list of available options and subcommands for troubleshooting and configuration.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_6

LANGUAGE: console
CODE:
```
$  celery worker --help
```

LANGUAGE: console
CODE:
```
$ celery --help
```

----------------------------------------

TITLE: Define Celery Sub-command Entry-point in setup.py
DESCRIPTION: This example demonstrates how to register a new `celery` sub-command (e.g., `flower`) using `setuptools entry_points` within a `setup.py` file. This mechanism allows external packages to extend Celery's CLI.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/extending.rst#_snippet_33

LANGUAGE: python
CODE:
```
setup(
        name='flower',
        entry_points={
            'celery.commands': [
               'flower = flower.command:flower',
            ],
        }
    )
```

----------------------------------------

TITLE: Starting the Celery Worker for Django Project
DESCRIPTION: This command initiates the Celery worker process for the Django project. The `-A proj` flag specifies the Celery application instance, and `-l INFO` sets the logging level to informational messages.

SOURCE: https://github.com/celery/celery/blob/main/examples/django/README.rst#_snippet_1

LANGUAGE: console
CODE:
```
$ celery -A proj worker -l INFO
```

----------------------------------------

TITLE: Access Celery Application Configuration
DESCRIPTION: Illustrates how to access configuration settings directly from the `app.conf` attribute of a Celery application. This example shows how to retrieve the current `timezone` setting.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_5

LANGUAGE: pycon
CODE:
```
>>> app.conf.timezone
'Europe/London'
```

----------------------------------------

TITLE: Install Celery Project Test Requirements
DESCRIPTION: These commands install or upgrade both the default and test-specific Python dependencies for the Celery project. This setup is essential before executing the full unittest suite, ensuring all necessary testing tools and libraries are available.

SOURCE: https://github.com/celery/celery/blob/main/requirements/README.rst#_snippet_1

LANGUAGE: Shell
CODE:
```
$ pip install -U -r requirements/default.txt
$ pip install -U -r requirements/test.txt
```

----------------------------------------

TITLE: Start Celery worker with Eventlet pool and concurrency
DESCRIPTION: This command initializes the Celery worker from the `examples/eventlet` directory. It configures the worker to use the Eventlet pool, sets the log level to INFO, and specifies a high concurrency of 500 for efficient asynchronous task processing.

SOURCE: https://github.com/celery/celery/blob/main/examples/eventlet/README.rst#_snippet_1

LANGUAGE: bash
CODE:
```
$ cd examples/eventlet
$ celery worker -l INFO --concurrency=500 --pool=eventlet
```

----------------------------------------

TITLE: Celery Signature API: apply_async method
DESCRIPTION: Documents the `apply_async` method of Celery signatures, explaining its parameters for optional partial arguments, partial keyword arguments, and execution options.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_34

LANGUAGE: APIDOC
CODE:
```
sig.apply_async(args=(), kwargs={}, **options)
  Calls the signature with optional partial arguments and partial
  keyword arguments. Also supports partial execution options.
```

----------------------------------------

TITLE: Dump Celery Events to Console
DESCRIPTION: Starts an event dumper that outputs raw event messages from workers to the console. This command is used to observe worker activities once events have been enabled.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_53

LANGUAGE: console
CODE:
```
$ celery -A proj events --dump
```

----------------------------------------

TITLE: Example Celery Configuration in Django settings.py
DESCRIPTION: This example demonstrates how to define Celery-specific configuration options within a Django project's `settings.py` file. These settings, prefixed with `CELERY_`, are automatically picked up by the Celery app when configured via `app.config_from_object`.

SOURCE: https://github.com/celery/celery/blob/main/docs/django/first-steps-with-django.rst#_snippet_3

LANGUAGE: Python
CODE:
```
...

# Celery Configuration Options
CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
```

----------------------------------------

TITLE: Create a partial Celery chain
DESCRIPTION: Demonstrates how to create a partial chain, allowing an initial argument to be passed when the chain is invoked, which then flows through the linked tasks.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_39

LANGUAGE: Python
CODE:
```
# (? + 4) * 8
g = chain(add.s(4) | mul.s(8))
g(4).get()
```

----------------------------------------

TITLE: Celery Control: add_consumer Method
DESCRIPTION: API documentation for the add_consumer method within Celery's control module, used to dynamically instruct workers to start consuming from a specified queue.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/workers.rst#_snippet_44

LANGUAGE: APIDOC
CODE:
```
celery.control.add_consumer(
  queue: str,
  reply: bool = False,
  destination: list[str] = None,
  exchange: str = None,
  exchange_type: str = None,
  routing_key: str = None,
  options: dict = None
)

Parameters:
  queue (str): The name of the queue to start consuming from.
  reply (bool): Whether to wait for a reply from the workers (default: False).
  destination (list[str]): A list of worker names to target (e.g., ['worker1@example.com']). If None, targets all workers.
  exchange (str): The name of the exchange to bind the queue to.
  exchange_type (str): The type of the exchange (e.g., 'topic', 'direct', 'fanout').
  routing_key (str): The routing key for the queue binding.
  options (dict): A dictionary of additional queue options (e.g., 'queue_durable', 'exchange_durable').

Returns:
  list[dict]: A list of dictionaries containing replies from targeted workers, if reply=True.
```

----------------------------------------

TITLE: Load Celery Configuration from Module with `config_from_object` (Python)
DESCRIPTION: Shows how to configure a Celery instance by loading settings from a dedicated Python module (e.g., 'celeryconfig') using `app.config_from_object`. This approach centralizes configuration for larger projects, enabling easier management and sysadmin control.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_17

LANGUAGE: python
CODE:
```
app.config_from_object('celeryconfig')
```

----------------------------------------

TITLE: Get Celery Configuration as Dictionary
DESCRIPTION: Shows how to retrieve the Celery application's configuration as a dictionary using `app.conf.table()`, with sensitive keys censored. This allows programmatic access to configuration settings.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_15

LANGUAGE: pycon
CODE:
```
>>> app.conf.table(with_defaults=False, censored=True)
```

----------------------------------------

TITLE: Initializing Celery App with Broker URL
DESCRIPTION: Demonstrates how to initialize a Celery application instance by directly providing the broker URL during instantiation. This simplifies configuration for common broker setups.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/whatsnew-3.0.rst#_snippet_33

LANGUAGE: python
CODE:
```
app = Celery(broker='redis://')
```

----------------------------------------

TITLE: Celery Worker Initialization and Shutdown Logs
DESCRIPTION: This log output illustrates the lifecycle of a Celery worker and consumer with a custom step installed. It shows the 'initializing', 'starting', 'stopping', and 'shutting down' phases, highlighting how custom steps interact with the worker's boot process and the redirection of print statements to logging.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/extending.rst#_snippet_28

LANGUAGE: text
CODE:
```
<Worker: w@example.com (initializing)> is in init
<Consumer: w@example.com (initializing)> is in init
[2013-05-29 16:18:20,544: WARNING/MainProcess]
    <Worker: w@example.com (running)> is starting
[2013-05-29 16:18:21,577: WARNING/MainProcess]
    <Consumer: w@example.com (running)> is starting
<Consumer: w@example.com (closing)> is stopping
<Worker: w@example.com (closing)> is stopping
<Consumer: w@example.com (terminating)> is shutting down
```

----------------------------------------

TITLE: Run Celery Worker with Environment Variable Configuration
DESCRIPTION: Example of running a Celery worker process, specifying the configuration module via the `CELERY_CONFIG_MODULE` environment variable directly in the console.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_13

LANGUAGE: console
CODE:
```
$ CELERY_CONFIG_MODULE="celeryconfig.prod" celery worker -l INFO
```

----------------------------------------

TITLE: Example Configuration for Celeryd Init-Script
DESCRIPTION: An example `/etc/default/celeryd` configuration file for a Python project. This bash script defines various settings for the Celery worker daemon, including node names, binary path, application instance, working directory, command-line options, logging, PID files, and user/group permissions.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/daemonizing.rst#_snippet_2

LANGUAGE: bash
CODE:
```
# Names of nodes to start
#   most people will only start one node:
CELERYD_NODES="worker1"
#   but you can also start multiple and configure settings
#   for each in CELERYD_OPTS
#CELERYD_NODES="worker1 worker2 worker3"
#   alternatively, you can specify the number of nodes to start:
#CELERYD_NODES=10

# Absolute or relative path to the 'celery' command:
CELERY_BIN="/usr/local/bin/celery"
#CELERY_BIN="/virtualenvs/def/bin/celery"

# App instance to use
# comment out this line if you don't use an app
CELERY_APP="proj"
# or fully qualified:
#CELERY_APP="proj.tasks:app"

# Where to chdir at start.
CELERYD_CHDIR="/opt/Myproject/"

# Extra command-line arguments to the worker
CELERYD_OPTS="--time-limit=300 --concurrency=8"
# Configure node-specific settings by appending node name to arguments:
#CELERYD_OPTS="--time-limit=300 -c 8 -c:worker2 4 -c:worker3 2 -Ofair:worker1"

# Set logging level to DEBUG
#CELERYD_LOG_LEVEL="DEBUG"

# %n will be replaced with the first part of the nodename.
CELERYD_LOG_FILE="/var/log/celery/%n%I.log"
CELERYD_PID_FILE="/var/run/celery/%n.pid"

# Workers should run as an unprivileged user.
#   You need to create this user manually (or you can choose
#   a user/group combination that already exists (e.g., nobody).
CELERYD_USER="celery"
CELERYD_GROUP="celery"

# If enabled pid and log directories will be created if missing,
```

----------------------------------------

TITLE: Celery Application Configuration API
DESCRIPTION: API documentation for configuring the Celery application instance, including methods for loading configuration from objects, modules, and environment variables.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_17

LANGUAGE: APIDOC
CODE:
```
Celery:
  config_from_object(obj: Union[str, object])
    obj: A module object, a class object, or a fully qualified string name (e.g., 'module:Config').
    Description: Loads configuration from a Python object or module.

  config_from_envvar(variable_name: str)
    variable_name: The name of the environment variable containing the configuration module name.
    Description: Loads configuration from a module specified by an environment variable.
```

----------------------------------------

TITLE: Configure Separate Read/Write Broker URLs in Celery
DESCRIPTION: Example Python code showing how to configure distinct broker URLs for read and write operations, which can be useful for advanced broker setups or load balancing.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_111

LANGUAGE: Python
CODE:
```
broker_read_url = 'amqp://user:pass@broker.example.com:56721'
broker_write_url = 'amqp://user:pass@broker.example.com:56722'
```

----------------------------------------

TITLE: Start Celery Worker in Foreground
DESCRIPTION: This command initiates a Celery worker process in the foreground. It requires specifying the application module ("-A proj") and sets the logging verbosity to INFO.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/workers.rst#_snippet_0

LANGUAGE: console
CODE:
```
$ celery -A proj worker -l INFO
```

----------------------------------------

TITLE: Install Celery Router Function by Name String
DESCRIPTION: This Python example demonstrates an alternative way to register a custom router function by providing its fully qualified name as a string in the `task_routes` setting.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/routing.rst#_snippet_41

LANGUAGE: python
CODE:
```
task_routes = ('myapp.routers.route_task',)
```

----------------------------------------

TITLE: Install Celery with zstd Support
DESCRIPTION: This command shows how to install Celery with `zstd` compression support, enabling the use of the zstd algorithm for improved compression ratios and performance in real-time scenarios.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/calling.rst#_snippet_33

LANGUAGE: console
CODE:
```
$ pip install celery[zstd]
```

----------------------------------------

TITLE: Displaying Celery Worker Help Options
DESCRIPTION: Command to display all available command-line options and arguments for the Celery worker. This provides comprehensive information on configuring worker behavior, including options for broker selection, concurrency, event monitoring, and queue management.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_3

LANGUAGE: console
CODE:
```
celery worker --help
```

----------------------------------------

TITLE: Create a Simple Celery Application
DESCRIPTION: This Python snippet demonstrates the minimal setup required to create a basic Celery application. It initializes a Celery app instance, connecting to a message broker, and defines a simple task using the `@app.task` decorator. The task, named `hello`, returns a string.

SOURCE: https://github.com/celery/celery/blob/main/README.rst#_snippet_0

LANGUAGE: python
CODE:
```
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'
```

----------------------------------------

TITLE: Install Celery with Brotli Compression Support
DESCRIPTION: Command to install Celery with brotli compression support. Brotli is optimized for web content and small text documents, providing efficient compression for static assets.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/calling.rst#_snippet_27

LANGUAGE: console
CODE:
```
$ pip install celery[brotli]
```

----------------------------------------

TITLE: Install Celery with Cassandra result backend extension
DESCRIPTION: This command installs Celery with the `cassandra` extension, enabling the use of Cassandra as a result backend, utilizing the new `cassandra-driver` library.

SOURCE: https://github.com/celery/celery/blob/main/docs/history/whatsnew-4.0.rst#_snippet_35

LANGUAGE: console
CODE:
```
$ pip install celery[cassandra]
```

----------------------------------------

TITLE: Run Django Migrations for django_celery_results
DESCRIPTION: After adding `django_celery_results` to `INSTALLED_APPS`, run this Django management command to create the necessary database tables for the result backend.

SOURCE: https://github.com/celery/celery/blob/main/docs/django/first-steps-with-django.rst#_snippet_11

LANGUAGE: console
CODE:
```
$ python manage.py migrate django_celery_results
```

----------------------------------------

TITLE: Illustrate Celery Task Lazy Evaluation
DESCRIPTION: This example demonstrates the lazy evaluation of Celery tasks. The task object is initially a `PromiseProxy` and is only fully evaluated when accessed or used, such as when `repr()` is called.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/application.rst#_snippet_16

LANGUAGE: pycon
CODE:
```
>>> @app.task
>>> def add(x, y):
...    return x + y

>>> type(add)
<class 'celery.local.PromiseProxy'>

>>> add.__evaluated__()
False

>>> add        # <-- causes repr(add) to happen
<@task: __main__.add>

>>> add.__evaluated__()
True
```

----------------------------------------

TITLE: Create a partial Celery group
DESCRIPTION: Shows how to create a partial group, where additional arguments can be passed when the group is called, which are then applied to each task within the group.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/next-steps.rst#_snippet_37

LANGUAGE: Python
CODE:
```
g = group(add.s(i) for i in range(10))
g(10).get()
```

----------------------------------------

TITLE: Install and Configure Celery IronCache Backend
DESCRIPTION: Instructions for installing the `iron_celery` library and configuring Celery's `result_backend` to use IronCache, including options for specifying a custom cache name.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_84

LANGUAGE: Shell
CODE:
```
$ pip install iron_celery
```

LANGUAGE: Python
CODE:
```
result_backend = 'ironcache://project_id:token@'

ironcache:://project_id:token@/awesomecache
```

----------------------------------------

TITLE: Example Configuration for GCS Result Backend
DESCRIPTION: Demonstrates a complete configuration for using Google Cloud Storage as a Celery result backend, including bucket name, project, base path, and time-to-live settings.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_79

LANGUAGE: Python
CODE:
```
gcs_bucket = 'mybucket'
gcs_project = 'myproject'
gcs_base_path = '/celery_result_backend'
gcs_ttl = 86400
```

----------------------------------------

TITLE: Celery Database Result Backend Specific Examples
DESCRIPTION: Provides concrete examples of configuring the Celery result backend for various database types, including SQLite, MySQL, PostgreSQL, and Oracle. Each example demonstrates the correct connection string format for the respective database.

SOURCE: https://github.com/celery/celery/blob/main/docs/userguide/configuration.rst#_snippet_37

LANGUAGE: python
CODE:
```
# sqlite (filename)
result_backend = 'db+sqlite:///results.sqlite'

# mysql
result_backend = 'db+mysql://scott:tiger@localhost/foo'

# postgresql
result_backend = 'db+postgresql://scott:tiger@localhost/mydatabase'

# oracle
result_backend = 'db+oracle://scott:tiger@127.0.0.1:1521/sidname'
```

----------------------------------------

TITLE: Verify Celery Configuration File Syntax (Console)
DESCRIPTION: Illustrates how to check a Celery configuration file for syntax errors by attempting to import it as a Python module from the console. This simple command helps ensure the configuration is valid before deploying the Celery application.

SOURCE: https://github.com/celery/celery/blob/main/docs/getting-started/first-steps-with-celery.rst#_snippet_19

LANGUAGE: console
CODE:
```
$ python -m celeryconfig
```