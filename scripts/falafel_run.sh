#!/bin/bash

# `bun run $1`

cd packages/falafel

arg=$1

if [ -z "$arg" ]; then
    bun run
    echo ""
    echo -e "\x1b[2mfalafel_run.sh: pass one of these scripts to falafel_run.sh\x1b[0m"
    echo -e "\033[0;2mexample:\x1b[0m scripts/falafel_run.sh \033[0;34mdev\x1b[0m"
else
    bun run $1
    echo "lol"

fi