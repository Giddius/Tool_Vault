import wmi

import time

WMI_MANAGER = wmi.WMI(impersonation_level="Impersonate")


def win_processes():
    for process in WMI_MANAGER.Win32_Process():
        yield process


def _kill_process(process):
    process.Terminate()

    print('terminated process ' + process.name)


def kill_undesired_processes():
    with open('undecired_processes.txt', 'r') as f:
        undesired = list(set(map(lambda x: x.strip(), f.read().splitlines())))
    for process in win_processes():
        if any(undesired_process.casefold() in process.name.casefold() for undesired_process in undesired):
            _kill_process(process)
    for process in win_processes():
        if any(undesired_process.casefold() in process.name.casefold() for undesired_process in undesired):
            print(process.name)


def run_multiple(runs: int):
    for i in range(runs):
        kill_undesired_processes()
        time.sleep(i * 2)
    print('#' * 10 + '- done -' + '#' * 10)


if __name__ == '__main__':
    run_multiple(5)
