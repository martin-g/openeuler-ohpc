PAPER    := steps
#TEX_SUFS := .aux .log .nav .out .snm .toc .vrb .fdb_latexmk .bbl .blg .fls
GITID    := $(shell git describe 2> /dev/null)

#$(info $$GITID is [${GITID}])                                                                                                              

.PHONY: steps.qmd
$(PAPER).qmd:
	cat $(PAPER).qmd
	quarto render $(PAPER).qmd --to pdf
	quarto render $(PAPER).qmd --to html
#ifdef GITID
#	common/vc
#else
#	test -s vc.tex || { echo "vc.tex file does not exist (and this is not a git repo)!"; exit 1; }
#endif


all: $(PAPER).qmd

clean:
#	$(RM) $(foreach suf, ${TEX_SUFS}, $(PAPER:.pdf=${suf}))
#ifdef GITID
#	$(RM) vc.tex
#endif
	$(RM) $(PAPER).pdf $(PAPER).html

