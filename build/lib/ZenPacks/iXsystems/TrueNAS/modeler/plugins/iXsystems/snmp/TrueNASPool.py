from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )
 
 
class TrueNASPool(SnmpPlugin):
    relname = 'TrueNAS_Pools'
    modname = 'ZenPacks.iXsystems.TrueNAS.TrueNASPool'

    deviceProperties = SnmpPlugin.deviceProperties + ('zTrueNASIgnorePools', 'zTrueNASIgnoreDatasets',)
 
    snmpGetTableMaps = (
        GetTableMap(
            'poolTable', '1.3.6.1.4.1.25359.1.1', {
                '.1': 'poolId',
                # '.2': 'availableKB',
                # '.3': 'usedKB',
                '.4': 'poolHealth',
                '.5': 'sizeKB',
                # '.6': 'opRead',

                }
            ),
        )
 
    def process(self, device, results, log):
      pools = results[1].get('poolTable', {})
 
      rm = self.relMap()
      for snmpindex, row in pools.items():
        ignore = False
        name = row.get('poolId')
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
            'size': row.get('sizeKB') * 1024,
            'health': row.get('poolHealth'),
            }))
 
      return rm
