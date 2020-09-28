is_running = True
import os
import time
import sys
import signal

def onSigChld(signo, frame):
    global is_running
    pid, status = os.waitpid(-1, os.WNOHANG)
    if pid:
        is_running = False
    pass


def onSigInt(signo, frame):
    global is_running
    is_running = False
    pass


def onSigTerm(signo, frame):
    global is_running
    is_running = False
    pass


def test():
    global is_running
    while is_running:
        time.sleep(1)
        print(".")
    print("App exit gracefully.")
    sys.exit(0)
    pass


if __name__ == "__main__":
    # 子进程退出后向父进程发送的信号
    signal.signal(signal.SIGCHLD, onSigChld)

    # 主进程退出信号
    signal.signal(signal.SIGINT, onSigInt)
    signal.signal(signal.SIGTERM, onSigTerm)

    test()
