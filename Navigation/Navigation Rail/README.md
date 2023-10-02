Resumen de los puntos más importantes del texto sobre las propiedades y eventos de `NavigationRail` y `NavigationRailDestination`:

**NavigationRail Properties:**

- `bgcolor`: Establece el color del contenedor que contiene todo el contenido de `NavigationRail`.

- `destinations`: Define la apariencia de los elementos de botón que se encuentran en `NavigationRail`. Debe ser una lista de dos o más instancias de `NavigationRailDestination`.

- `extended`: Indica que `NavigationRail` debe estar en estado extendido, lo que significa que tiene un contenedor de riel más ancho y las etiquetas se colocan junto a los iconos. Se puede establecer `min_extended_width` para establecer el ancho mínimo del riel cuando está en este estado.

- `group_alignment`: La alineación vertical para el grupo de destinos dentro del riel. Debe estar entre -1.0 y 1.0.

- `label_type`: Define el diseño y el comportamiento de las etiquetas para `NavigationRail` no extendido. Los valores incluyen `NONE` (predeterminado), `ALL` y `SELECTED`.

- `leading`: Un control opcional en el riel que se coloca encima de los destinos. Puede ser un `FloatingActionButton` o un elemento no botón, como un logotipo.

- `min_extended_width`: El ancho final cuando la animación se completa para `extended` en True. El valor predeterminado es 256.

- `min_width`: El ancho mínimo posible para el riel, independientemente del tamaño del icono o etiqueta de destino. El valor predeterminado es 72.

- `selected_index`: El índice en `destinations` para el destino actualmente seleccionado o None si no hay ningún destino seleccionado.

- `trailing`: Un control opcional en el riel que se coloca debajo de los destinos. Normalmente es una lista de opciones o destinos adicionales que solo se renderiza cuando `extended` es True.

**NavigationRail Events:**

- `on_change`: Se dispara cuando cambia el destino seleccionado.

**NavigationRailDestination Properties:**

- `icon`: El nombre del icono del destino.

- `icon_content`: El control de icono del destino. Se usa en lugar de la propiedad `icon`.

- `label`: La etiqueta del destino.

- `label_content`: El control de etiqueta para el destino.

- `padding`: La cantidad de espacio para ajustar el elemento de destino.

- `selected_icon`: El nombre del icono alternativo que se muestra cuando se selecciona este destino.

- `selected_icon_content`: Un control de icono alternativo que se muestra cuando se selecciona este destino.