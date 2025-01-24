# class Coche

La clase `Coche` permite definir un modelo específico de coche.

Entre sus funcionalidades están los siguientes métodos:

- El control de velocidad.
- El seguimiento del estado de combustible.
- Método para acelerar.
- Método para frenar.
- Método para repostar y verificar el nivel de combustible.

## Descripción del código fuente

1. **Definición de la clase `Coche`**: con un constructor `__init__` que inicializa los atributos:
   - `marca`
   - `modelo`
   - `año`
   - `capacidad_tanque`
   - `nivel_combustible`
   - `velocidad`

2. **Métodos**:
   - **`descripcion`**: Devuelve una descripción del coche.
   - **`arrancar`**: Simula el arranque del coche. Verifica si hay suficiente combustible para arrancar.
   - **`acelerar`**: Aumenta la velocidad del coche y reduce el nivel de combustible.
   - **`frenar`**: Reduce la velocidad del coche.
   - **`verificar_combustible`**: Verifica el nivel actual de combustible.
   - **`repostar`**: Añade combustible al tanque del coche.
   
3. **Instanciar clase `Coche`**:
   - Se crea un objeto `mi_coche`.
   
4. **Llamada a los métodos de la instancia**:
   - Método `descripcion`.
   - Método `arrancar`.
   - Método `acelerar`.
   - Método `frenar`.
   - Método `verificar_combustible`.
   - Método `repostar`.
 
**Importante**: La programación orientada a objetos permite organizar y estructurar el código de una manera modular y reutilizable. 

## Instalación

Instrucciones para clonar el proyecto.

```sh
git clone https://github.com/profesor-ricardo-2024/classCoche.git
```