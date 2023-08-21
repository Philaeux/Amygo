import multiprocessing

from amygo.amygo import Amygo

if __name__ == '__main__':
    multiprocessing.freeze_support()
    Amygo().run()
