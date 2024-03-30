import streamlit as st

def main():
    # Texto de bienvenida
    st.title("Bienvenido al Directorio de servicios, tiendas, restaurantes del Fracc. Las Americas, MID",)
    st.write("Aquí puedes ver un mapa interactivo de Mapbox.")

    # Código HTML para incrustar el mapa de Mapbox
    html_code = """
   <iframe width='100%' height='400px' src="https://api.mapbox.com/styles/v1/talegaman5000/clu62pv7p00jq01pa350vddfh.html?title=false&access_token=pk.eyJ1IjoidGFsZWdhbWFuNTAwMCIsImEiOiJjbGo1YXM3ZHMwMm45M2dvNXVtaTZ4dmlpIn0.KwWuHIQzGYotPniqszMunQ&zoomwheel=false#15.14/21.067595/-89.648999" title="directorio americas" style="border:none;"></iframe>
    """
    st.components.v1.html(html_code, width=700, height=600)

if __name__ == "__main__":
    main()
