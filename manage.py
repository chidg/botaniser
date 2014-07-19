#!/usr/bin/env python
import os
import sys

if os.environ['USER'] == 'ubuntu':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "botaniser.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "botaniser.settings.dev")


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
