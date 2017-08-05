import gettext
from jinja2 import (
    Environment,
    FileSystemLoader,
)

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Renderer:
    def __init__(self, content_dir='../../content/', output_dir='../../static/html'):
        loader = FileSystemLoader(searchpath='templates')
        self.defaults = {'translations': {}, 'sections': {'en': [], 'fr': []}}
        self.env = Environment(loader=loader, extensions=['jinja2.ext.i18n'])
        self.env.install_null_translations()
        self.queue = []
        self.content_dir = content_dir
        self.output_dir = output_dir

    def read_content(self, source):
        with open(self.content_dir + source) as content_file:
            return content_file.read()

    def add(self, path, *args, **kwargs):
        if 'section' in kwargs and kwargs['section']:
            lang = kwargs['lang']
            section = {'href': path,
                       'title': kwargs['title']}
            try:
                section.update(kwargs['section'])
            except:
                pass
            self.defaults['sections'][lang].append(section)
        args = tuple([path]+list(args))
        self.queue.append((args, kwargs))


    def render_all(self):
        for args, kwargs in self.queue:
            self.render(*args, **kwargs)

    def render(self, path, template, **kwargs):
        kwargs = {**self.defaults, **kwargs}
        page = self.env.get_template(template).render(path=path, **kwargs)
        with open(self.output_dir + path + '.html', 'w') as out:
            out.write(page)


if __name__ == "__main__":
    import argparse
    argparser = argparse.ArgumentParser(description='Render my resume.')
    argparser.add_argument('input', type=argparse.FileType('r'))
    argparser.add_argument('out', type=argparse.FileType('w'))

    args = argparser.parse_args()
    _input = args.input
    out = args.out
    out.write(render(_input))
