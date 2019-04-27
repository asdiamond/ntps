# retrieved from pypacker examples_interceptor.py
iptables -I INPUT 1 -p icmp -j NFQUEUE --queue-balance 0:2

echo "NEW CONFIGURATION IS:"
iptables -S
