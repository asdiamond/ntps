#!/usr/bin/env bash
iptables-restore "previous_configs/$1"

echo 'CURRENT CONFIGURATION IS'
iptables -S
