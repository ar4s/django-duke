`django-duke` uses the [django-configuration](https://django-configurations.readthedocs.io/en/stable) package to manage configuration.
This means that the first thing you need to do is install `django-configuration` and `django-duke`:

```bash
pip install django-configuration django-duke
# or
poetry add django-configuration django-duke
```

Then, you need to modify a `settings.py`, `manage.py`, `wsgi.py` and `asgi.py` file in your project's root directory according to the [django-configuration documentation](https://django-configurations.readthedocs.io/en/stable/#quickstart).

Next step is to get Duke's configuration class. You can do this by importing `DukeConfiguration` from `django-duke`:

```python
# settings.py
from configurations import Configuration
from duke import get_configuration_class

DukeConfiguration = get_configuration_class()

class Base(DukeConfiguration, Configuration):
    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            ...
        ]
    @property
    def MIDDLEWARE(self):
        return super().MIDDLEWARE + [
            ...
        ]
```

!!! notice
    You need to inherit from `DukeConfiguration` before `Configuration` to make sure that Duke's configuration is applied first.

    Also you need to use `@property` decorator for `INSTALLED_APPS` and `MIDDLEWARE` properties to make sure that Duke's configuration is applied after your project's configuration.

And finally, you need unpack urls from `duke.urls` into your project's `urls.py`:

```python
# urls.py
from duke import get_urls

urlpatterns = [
    ...
    *get_urls(),
    ...
]
# or
urlpatterns += get_urls()
```
Now you can install Duke's plugins and start using them.
Check out the [plugins](/plugins) section for more information.
