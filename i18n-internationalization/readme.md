# What is internationalization? (i18n)

Is the process of designing and developing software, websites, or other digital
products to be adaptable to different languages, cultures, and regions without
requiring major changes to the code or structure of the product. The goal of
internationalization is to create a product that can be easily translated and
localized for different markets and audiences, and that can accommodate
different writing systems, date and time formats, and other cultural
conventions.

In summary, internationalization involves separating the content and user
interface elements of a product from the code that controls its functionality,
so that they can be easily translated and adapted to different languages and
regions. This typically involves using standardized formats for text, dates, and
other data. This is complemented by designing the product with flexibility and
scalability in mind. Once the application has been internationalized, it can be
localized for specific markets by translating the content and customizing the
user interface to suit the needs of users in different countries or regions.

## Internatiolization in Python

### The `_()` approach

This approach uses `gettext` function to wrap the text to be translated to create
the `.mo`, `.pot` and `.po` files for the translation.

This approach is based on the GNU gettext library, and can be used with the
pygettext module included in Python. By wrapping the text in gettext function
calls, you can easily create the necessary locale files for each language
translation.

Using this approach, helps to maintain separate translations for each language,
making your application more accessible and user-friendly for a wider audience.

Additionally, this method allows for easy updates and modifications to the
translations, simplifying the process of maintaining your multilingual web
application.

This feature is not only for Django, it can be used just with Python.

### Translation inside Django

Django provides robust support for internationalization and localization through
its i18n framework. This framework includes a powerful set of tools and
utilities to make your web application accessible to users. This feature includes
language and location settings.

One of the key features of Django's i18n framework is its built-in support for
translations. With this feature, it is easy to create and manage translations
for an application text and content. This includes everything from simple
strings and messages, to more complex content like templates and user-facing
documentation.

To get started with translations in Django, an approach is to us `gettext`
function to wrap the text you want to translate, and then generate the necessary
`.mo`, `.pot`, and `.po` files for each language translation, similar to the
previous approach. You can also use the `gettext_lazy` function to translate text
in models, forms, and other places where strings are evaluated lazily.

Django's i18n framework provides several ways to translate text within your web
application, including the `{% translate %}` template tag. This tag allows you to
mark up text within your templates that should be translated, making it easy to
maintain and update translations as your application evolves.

To use the {% translate %} tag, simply surround the text you want to translate
with the tag, like so:

```py
{% translate "Hello, world!" %}
```

In addition to the `{% translate %}` tag, Django's i18n framework also provides
several other template tags and filters for handling translations, including `{%
blocktrans %}`, `{% trans %}`, and `{% pluralize %}`. These tags and filters
provide additional flexibility and functionality for handling translations in
your templates.
