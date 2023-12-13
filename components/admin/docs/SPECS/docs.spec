#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros

%define quarto_version 1.3.450

Name:           docs%{PROJ_DELIM}
Version:        3.0.0
Release:        1
Summary:        OpenHPC documentation
License:        BSD-3-Clause
Group:          %{PROJ_NAME}/admin
URL:            https://github.com/openhpc/ohpc
Source0:        docs-ohpc.tar

BuildRequires:  git
BuildRequires:  make

%if ! 0%{?openEuler}
BuildRequires:  texlive-latex
BuildRequires:  texlive-caption
BuildRequires:  texlive-colortbl
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-mdwtools
BuildRequires:  texlive-multirow
#BuildRequires:  texlive-draftwatermark
BuildRequires:  texlive-tcolorbox
BuildRequires:  texlive-environ
BuildRequires:  texlive-trimspaces
BuildRequires:  texlive-amsmath
%endif

%if 0%{?suse_version}
BuildRequires:  libstdc++6
BuildRequires:  texlive-latexmk
BuildRequires:  texlive-epstopdf-pkg
BuildRequires:  texlive-listings
BuildRequires:  texlive-geometry
BuildRequires:  texlive-ctex
%endif

%if 0%{?rhel}
BuildRequires:  texlive-texconfig
BuildRequires:  texlive-metafont
BuildRequires:  texlive-cm
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-ec
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-dvips
BuildRequires:  texlive-mfware
BuildRequires:  latexmk
BuildRequires:  texlive-pdftex-def
BuildRequires:  texlive-epstopdf-pkg
BuildRequires:  tex
%endif

%if 0%{?openEuler}
BuildRequires:  texlive-xetex
BuildRequires:  texlive-fontspec
BuildRequires:  texlive-footnotehyper
BuildRequires:  texlive-tcolorbox
BuildRequires:  texlive-lm-math
BuildRequires:  texlive-collection-langchinese
BuildRequires:  texlive-ctex
BuildRequires:  texlive-xecjk
BuildRequires:  texlive-fandol
BuildRequires:  texlive-framed
BuildRequires:  texlive-mdwtools
BuildRequires:  texlive-multirow
BuildRequires:  texlive-fontawesome5

#BuildRequires:  texlive-texconfig
#BuildRequires:  texlive-helvetic
#BuildRequires:  texlive-ec
#BuildRequires:  texlive-cm-super
#BuildRequires:  latexmk
#BuildRequires:  texlive-mdwtools
#BuildRequires:  texlive-multirow

%ifarch x86_64
Source1: https://github.com/quarto-dev/quarto-cli/releases/download/v%{quarto_version}/quarto-%{quarto_version}-linux-amd64.tar.gz
%endif

%ifarch aarch64
Source1: https://github.com/quarto-dev/quarto-cli/releases/download/v%{quarto_version}/quarto-%{quarto_version}-linux-arm64.tar.gz
%endif
%endif

%description

This guide presents a simple cluster installation procedure using components
from the OpenHPC software stack.

%prep
%setup -n docs-ohpc
%if 0%{?openEuler}
tar -C /tmp -xzf %{SOURCE1}
mkdir -p ${HOME}/bin
ln -s /tmp/quarto-%{quarto_version}/bin/quarto ${HOME}/bin/quarto
export PATH=${HOME}/bin:$PATH
%endif

%build
%if 0%{?suse_version}
%define source_path docs/recipes/install/leap15
%else
%if 0%{?rhel}
%define source_path docs/recipes/install/centos8
%endif
%if 0%{?openEuler}
%define source_path docs/recipes/install/openeuler22.03
%endif
%endif

%define parser ../../../../parse_doc.pl

#----------------------
# x86_64-based recipes
#----------------------

#pushd docs/recipes/install/centos8/x86_64/warewulf/slurm
#make ; %{parser} steps.tex > recipe.sh ; popd

%if 0%{?rhel}
pushd docs/recipes/install/rocky9/x86_64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/rocky9/x86_64/warewulf/openpbs
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/rocky9/x86_64/xcat/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/rocky9/x86_64/xcat_stateful/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/almalinux9/x86_64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/almalinux9/x86_64/warewulf/openpbs
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/almalinux9/x86_64/xcat/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/almalinux9/x86_64/xcat_stateful/slurm
make ; %{parser} steps.tex > recipe.sh ; popd
%endif

%if 0%{?suse_version}
pushd docs/recipes/install/leap15/x86_64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/leap15/x86_64/warewulf/openpbs
make ; %{parser} steps.tex > recipe.sh ; popd
%endif

#%if 0%{?openEuler}
#pushd docs/recipes/install/openeuler22.03/x86_64/warewulf/slurm
#make
#%{parser} steps.tex > recipe.sh
#popd

#pushd docs/recipes/install/openeuler22.03/x86_64/warewulf/openpbs
#make
#%{parser} steps.tex > recipe.sh
#popd
#%endif

#----------------------
# aarch64-based recipes
#----------------------

%if 0%{?rhel}
pushd docs/recipes/install/rocky9/aarch64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/rocky9/aarch64/warewulf/openpbs
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/almalinux9/aarch64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/almalinux9/aarch64/warewulf/openpbs
make ; %{parser} steps.tex > recipe.sh ; popd
%endif

%if 0%{?suse_version}
pushd docs/recipes/install/leap15/aarch64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/leap15/aarch64/warewulf/openpbs
make ; %{parser} steps.tex > recipe.sh ; popd
%endif


%if 0%{?openEuler}
pushd docs/recipes/install/quarto
make openeuler
# TODO install codedown https://github.com/earldouglas/codedown
# codedown ohpc _output/openeuler22.03/guide.md > recipe-openeuler22.03.sh 
# codedown ohpc _output/rocky9/guide.md > recipe-rocky9.sh 
popd

%endif

%install

%{__mkdir_p} %{buildroot}%{OHPC_PUB}/doc

install -m 0644 -p docs/ChangeLog %{buildroot}/%{OHPC_PUB}/doc/ChangeLog
install -m 0644 -p docs/Release_Notes.txt %{buildroot}/%{OHPC_PUB}/doc/Release_Notes.txt

# x86_64 guides

%if 0%{?rhel}
%define lpath rocky9/x86_64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath rocky9/x86_64/warewulf/openpbs
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath rocky9/x86_64/xcat/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath rocky9/x86_64/xcat_stateful/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh


%define lpath almalinux9/x86_64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath almalinux9/x86_64/warewulf/openpbs
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath almalinux9/x86_64/xcat/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath almalinux9/x86_64/xcat_stateful/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh
%endif

%if 0%{?suse_version}
%define lpath leap15/x86_64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath leap15/x86_64/warewulf/openpbs
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh
%endif

%if 0%{?openEuler}
ls -laR docs/recipes/install/quarto/
%define out_path openeuler22.03/english/aarch64/slurm/warewulf3
%define lpath quarto/_output/%{out_path}
install -m 0644 -p -D docs/recipes/install/%{lpath}/pdf/guide.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.pdf
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/guide.md %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.md
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/figures/* %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/figures/*
#install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define out_path openeuler22.03/english/x86_64/slurm/warewulf3
%define lpath quarto/_output/%{out_path}
install -m 0644 -p -D docs/recipes/install/%{lpath}/pdf/guide.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.pdf
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/guide.md %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.md
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/figures/* %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/figures/*
#install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define out_path openeuler22.03/chinese/aarch64/slurm/warewulf3
%define lpath quarto/_output/%{out_path}
install -m 0644 -p -D docs/recipes/install/%{lpath}/pdf/guide.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.pdf
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/guide.md %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.md
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/figures/* %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/figures/*
#install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define out_path openeuler22.03/chinese/x86_64/slurm/warewulf3
%define lpath quarto/_output/%{out_path}
install -m 0644 -p -D docs/recipes/install/%{lpath}/pdf/guide.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.pdf
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/guide.md %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/Install_guide.md
install -m 0644 -p -D docs/recipes/install/%{lpath}/md/figures/* %{buildroot}/%{OHPC_PUB}/doc/recipes/%{out_path}/figures/*
#install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh


#%define lpath openeuler22.03/x86_64/warewulf/openpbs
#install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
#install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh
%endif

# aarch64 guides

%if 0%{?rhel}
%define lpath rocky9/aarch64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath rocky9/aarch64/warewulf/openpbs
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath almalinux9/aarch64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath almalinux9/aarch64/warewulf/openpbs
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh
%endif

%if 0%{?suse_version}
%define lpath leap15/aarch64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath leap15/aarch64/warewulf/openpbs
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh
%endif

#%if 0%{?openEuler}
#%define lpath openeuler22.03/aarch64/warewulf/slurm
#install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
#install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

#%define lpath openeuler22.03/aarch64/warewulf/openpbs
#install -m 0644 -p -D docs/recipes/install/%{lpath}/english/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/english/Install_guide.pdf
#install -m 0755 -p -D docs/recipes/install/%{lpath}/english/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/english/recipe.sh
#install -m 0644 -p -D docs/recipes/install/%{lpath}/chinese-simplified/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/chinese-simplified/Install_guide.pdf
#install -m 0755 -p -D docs/recipes/install/%{lpath}/chinese-simplified/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/chinese-simplified/recipe.sh
#%endif

# input file templates
#install -m 0644 -p docs/recipes/install/centos8/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/centos8/input.local
%if 0%{?rhel}
install -m 0644 -p docs/recipes/install/rocky9/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/rocky9/input.local
install -m 0644 -p docs/recipes/install/almalinux9/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/almalinux9/input.local
%endif
%if 0%{?suse_version}
install -m 0644 -p docs/recipes/install/leap15/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/leap15/input.local
%endif
%if 0%{?openEuler}
install -m 0644 -p docs/recipes/install/openeuler22.03/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/openeuler22.03/input.local
%endif

%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%files
%dir %{OHPC_HOME}
%{OHPC_PUB}
