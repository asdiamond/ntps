#!/usr/bin/env bash

# may have an f option depending on kernel version
iptables-save > "previous_configs/$1"

echo "SAVED:"
cat "previous_configs/$1"
