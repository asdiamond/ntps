
iptables-save -f $1

echo "SAVED:"
cat $1
