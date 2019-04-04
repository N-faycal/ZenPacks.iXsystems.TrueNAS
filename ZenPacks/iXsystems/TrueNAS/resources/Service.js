Ext.apply(Zenoss.render, {
  api_zpoolHealthRenderer: function(n) {
      var status = parseInt(n)

      switch (status) {
          case 0:
              return "online";
          case 1:
              return "degraded";
          case 2:
              return "faulted";
          case 3:
              return "offline";
          case 4:
              return "unavailable";
          case 5:
              return "removed";
          default:
              return "unknown";
      }
  }
});


