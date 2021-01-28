# ProyectoWeb
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Proyecto de un sitio Web para la gestion de Pedidos y Tienda Online. Partiendo del uso del Framework Django

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Despliegue del sitio en local:

1. Instalar Python (v3.9.1 o superior), desde la pagina oficial ( https://www.python.org/downloads/ ).
    Corroborar que la consola reconozca el programa en cuestion y la version mencionada
 
2. Instalacion y/o actualizacion de paquetes:
    Primeramente actualizando el administrador integrado "pip", con el comando : " python -m pip install --upgrade pip "
    Situarnos desde la consola en el directorio del proyecto,
    para luego actualizar las dependencias, comando: "pip install -r requirements.txt"
    
3. Iniciando el servidor:
    A travez del comando " python manage.py runserver".
    Podremos corroborar que el proyecto y servidor correspondiente estan en normal funcionamiento,
    al leer por consola el sig. mensaje:
        
        ...
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        January 28, 2021 - 17:22:17
        Django version 3.1.5, using settings 'ProyectoWeb.settings'
        Starting development server at http://127.0.0.1:8000/     <--------- *Esta direccion puede variar
        Quit the server with CTRL-BREAK.
        ...
    
4. Accediendo a la direccion mencionada y comentada en el paso 3, es decir,
   en la puesta en funcionamiento del servidor (en mi caso ejemplificado :  http://127.0.0.1:8000/ ).
   Podremos acceder a la pagina principal del proyecto.



