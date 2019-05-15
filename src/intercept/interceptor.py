from netfilterqueue import NetfilterQueue
import subprocess


def produce(pkt):
    print(pkt)

    # pkt.accept()


def start_interception():
    # save previous iptables config to `previous_configs/fname`
    # by calling the save.sh script
    fname = "previous_config.txt"
    subprocess.call(["./save.sh", fname])

    # change iptables rule to forward traffic into nfqueue
    subprocess.call("./intercept.sh")

    # bind nfque, and call produce method on new packets intercepted
    nfq = NetfilterQueue()
    nfq.bind(1, produce)

    try:
        nfq.run()
    except KeyboardInterrupt:
        subprocess.call(['./restore.sh', fname])
        print('Goodbye!')

    nfq.unbind()

start_interception()
