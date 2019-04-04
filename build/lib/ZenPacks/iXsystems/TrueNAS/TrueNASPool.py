from . import schema
from Products.ZenUtils.Utils import convToUnits
from math import isnan
 
 
class TrueNASPool(schema.TrueNASPool):
    def usage(self, givenUsage = None):
        if givenUsage:
          usage = givenSize
          return 'N/A'
        else: 
          usedSize = self.getUsedSize()
          if usedSize == float('nan'): return 'N/A'
          usage = 100 * ((float(usedSize) * self.allocationUnit) / float(self.size))
        return '{:.2f}%'.format(usage)


    def getUsedSize(self, default = None):
        size = self.cacheRRDValue('zpoolUsed_zpoolUsed', default)
        if size is None or isnan(size):
          size = float('nan')
	return size


