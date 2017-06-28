import os

import http.server
from http.server import SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        print(":path is: " + path)
        if path[1:3] in ('en', 'fr'):
            path = os.path.join(self.static_root, 'html', path[1:]+'.html')
        elif path.startswith('/static/'):
            path = os.path.join(self.static_root, path[8:])
            print(path)
        return path

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='../../static')
    args = ap.parse_args()
    Handler.static_root = args.root

    server = http.server.HTTPServer(('127.0.0.1', 8000), Handler)
    server.serve_forever()
