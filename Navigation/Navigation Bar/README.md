Resumen de los puntos más importantes del texto sobre las propiedades y eventos de `NavigationBar` y `NavigationDestination`:

## NavigationBar Properties

- **`bgcolor`**: El color de la propia `NavigationBar`.

- **`destinations`**: Define la apariencia de los elementos de botón que se encuentran en la barra de navegación. Debe ser una lista de dos o más instancias de `NavigationDestination`.

- **`elevation`**: La elevación de la propia `NavigationBar`.

- **`label_behavior`**: Define cómo se distribuirán las etiquetas de los destinos y cuándo se mostrarán. Puede usarse para mostrar todas las etiquetas, mostrar solo la etiqueta seleccionada o ocultar todas las etiquetas.

- **`selected_index`**: El índice en `destinations` para el destino actualmente seleccionado o None si no hay ningún destino seleccionado.

## NavigationBar Events

- **`on_change`**: Se dispara cuando cambia el destino seleccionado.

## NavigationDestination Properties

- **`icon`**: El nombre del icono del destino.

- **`icon_content`**: El control de icono del destino. Se usa en lugar de la propiedad `icon`.

- **`label`**: La etiqueta de texto que aparece debajo del icono de este `NavigationDestination`.

- **`selected_icon`**: El nombre del icono alternativo que se muestra cuando se selecciona este destino.

- **`selected_icon_content`**: Un control de icono alternativo que se muestra cuando se selecciona este destino. Si este icono no se proporciona, la `NavigationBar` mostrará `icon_content` en cualquiera de los estados.