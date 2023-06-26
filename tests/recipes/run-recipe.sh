#!/bin/bash

# ./docs/recipes/install/parse_doc.pl
PARSER="../../docs/recipes/install/parse_doc.pl"

pushd docs/recipes/install/openeuler22.03/x86_64/warewulf/slurm
make
${PARSER} steps.tex > recipe.sh
popd
