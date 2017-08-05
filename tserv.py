#!/usr/bin/env python
"""
Starts a Tornado static file server in a given directory.
To start the server in the current directory:
    tserv .
Then go to http://localhost:8000 to browse the directory.
Use the --prefix option to add a prefix to the served URL,
for example to match GitHub Pages' URL scheme:
    tserv . --prefix=jiffyclub
Then go to http://localhost:8000/jiffyclub/ to browse.
Use the --port option to change the port on which the server listens.
"""

from __future__ import print_function

import os
import sys
from argparse import ArgumentParser

import tornado.ioloop
import tornado.web


class Handler(tornado.web.StaticFileHandler):
    def parse_url_path(self, url_path):
        if not url_path.startswith('static'):
            url_path = 'html/'+url_path+'.html'
        else:
            url_path = url_path[7:]
        if not url_path or url_path.endswith('/'):
            url_path = url_path + '.html'
        return url_path


def mkapp(prefix=''):
    if prefix:
        path = '/' + prefix + '/(.*)'
    else:
        path = '/(.*)'

    application = tornado.web.Application([
        (path, Handler, {'path': os.getcwd()}),
    ], debug=True)

    return application


def start_server(prefix='', port=8000):
    app = mkapp(prefix)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()


def parse_args(args=None):
    parser = ArgumentParser(
        description=(
            'Start a Tornado server'
        )
    )
    parser.add_argument(
        '-p', '--port', type=int, default=8000,
        help='Port on which to run server.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    os.chdir('static')
    print('Starting server on port {}'.format(args.port))
    start_server(port=args.port)


if __name__ == '__main__':
    sys.exit(main())
