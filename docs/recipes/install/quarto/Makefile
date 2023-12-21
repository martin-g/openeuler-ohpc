PAPER    := guide
GITID    := $(shell git describe 2> /dev/null)

#$(info $$GITID is [${GITID}])

_build-distro:
	echo Going to build docs for '$(DISTRO)'

	for distro in $(DISTRO); do \
		for lang in english chinese; do \
			for arch in aarch64 x86_64; do  \
				for rms in slurm openpbs; do  \
					for provisioner in warewulf3; do \
						for format in html pdf md; do \
							quarto render \
								--profile git,$${lang},$${distro},$${arch},$${rms},$${provisioner} \
								--to $${format} \
								--output-dir _output/$${distro}/$${lang}/$${arch}/$${rms}/$${provisioner}/$${format}/ ; \
						done \
					done \
				done \
			done \
		done \
	done

	echo Done building docs for '$(DISTRO)'

openeuler: generate-git-profile 
	$(MAKE) DISTRO=openeuler22.03 _build-distro


rocky: generate-git-profile
	$(MAKE) DISTRO=rocky9 _build-distro

all: generate-git-profile openeuler rocky

clean:
	rm -rf _output $(PAPER)_files .quarto _quarto-git.yml
	
	for ext in pdf html md tex aux log toc; do  \
	 	$(RM) $(PAPER).$$ext; \
	done

generate-git-profile:
	bash ./update_quarto-git.sh

# a goal used for testing/debugging
test-en: generate-git-profile
	quarto render \
		--profile git,english,openeuler22_03,aarch64,slurm,warewulf3 \
		--to pdf \
		--output $(PAPER)_en.pdf ; \
		open $(PAPER)_en.pdf;

test-zh: generate-git-profile
	quarto render \
		--profile git,chinese,openeuler22_03,aarch64,slurm,warewulf3 \
		--to pdf \
		--output $(PAPER)_zh.pdf ; \
		open $(PAPER)_zh.pdf;
