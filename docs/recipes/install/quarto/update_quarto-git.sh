#!/usr/bin/env bash

# newline with two spaces
NL1="%n  "
# newline with four spaces
NL2="%n    "

git --no-pager log -1 HEAD --pretty=format:"ohpc:${NL1}git:${NL2}Hash: %H${NL2}AbrHash: %h${NL2}ParentHashes: %P${NL2}AbrParentHashes: %p${NL2}AuthorName: %an${NL2}AuthorEmail: %ae${NL2}AuthorDate: %ai${NL2}CommitterName: %cn${NL2}CommitterEmail: %ce${NL2}CommitterDate: %ci%n" > _quarto-git.yml