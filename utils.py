import jinja2
import os


JINJA_ENV = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


def _datetime_format(value, format='%H:%M / %d-%m-%Y'):
    '''Renders datetime in proper format.

    Args:
      value: (datetime)datetime object.
      format(optional): (string)format of datetime(default: '%H:%M / %d-%m-%Y').

    Returns:
      (string)formated datetime string.
    '''
    return value.strftime(format)

JINJA_ENV.filters['datetime'] = _datetime_format


def render(tmpl, context):
    '''Renders context into tmpl.

    Args:
      tmpl: (string)template path.
      context: (dict)dictinory containing context variables.

    Returns:
      (string)rendered string.
    '''
    template = JINJA_ENV.get_template(tmpl)
    return template.render(context)
