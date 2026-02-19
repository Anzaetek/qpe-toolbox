#!/usr/bin/env bash

status=0
for file in "$@"; do
    if [ "$(grep -c '^# # ' $file)" -ne 1 ]; then
      echo "$file: expected exactly 1 occurrence of '^# # ', found"
      grep -Hn '^# # ' "$file"
      status=1
    fi
done
exit $status
