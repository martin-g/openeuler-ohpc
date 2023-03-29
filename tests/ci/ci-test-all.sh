#!/bin/bash

set -x

PR_NUMBER="$1"
REPO_OWNER_AND_NAME="$2"

if [ "$PR_NUMBER" == "" ]; then
	echo "This script only support pull requests"
	exit 1
fi

if [ -z  "$REPO_OWNER_AND_NAME" ]; then
	echo "REPO_OWNER_AND_NAME/\$2 not set. Exiting."
	exit 1
fi

COMMIT_MSGS=$( curl -s https://api.github.com/repos/"$REPO_OWNER_AND_NAME"/pulls/"$PR_NUMBER"/commits | jq -r .[].commit.message )

for c in $COMMIT_MSGS; do
	if echo $c | grep -q ci-test-all --; then 
		# "Will run all tests!"
		echo 1
		exit 0
	fi
done

# Will run the tests for the changed specs only!
echo 0
