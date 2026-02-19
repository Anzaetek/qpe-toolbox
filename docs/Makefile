# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
EXAMPLESDIR	  = ../examples
SOURCEDIR     = source
BUILDDIR      = build
AUTOAPIRDIR = $(SOURCEDIR)/autoapi
TUTODIR = $(SOURCEDIR)/customapi/tutorials

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.PHONY: clean

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(AUTOAPIRDIR)/*
	rm -rf $(TUTODIR)/*ipynb
	rm -rf $(TUTODIR)/figures

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	jupytext $(EXAMPLESDIR)/*py --to ../docs/$(TUTODIR)//ipynb
	cp -r $(EXAMPLESDIR)/figures $(TUTODIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
