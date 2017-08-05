from renderer import Renderer
renderer = Renderer()
add = renderer.add
r = renderer.read_content

from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
def from_yaml(source):
    with open('../../content/' + source) as yaml_source:
        return load(yaml_source, Loader=Loader)

cv_css = [
    {'href': '/static/vendor/fonts/Serif/cmun-serif.css'},
    {'href': '/static/css/cv.css'},
]

add(path='/index', template="simple.j2", content=r('root.html'), title='Jonathan Villemaire-Krajden')
add(path='/en', template="home.j2", content=r('home.en.html'), lang='en', title='Jonathan Villemaire-Krajden', translations={'fr':'/fr'})
add(path='/fr', template="home.j2", content=r('home.fr.html'), lang='fr', title='Jonathan Villemaire-Krajden', translations={'en':'/en'})

add(path='/en/resume', template="cv.j2", cv=from_yaml('cv-en.yaml'), lang='en', title='Resume | Jonathan Villemaire-Krajden', translations={'fr':'/fr/cv'}, css=cv_css, section={'title': 'Resume'})
add(path='/fr/cv', template="cv.j2", cv=from_yaml('cv-fr.yaml'), lang='fr', title='CV | Jonathan Villemaire-Krajden', translations={'en':'/en/resume'}, css=cv_css, section={'title': 'CV'})

renderer.render_all()
