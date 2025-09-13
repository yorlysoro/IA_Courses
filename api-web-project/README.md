# API Web Project

Este proyecto es una API web construida utilizando Uvicorn como servidor ASGI. A continuación se presentan las instrucciones para instalar las dependencias y ejecutar la aplicación.

## Estructura del Proyecto

```
api-web-project
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── routes           # Contiene las rutas de la API
│   │   └── index.py     # Definición de las rutas y manejo de solicitudes
│   └── types            # Contiene definiciones de tipos o modelos
│       └── index.py     # Modelos utilizados en la API
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

## Instalación

Para instalar las dependencias del proyecto, asegúrate de tener `pip` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```
uvicorn src.main:app --reload
```

Esto iniciará el servidor en modo de recarga automática, lo que significa que se reiniciará cada vez que realices cambios en el código. La aplicación estará disponible en `http://127.0.0.1:8000`.