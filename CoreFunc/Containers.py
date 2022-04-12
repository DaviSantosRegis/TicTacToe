
import numpy as np
import itertools as it





class Iterations():
    def __init__(self,list):
        self.list = np.array(list)

    def all_equals(self,item):
        return all([itemiter == item for itemiter in self.list])

    def ForRangeList(self):

        ForRange = [range(self.list[x]) for x in range(self.list.size)]
        return np.array(list(it.product(*ForRange)))

    def Index(self,item):
        npIndex = np.where(self.list == item)
        try:
            return tuple([Index[0] for Index in npIndex])

        except IndexError:
            return None






