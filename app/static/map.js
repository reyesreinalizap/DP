var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([120.986198,14.586017]), // Coordinates of Adamson University
      zoom: 7 //Initial Zoom Level
    })
  });