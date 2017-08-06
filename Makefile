all: pdf

en.pdf: html
	cp static/html/en/resume.html /tmp/cv.html.o
	sed -i 's,href="/,href=",g' /tmp/cv.html.o
	weasyprint /tmp/cv.html.o --base-url . cv-fr.pdf
	rm /tmp/cv.html.o

fr.pdf: html
	cp static/html/fr/cv.html /tmp/cv.html.o
	sed -i 's,href="/,href=",g' /tmp/cv.html.o
	weasyprint /tmp/cv.html.o --base-url . cv-fr.pdf
	rm /tmp/cv.html.o

pdf: en.pdf fr.pdf

pot: src/jvk/templates/*.j2
	cd src; python setup.py extract_messages

po: pot
	cd src; python setup.py update_catalog

mo: po
	cd src; python setup.py compile_catalog

html: mo src/jvk/site.py content/** src/jvk/templates/*
	cd src/jvk/ ; python site.py
