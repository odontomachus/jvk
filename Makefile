LANG ?= en_US
LLANG = $(firstword $(subst ., ,$(LANG)))
LCODE = $(firstword $(subst _, ,$(LLANG)))

all: pdf

pdf: html
	cp cv-$(LCODE).html cv-$(LCODE).html.o
	sed -i 's,href="/,href=",g' cv-$(LCODE).html.o
	weasyprint cv-$(LCODE).html.o --base-url . cv-$(LCODE).pdf
	rm cv-$(LCODE).html.o

html: src/jvk/cv.py content/cv-en.yaml src/jvk/templates/cv.j2
	cd src/jvk/ ; python cv.py ../../content/cv-en.yaml ../../cv.html
	rm -f index.html
	ln -s cv-$(LCODE).html index.html
