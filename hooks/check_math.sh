#!/usr/bin/env bash
# Check that examples contain math blocks compatible with myst-nb
# 1. math blocks starting with '# $$' must be preceded by a blank line or another math block
# 2. no text after ending $$
# 3. only one math block per line
# Reports all violations and exits non-zero at the end

set -euo pipefail

errors=0

for file in "$@"; do
    awk '
      BEGIN { err = 0 }
      /^# *\$\$/ {
        if (prev != "#" && prev !~ /^# *\$\$/) {
          printf "%s:%d: $$ not preceded by blank line\n", FILENAME, NR
          err++
        }
        if ($0 !~ /\$\$$/) {
          printf "%s:%d: $$ not ending by $$\n", FILENAME, NR
          err++
        }
      }

      # Second check: any line containing $$ but NOT starting with # + spaces + $$
      {
        if ($0 ~ /\$\$/ && $0 !~ /^# *\$\$/) {
          printf "%s:%d: contains $$ but does not start with # $$\n", FILENAME, NR
          err++
        }
      }

      # Detect extra $$ on same line
      /^# *\$\$.*\$\$.*\$\$/ {
        printf "%s:%d: multiple $$ on same line\n", FILENAME, NR
        err++
      }

      { prev = $0 }
      END { exit err }
    ' "$file"
      errors=$((errors + $?))
done

if (( errors > 0 )); then
  exit 1
fi
