from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )
 
 
class TrueNASPool(SnmpPlugin):
    relname = 'trueNASPools'
    modname = 'ZenPacks.iXsystems.TrueNAS.TrueNASPool'

    deviceProperties = SnmpPlugin.deviceProperties + ('zTrueNASIgnorePools', 'zTrueNASIgnoreDatasets',)
 
    snmpGetTableMaps = (
        GetTableMap(
            'poolTable', '1.3.6.1.4.1.50536.1.1.1', {
                '.1.2': 'zpoolDescr',
                # '.2': 'availableKB',
                '.1.3': 'zpoolAllocationUnit',
		'.1.6': 'zpoolAvailable',
                # '.3': 'usedKB',
                '.1.7': 'zpoolHealth',
                '.1.4': 'zpoolSize',
                # '.6': 'opRead',

                }
            ),
        )
 
    def process(self, device, results, log):
      pools = results[1].get('poolTable', {})
 
      rm = self.relMap()
      for snmpindex, row in pools.items():
        allocationUnit = int(row.get('zpoolAllocationUnit'))
        size = int(row.get('zpoolSize')) * allocationUnit
        ignore = False
        name = row.get('zpoolDescr')
        toIgnorePools = getattr(device,'zTrueNASIgnorePools', [])
        for toIgnorePool in toIgnorePools:
          if toIgnorePool in name:
            log.warn('Skipping pool {0} since it is set to be ignored'.format(name))
            ignore = True
        if not ignore:
          rm.append(self.objectMap({
            'id': self.prepId(name),
            'title': name,
            'snmpindex': snmpindex.strip('.'),
            'size': size,
            'allocationUnit':allocationUnit,
            'health': row.get('zpoolHealth'),
            }))
 
      return rm




