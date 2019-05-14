#!/usr/bin/env bash
# modified from pypacker and python-netfilterqueue, examples
# only works on icmp packets right now
iptables -I INPUT 1 -p icmp -j NFQUEUE --queue-num 1

#echo "NEW CONFIGURATION IS:"
#iptables -S
