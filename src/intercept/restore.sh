#!/usr/bin/env bash
iptables-restore $1

echo 'CURRENT CONFIGURATION IS'
iptables -S
