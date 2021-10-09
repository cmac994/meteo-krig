#!/bin/sh

# Credits: http://stackoverflow.com/a/750191

git filter-branch -f --env-filter "
    GIT_AUTHOR_NAME='Callie'
    GIT_AUTHOR_EMAIL='cmcnich@uw.edu'
    GIT_COMMITTER_NAME='Callie'
    GIT_COMMITTER_EMAIL='cmcnich@uw.edu'
  " HEAD
