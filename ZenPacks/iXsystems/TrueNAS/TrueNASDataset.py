from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
 
 
class TrueNASDataset(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'TrueNASDataset'
 
    size = -1
    _properties = ManagedEntity._properties + (
        {'id': 'size', 'type': 'int'},
        )
 
    _relations = ManagedEntity._relations + (
        ('TrueNAS_Device', ToOne(ToManyCont,
            'ZenPacks.iXsystems.TrueNAS.TrueNASDevice',
            'TrueNAS_Datasets',
            )),
        )
 
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)
 
    def device(self):
        return self.TrueNAS_Device()
 
    def getRRDTemplateName(self):
        return 'TrueNASDataset'
