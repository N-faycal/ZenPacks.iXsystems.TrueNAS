from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )
 
 
class TrueNASDataset(SnmpPlugin):
    relname = 'trueNASDatasets'
    modname = 'ZenPacks.iXsystems.TrueNAS.TrueNASDataset'

    deviceProperties = SnmpPlugin.deviceProperties + ('zTrueNASIgnorePools', 'zTrueNASIgnoreDatasets',)
 
    snmpGetTableMaps = (
        GetTableMap(
            'datasetTable', '1.3.6.1.4.1.50536.1.2', {
                '.1.1.2': 'datasetDescr',
                # '.2': 'availableKB',
                # '.3': 'usedKB',
                #'.4': 'sizeKB',
		#'.1.6.0': 'datasetAvailable',
                '.1.1.4': 'datasetSize',
                #'.1.1.5.0': 'datasetUsed',
                '.1.1.3': 'datasetAllocationUnits',
                #'.1.1.2.0': 'datasetDescr',
                }
            ),
        )
 
    def process(self, device, results, log):
      datasets = results[1].get('datasetTable', {})
      rm = self.relMap()
      for snmpindex, row in datasets.items():
        allocationUnit = int(row.get('datasetAllocationUnits'))
        hiddenSize = int(row.get('datasetSize')) * allocationUnit
        ignore = False
        name = row.get('datasetDescr')
        toIgnoreDatasets = getattr(device, 'zTrueNASIgnoreDatasets', [])
        for toIgnoreDataset in toIgnoreDatasets:
          if toIgnoreDataset in name:
            log.warn('Skipping dataset {0} since it is set to be ignored'.format(name))
            ignore = True
        if not ignore:
          rm.append(self.objectMap({
            'id': self.prepId(name),
            'title': name,
            'snmpindex': snmpindex.strip('.'),
            'allocationUnit': allocationUnit,
            'size': hiddenSize,
            'hiddenSize': hiddenSize,
            }))
 
      return rm




