PAPER    := guide
#TEX_SUFS := .aux .log .nav .out .snm .toc .vrb .fdb_latexmk .bbl .blg .fls
GITID    := $(shell git describe 2> /dev/null)

#$(info $$GITID is [${GITID}])                                                                                                              

.PHONY: guide.qmd
$(PAPER).qmd:
	./update_quarto-git.sh

	quarto render --profile git,english,openeuler22,aarch64 --to md   --output-dir _output/openeuler22.03/english/aarch64
	quarto render --profile git,english,openeuler22,aarch64 --to pdf  --output-dir _output/openeuler22.03/english/aarch64
	quarto render --profile git,english,openeuler22,aarch64 --to html --output-dir _output/openeuler22.03/english/aarch64

	quarto render --profile git,chinese,openeuler22,aarch64 --to md   --output-dir _output/openeuler22.03/chinese/aarch64
	quarto render --profile git,chinese,openeuler22,aarch64 --to pdf  --output-dir _output/openeuler22.03/chinese/aarch64
	quarto render --profile git,chinese,openeuler22,aarch64 --to html --output-dir _output/openeuler22.03/chinese/aarch64

	quarto render --profile git,english,openeuler22,x86_64 --to md   --output-dir _output/openeuler22.03/english/x86_64
	quarto render --profile git,english,openeuler22,x86_64 --to pdf  --output-dir _output/openeuler22.03/english/x86_64
	quarto render --profile git,english,openeuler22,x86_64 --to html --output-dir _output/openeuler22.03/english/x86_64

	quarto render --profile git,chinese,openeuler22,x86_64 --to md   --output-dir _output/openeuler22.03/chinese/x86_64
	quarto render --profile git,chinese,openeuler22,x86_64 --to pdf  --output-dir _output/openeuler22.03/chinese/x86_64
	quarto render --profile git,chinese,openeuler22,x86_64 --to html --output-dir _output/openeuler22.03/chinese/x86_64

	quarto render --profile git,english,rocky9 --to md   --output-dir _output/rocky9
	quarto render --profile git,english,rocky9 --to pdf  --output-dir _output/rocky9
	quarto render --profile git,english,rocky9 --to html --output-dir _output/rocky9

#ifdef GITID
#	common/vc
#else
#	test -s vc.tex || { echo vc.tex file does not exist (and this is not a git repo)!"; exit 1; }
#endif


all: $(PAPER).qmd

clean:
#	$(RM) $(foreach suf, ${TEX_SUFS}, $(PAPER:.pdf=${suf}))
#ifdef GITID
#	$(RM) vc.tex
#endif
	rm -rf _output $(PAPER)_files .quarto
	
	for ext in pdf html md tex aux log toc; do  \
	 	$(RM) $(PAPER).$$ext; \
	done

