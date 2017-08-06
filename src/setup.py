from distutils.core import setup
from babel.messages import frontend as babel

from setuptools import setup, find_packages
setup(
    name="jvk",
    version="0.1",
    install_requires=[
        'jinja2',
        'babel'
        ],
    scripts=['jvk/site.py'],
    author="Jonathan Villemaire-Krajden",
    author_email="jonathan@j-vk.com",
    description="Personal website",
    license="MIT",
    keywords="Personal site",
    url="https://j-vk.com/",
    cmdclass = {'compile_catalog': babel.compile_catalog,
                'extract_messages': babel.extract_messages,
                'init_catalog': babel.init_catalog,
                'update_catalog': babel.update_catalog},
    message_extractors = {
        'messages': [
            ('jvk/templates/**.j2',                'jinja2', None),
            ]
    }
)
