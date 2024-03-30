import streamlit as st

def main():
    # Texto de bienvenida
    st.title("Bienvenido al Directorio de servicios, tiendas, restaurantes del Fracc. Las Americas, MID",)
    st.write("Aquí puedes ver un mapa interactivo de Mapbox.")

    # Código HTML para incrustar el mapa de Mapbox
    html_code = """
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='utf-8' />
    <title>Points on a map</title>
    <meta name='viewport' content='width=device-width, initial-scale=1' />
    <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v3.1.0/mapbox-gl.js'></script>
    <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v3.1.0/mapbox-gl.css' rel='stylesheet' />
    <style>
      body { 
        margin: 0; 
        padding: 0; 
      }

      #map { 
        position: absolute; 
        top: 0; 
        bottom: 0; 
        width: 100%; 
      }
    </style>
  </head>
  <body>
    <div id='map'></div>
    <script>
    // The value for 'accessToken' begins with 'pk...'
    mapboxgl.accessToken = 'pk.eyJ1IjoidGFsZWdhbWFuNTAwMCIsImEiOiJjbGo1YXM3ZHMwMm45M2dvNXVtaTZ4dmlpIn0.KwWuHIQzGYotPniqszMunQ'; 
    const map = new mapboxgl.Map({
      container: 'map',
      // Replace YOUR_STYLE_URL with your style URL.
      style: 'mapbox://styles/talegaman5000/clu62pv7p00jq01pa350vddfh', 
      center: [-89.65558693411182, 21.070582338532652],
      zoom: 14
    });

    // Code from the next step will go here.
    /* 
Add an event listener that runs
  when a user clicks on the map element.
*/
map.on('click', (event) => {
  // If the user clicked on one of your markers, get its information.
  const features = map.queryRenderedFeatures(event.point, {
    layers: ['directorio'] // replace with your layer name
  });
  if (!features.length) {
    return;
  }
  const feature = features[0];

  // Code from the next step will go here.

/* 
    Create a popup, specify its options 
    and properties, and add it to the map.
  */
  const popup = new mapboxgl.Popup({ offset: [0, -15] })
  .setLngLat(feature.geometry.coordinates)
  .setHTML(
    `<h3>${feature.properties.title}</h3><p>${feature.properties.description}</p>`
  )
  .addTo(map);

});

    </script>
  </body>
</html>

"""
    st.components.v1.html(html_code, width=700, height=600)

if __name__ == "__main__":
    main()
