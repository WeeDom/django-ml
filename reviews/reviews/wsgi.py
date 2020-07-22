"""
WSGI config for reviews project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import inspect
from reviews.ml.registry import MLRegistry
from reviews.ml.income_classifier.random_forest import RandomForestClassifier
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews.settings')

application = get_wsgi_application()

try:
    registry = MLRegistry()
    #  Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML regstry
    registry.add_algorithm(
        endpoint_name="income_classifier",
        algorithm_object=rf,
        algorithm_name="random forest",
        algorithm_status="production",
        algorithm_version="0.0.1",
        owner="WeeDom",
        algorithm_description="Random Forest with simple pre- and post-processing",  # noqa 501
        algorithm_code=inspect.getsource(RandomForestClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
