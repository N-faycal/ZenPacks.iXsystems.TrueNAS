from . import schema
from Products.ZenUtils.Utils import convToUnits
from math import isnan

class TrueNASDataset(schema.TrueNASDataset):

    def usage(self, givenUsage = None):
        if givenUsage:
          usage = givenSize
        else: 
          usedSize = self.getUsedSize()
          usage = 100 * ((float(usedSize) * self.allocationUnit) / float(self.size))
        return '{:.2f}%'.format(usage)

    '''
    def size(self, givenSize = None):
      if givenSize: size = givenSize
      else:
        size = self.getAvailableSize()
      return convToUnits(size)
    '''

    def getUsedSize(self, default = None):
        size = self.cacheRRDValue('datasetUsed_datasetUsed', default)
        if size is None or isnan(size):
          size = float('nan')
	return size

    '''
    def getAvailableSize(self, default = None):
        size = self.cacheRRDValue('datasetAvailable_datasetAvailable', default)
        if size is None or isnan(size):
          size = float('nan')
        return size
    '''


