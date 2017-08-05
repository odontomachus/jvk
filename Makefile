LANG ?= en_US
LLANG = $(firstword $(subst ., ,$(LANG)))
LCODE = $(firstword $(subst _, ,$(LLANG)))

all: pdf

pdf: html
	cd static/ ; cp html/$(LCODE)/resume.html /tmp/cv-$(LCODE).html.o
	sed -i 's,href="/,href=",g' /tmp/cv-$(LCODE).html.o
	weasyprint /tmp/cv-$(LCODE).html.o --base-url . cv-$(LCODE).pdf
	rm /tmp/cv-$(LCODE).html.o

html: src/jvk/site.py content/** src/jvk/templates/*
	cd src/jvk/ ; python site.py
