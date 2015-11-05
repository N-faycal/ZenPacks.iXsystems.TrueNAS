(function(){
 
var ZC = Ext.ns('Zenoss.component');
 
ZC.registerName(
    'TrueNASPool',
    _t('TrueNAS Pool'),
    _t('TrueNAS Pools'));

ZC.TrueNASPoolPanel = Ext.extend(ZC.ComponentGridPanel, {
 constructor: function(config) {
 config = Ext.applyIf(config||{}, {
 componentType: 'TrueNASPool',
 autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'size'},
                {name: 'health'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'size',
                dataIndex: 'size',
                header: _t('Size'),
                sortable: true,
                renderer: function(n){
                    if (n<0) {
                        return _t('Unknown');
                    } else {
                        return Zenoss.render.bytesString(n);
                    }

                },
                width: 120
            },{
                id: 'health',
                dataIndex: 'health',
                header: _t('Health'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });
 
        ZC.TrueNASPoolPanel.superclass.constructor.call(
 this, config);
    }
});
 
Ext.reg('TrueNASPoolPanel', ZC.TrueNASPoolPanel);


ZC.registerName(
    'TrueNASDataset',
    _t('TrueNAS Dataset'),
    _t('TrueNAS Datasets'));

ZC.TrueNASDatasetPanel = Ext.extend(ZC.ComponentGridPanel, {
 constructor: function(config) {
 config = Ext.applyIf(config||{}, {
 componentType: 'TrueNASDataset',
 autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'size'},
                {name: 'health'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'size',
                dataIndex: 'size',
                header: _t('Size'),
                sortable: true,
                renderer: function(n){
                    if (n<0) {
                        return _t('Unknown');
                    } else {
                        return Zenoss.render.bytesString(n);
                    }

                },
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });
 
        ZC.TrueNASDatasetPanel.superclass.constructor.call(
 this, config);
    }
});
 
Ext.reg('TrueNASDatasetPanel', ZC.TrueNASDatasetPanel);
 
})();
