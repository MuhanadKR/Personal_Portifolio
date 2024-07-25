#!/bin/bash

# Activate the virtual environment
source djangoenv/Scripts/activate

# Run the collectstatic command
python manage.py collectstatic --noinput