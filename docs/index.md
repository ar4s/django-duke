# django-duke

django-duke allows you to easily integrate predefined plugins into your Django project.
Main idea is to achive zero-configuration approach and simplify installation process of popular application.

## Why?
When you start a new Django project, you usually need to install some apps and configure them.
For example, you need to install `django-debug-toolbar` and add it to `INSTALLED_APPS` and `MIDDLEWARE` settings
and add `INTERNAL_IPS` setting. Of course, you can copy-paste this configuration from some other project,
but it's not very convenient. django-duke allows you to install `django-duke-debug-toolbar` package and it will
automatically add `django-debug-toolbar` to `INSTALLED_APPS` and `MIDDLEWARE` and `INTERNAL_IPS` settings.

Wait! You forget about add paths to `urls.py` file... and Duke will do it for you!

## How it works?
django-duke utilizes Python's entrypoint mechanism to find plugins.
In short, it searches for `duke.plugins` entrypoint in all installed packages and loads them.

## What is a plugin?
Plugin in django-duke is a tiny python package that contains configuration for some app.
It can be a django app, for example `django-duke-debug-toolbar` - it contains configuration for `debug_toolbar` app.

