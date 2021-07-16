# Challenge

## Requisitos
  - [Python 3.8](https://www.python.org/downloads/release/python-389/): Durante la instalacion recuerda activar la casilla de agregar al path.
  - [Pipenv](https://pipenv-es.readthedocs.io/es/latest/): Automáticamente crea y maneja un entorno virtual para tus proyectos.

## Instalacion de librerias

Estando dentro de la carpeta principal instalar las dependencias con Pipenv desde la terminal de comandos.


```powershell
$ pipenv sync
```

Esto crea y activa un entorno virtual e instala las dependencias que necesita el proyecto para funcionar.

> **⚠ WARNING** 
> Recuerda instalar pipenv
>
> `$ pip install pipenv`

> **NOTA** 
> En caso de que existan problemas con pipenv, instala las dependencias directamente con pip desde la terminal de comandos.
>
> `$ pip install -r requirements.txt`

## Uso

Para añadir mas páginas de comercio de productos, se debe hacer desde `settings.py`. Cada `store` en el diccionario será utilizada para buscar el código UPC. Por cada `store`se crea un archivo `csv`.

| Propiedad | Tipo     | Descripción                                                |
| :-------- | :------- | :----------------------------------------------------------|
|   `card`  | `string` | **Required**. XPATH para card en grid dentro de página     |
|   `upc`   | `string` | **Required**. XPATH para encontrar elemento UPC            |
|   `split` | `string` | **Required**. Símbolo para hacer split                     |
|   `tag`   | `string` | **Required**. Nombre prepresentativo de la tienda en linea |
|   `url`   | `string` | **Required**. URL de la página                             |
|   `search`| `string` | **Required**. XPATH para encontrar buscador de la página   |

## Ejecución

```bash
python main.py
```



