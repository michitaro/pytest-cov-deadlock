import multiprocessing
import sqlite3
import threading


errors = []


def noop():
    return


def bg_thread():
    bg_process = multiprocessing.Process(target=noop)
    bg_process.start()
    bg_process.join(timeout=1)  # noop should finish within a second.
    if bg_process.exitcode is None:
        errors.append('join timeout')


def run_thread():
    errors.clear()
    th = threading.Thread(target=bg_thread)
    th.start()
    sqlite3.connect(':memory:').close()
    th.join()


def test_main():
    for i in range(200):
        run_thread()
        if len(errors) > 0:
            raise RuntimeError(f'join timeout occured in trial {i}')
