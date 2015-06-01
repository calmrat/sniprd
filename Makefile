
TMP = $(CURDIR)/tmp
VERSION = $(shell grep ^Version sniprd.spec | sed 's/.* //')

# Push files to the production web only when in the master branch
ifeq "$(shell git rev-parse --abbrev-ref HEAD)" "master"
PUSH_URL = fedorapeople.org:public_html/sniprd
else
PUSH_URL = fedorapeople.org:public_html/sniprd/testing
endif

PACKAGE = sniprd-$(VERSION)
DOCS = $(TMP)/$(PACKAGE)/docs
EXAMPLES = $(TMP)/$(PACKAGE)/examples
CSS = --stylesheet=style.css --link-stylesheet
FILES = LICENSE README.rst \
		Makefile sniprd.spec \
		docs examples source

ifndef USERNAME
    USERNAME = echo $$USER
endif

all: push clean

build:
	mkdir -p $(TMP)/{SOURCES,$(PACKAGE)}
	cp -a $(FILES) $(TMP)/$(PACKAGE)
	cd docs && make man SPHINXOPTS=-Q && gzip -c _build/man/sniprd.1 > $(DOCS)/sniprd.1.gz

tarball: build
	cd $(TMP) && tar cfj SOURCES/$(PACKAGE).tar.bz2 $(PACKAGE)

rpm: tarball
	rpmbuild --define '_topdir $(TMP)' -bb sniprd.spec

srpm: tarball
	rpmbuild --define '_topdir $(TMP)' -bs sniprd.spec

packages: rpm srpm

push: packages
	# Documentation & examples
	scp $(DOCS)/*.{css,html} $(PUSH_URL)
	scp $(EXAMPLES)/* $(PUSH_URL)/examples
	# Archives & rpms
	scp sniprd.spec \
		$(TMP)/SRPMS/$(PACKAGE)* \
		$(TMP)/RPMS/noarch/$(PACKAGE)* \
		$(TMP)/SOURCES/$(PACKAGE).tar.bz2 \
		$(PUSH_URL)/download

clean:
	rm -rf $(TMP)
	find source -name '*.pyc' -exec rm {} \;

run_docker: build_docker
	@echo
	@echo "Please note: this is a first cut at doing a container version as a result; known issues:"
	@echo "* kerberos auth may not be working correctly"
	@echo "* container runs as privileged to access the conf file"
	@echo "* output directory may not be quite right"
	@echo 
	@echo "This does not actually run the docker image as it makes more sense to run it directly. Use:"
	@echo "docker run --privileged --rm -it -v $(HOME)/.sniprd:/sniprd.conf $(USERNAME)/sniprd"
	@echo "If you want to add it to your .bashrc use this:"
	@echo "alias sniprd=\"docker run --privileged --rm -it -v $(HOME)/.sniprd:/sniprd.conf $(USERNAME)/sniprd\""

build_docker: docker-artifacts/Dockerfile
	docker build -t $(USERNAME)/sniprd --file="docker-artifacts/Dockerfile" .
