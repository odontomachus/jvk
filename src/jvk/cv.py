import argparse
import gettext
from yaml import load, dump

from jinja2 import (
    Environment,
    FileSystemLoader,
    )

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

loader = FileSystemLoader(searchpath='templates')
env = Environment(loader=loader, extensions=['jinja2.ext.i18n'])
env.install_null_translations()

def render(_input):
    with _input as cvsrc:
        cv = load(cvsrc, Loader=Loader)
        page = {
            'title': 'CV Jonathan Villemaire-Krajden',
            'head': {
                'css': [
                    {'href': '/static/vendor/fonts/Serif/cmun-serif.css'},
                    {'href': '/static/css/cv.css'},
                ]}}
    return env.get_template('cv.j2').render(cv=cv, conf=cv['meta'], page=page)


if __name__ == "__main__":
    import argparse
    argparser = argparse.ArgumentParser(description='Render my resume.')
    argparser.add_argument('input', type=argparse.FileType('r'))
    argparser.add_argument('out', type=argparse.FileType('w'))

    args = argparser.parse_args()
    _input = args.input
    out = args.out
    out.write(render(_input))
