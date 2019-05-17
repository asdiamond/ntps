from threading import Thread

from HookCollectionSubsystem import HookRunner
from intercept import interceptor.start_interception

def main():
    interceptor = Thread(target='start_interception')

    hook_executor = HookRunner()

    interceptor.start()
    hook_executor.start()


main()