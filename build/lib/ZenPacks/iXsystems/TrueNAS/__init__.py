from . import zenpacklib

zenpacklib.load_yaml()


from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
# from Products.ZenUtils.Utils import unused
#
# unused(Globals)
#
#
class ZenPack(ZenPackBase):
#
#     # All zProperties defined here will automatically be created when the
#     # ZenPack is installed.
     packZProperties = [
         ('zTrueNASLogin', 'admin', 'str'),
         ('zTrueNASPass',  'admin', 'password'),
         ('zTrueNASIgnorePools', ['freenas-boot'], 'lines'),
         ('zTrueNASIgnoreDatasets', ['freenas-boot/ROOT/Initial-Install', 'freenas-boot/ROOT/default'], 'lines')
         ]

