PAPER    := guide
GITID    := $(shell git describe 2> /dev/null)

#$(info $$GITID is [${GITID}])

.PHONY: $(PAPER).qmd
$(PAPER).qmd:
	bash ./update_quarto-git.sh
	
	for lang in english chinese; do \
		for distro in openeuler22_03 rocky9; do \
			for arch in aarch64 x86_64; do  \
				for rms in slurm openpbs; do  \
					for provisioner in warewulf3; do \
						for format in html pdf md; do \
							quarto render \
								--profile git,$${lang},$${distro},$${arch},$${rms},$${provisioner} \
								--to $${format} \
								--output-dir _output/$${lang}/$${distro}/$${arch}/$${rms}/$${provisioner}/$${format}/ ; \
						done \
					done \
				done \
			done \
		done \
	done


all: $(PAPER).qmd

clean:
	rm -rf _output $(PAPER)_files .quarto
	
	for ext in pdf html md tex aux log toc; do  \
	 	$(RM) $(PAPER).$$ext; \
	done

# a goal used for testing/debugging
test:
	quarto render \
		--profile git,english,openeuler22_03,aarch64,slurm,warewulf3 \
		--to pdf \
		--output-dir . ; \
		open $(PAPER).pdf;
