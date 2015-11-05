from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )
 
 
class TrueNASDataset(SnmpPlugin):
    relname = 'TrueNAS_Datasets'
    modname = 'ZenPacks.iXsystems.TrueNAS.TrueNASDataset'

    deviceProperties = SnmpPlugin.deviceProperties + ('zTrueNASIgnorePools', 'zTrueNASIgnoreDatasets',)
 
    snmpGetTableMaps = (
        GetTableMap(
            'datasetTable', '1.3.6.1.4.1.25359.1.7', {
                '.1': 'datasetId',
                # '.2': 'availableKB',
                # '.3': 'usedKB',
                '.4': 'sizeKB',

                }
            ),
        )
 
    def process(self, device, results, log):
      datasets = results[1].get('datasetTable', {})
 
      rm = self.relMap()
      for snmpindex, row in datasets.items():
        ignore = False
        name = row.get('datasetId')
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
            'size': int(row.get('sizeKB')) * 1024,
            }))
 
      return rm
