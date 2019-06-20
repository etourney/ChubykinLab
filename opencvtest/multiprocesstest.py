from multiprocessing import Process
import os
import processA
import processB


if __name__ == '__main__':
    #info('main line')
    pA = Process(target=processA.procA, args=())
    pA.start()
    pB = Process(target=processB.procB, args=())
    pB.start()
    pA.join()
    pB.join()