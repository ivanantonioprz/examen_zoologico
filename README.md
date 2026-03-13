IVAN ANTONIO PEREZ LOUSTAUNAU
ZOOLOGICO

---

## Descripción

Programa en Python que permite consultar y gestionar un listado de animales con sus características y clasificación.

---

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (solo módulos de la librería estándar)

---

## Cómo iniciar el programa

1. Clona o descarga el repositorio.
2. Asegúrate de que los archivos `zoo.csv` y `clases.csv` estén en la misma carpeta que `main.py`.
3. Abre una terminal y navega a la carpeta `zoologico`:

```bash
cd zoologico
```

4. Ejecuta el programa:

```bash
python main.py
```

---

## Cómo interactuar con el programa

Al iniciar verás el menú principal:

```
=============================================
         🐾  ZOOLÓGICO  🐾
=============================================
  1. Listar animales por clase
  2. Listar animales por característica
  3. Agregar nuevo animal
  4. Salir
=============================================
```

### Opción 1 — Listar por clase
Se muestran las clases disponibles (Mamífero, Ave, Reptil, etc.).  
Escribe el número de la clase que deseas consultar y se listarán todos los animales de esa clase.

### Opción 2 — Listar por característica
Se muestran características como "Tiene pelo", "Vuela", "Es venenoso", etc.  
Escribe el número de la característica y se listarán todos los animales que la poseen.

### Opción 3 — Agregar nuevo animal
El programa te pedirá el nombre del animal y luego una serie de preguntas (1=Sí, 0=No) sobre sus características. Al final seleccionas su clase.  
Puedes agregar varios animales seguidos.

### Opción 4 — Salir
Al salir, los cambios se guardan automáticamente en `zoo.csv`, por lo que la próxima vez que abras el programa los nuevos animales estarán disponibles.

---

## Archivos del proyecto

| Archivo        | Descripción                                      |
|----------------|--------------------------------------------------|
| `main.py`      | Lógica principal y menús del programa            |
| `funciones.py` | Funciones auxiliares, clase Animal, carga/guardado |
| `zoo.csv`      | Base de datos de animales                        |
| `clases.csv`   | Catálogo de clases/tipos de animales             |
| `README.md`    | Este archivo                                     |
