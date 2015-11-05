from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
 
class TrueNASDevice(Device):
    # temp_sensor_count = None
   
  _properties = Device._properties + (
        # {'id': 'temp_sensor_count', 'type': 'int'},
        )
  _relations = Device._relations + (
      ('TrueNAS_Pools', ToManyCont(ToOne,
          'ZenPacks.iXsystems.TrueNAS.TrueNASPool',
          'TrueNAS_Device',
          )),
      ('TrueNAS_Datasets', ToManyCont(ToOne,
          'ZenPacks.iXsystems.TrueNAS.TrueNASDataset',
          'TrueNAS_Device',
          )),

      )
