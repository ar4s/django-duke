## django-duke-browser-reload
Popular application for automatic browser reload when files are changed.

!!! warning

    This plugin is not recommended to be working in production environment.
    Pay attention to the installation command, it is installed **only** in the dev group.

### Installation command
```bash
poetry add --group dev install django-duke-browser-reload
```

### Configuration
n/a

### Resources
  - [django-browser-loader code](https://github.com/adamchainz/django-browser-reload)


## django-duke-debug-toolbar
Must have application for debugging Django project.

!!! warning

    This plugin is not recommended to be working in production environment.
    Pay attention to the installation command, it is installed **only** in the dev group.

### Installation command
```bash
poetry add --group dev install django-duke-debug-toolbar
```

### Configuration
Export environment variables:

  - `DEBUG_TOOLBAR_INTERNAL_IPS` - list of IP addresses that have access to the debug toolbar (default: `127.0.0.1`)

### Resources
  - [django-debug-toolbar code](https://github.com/jazzband/django-debug-toolbar/)
  - [Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)

## django-duke-sentry
Good for tracking errors in production.

### Installation command
```bash
poetry add install django-duke-sentry
```
### Configuration
Export environment variables:

  - `SENTRY_DSN` - DSN for Sentry project.

### Resources
  - [sentry code](https://github.com/getsentry/sentry)
  - [Documentation](https://docs.sentry.io/platforms/python/integrations/django/)


## TODO
  - django-duke-dramatiq
  - django-duke-extensions
