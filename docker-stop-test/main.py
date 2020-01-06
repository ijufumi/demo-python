import time
import signal
import datetime

flag = True

def receive_signal(signum, stack):
    print("[{}] received signal".format(datetime.datetime.now()))
    flag = False
    
def main() -> None:
    print("[{}] main start".format(datetime.datetime.now()))
    signal.signal(signal.SIGTERM, receive_signal)
    try:
        while flag:
            print("[{}] loop...{}".format(datetime.datetime.now(), flag))
            time.sleep(10)
    except KeyboardInterrupt:
        print("[{}] stopped".format(datetime.datetime.now()))
        time.sleep(10)


if __name__ == "__main__":
    main()

