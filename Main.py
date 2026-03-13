from funciones import (
    cargar_csv, guardar_animales, Animal,
    listar_por_clase, listar_por_caracteristica,
    agregar_animal, CARACTERISTICAS
)

# ─────────────────────────────────────────────
# RUTAS DE ARCHIVOS
# ─────────────────────────────────────────────
RUTA_ZOO    = 'zoo.csv'
RUTA_CLASES = 'clases.csv'

# ─────────────────────────────────────────────
# CARGAR DATOS AL INICIO
# ─────────────────────────────────────────────

def cargar_clases():
    """Carga clases.csv en un diccionario {id: tipo}."""
    datos = cargar_csv(RUTA_CLASES)
    return {fila['Clase_id']: fila['Clase_tipo'] for fila in datos}


def cargar_animales(clases):
    """Carga zoo.csv y devuelve una lista de objetos Animal."""
    datos = cargar_csv(RUTA_ZOO)
    animales = []
    for fila in datos:
        a = Animal(
            nombre       = fila['nombre_animal'],
            pelo         = fila['pelo'],
            plumas       = fila['plumas'],
            huevos       = fila['huevos'],
            leche        = fila['leche'],
            vuela        = fila['vuela'],
            acuatico     = fila['acuatico'],
            depredador   = fila['depredador'],
            dientes      = fila['dientes'],
            espinazo     = fila['espinazo'],
            respira      = fila['respira'],
            venenoso     = fila['venenoso'],
            aletas       = fila['aletas'],
            patas        = fila['patas'],
            cola         = fila['cola'],
            domestico    = fila['domestico'],
            tamanio_gato = fila['tamanio_gato'],
            clase        = fila['clase']
        )
        animales.append(a)
    return animales

# ─────────────────────────────────────────────
# MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def mostrar_menu():
    print("\n" + "=" * 45)
    print("         🐾  ZOOLÓGICO  🐾")
    print("=" * 45)
    print("  1. Listar animales por clase")
    print("  2. Listar animales por característica")
    print("  3. Agregar nuevo animal")
    print("  4. Salir")
    print("=" * 45)


def menu_clases(animales, clases):
    """Submenú para elegir clase."""
    print("\n  Clases disponibles:")
    for cid, ctipo in clases.items():
        print(f"    {cid}. {ctipo}")
    opcion = input("\n  Selecciona el número de clase: ").strip()
    if opcion in clases:
        listar_por_clase(animales, clases, int(opcion))
    else:
        print("  Opción no válida.")


def menu_caracteristicas(animales):
    """Submenú para elegir característica."""
    print("\n  Características disponibles:")
    for key, (atributo, descripcion) in CARACTERISTICAS.items():
        print(f"    {key:>2}. {descripcion}")
    opcion = input("\n  Selecciona el número de característica: ").strip()
    if opcion in CARACTERISTICAS:
        atributo, _ = CARACTERISTICAS[opcion]
        listar_por_caracteristica(animales, atributo)
    else:
        print("  Opción no válida.")


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    print("\nCargando datos...")
    clases   = cargar_clases()
    animales = cargar_animales(clases)
    print(f"Se cargaron {len(animales)} animales y {len(clases)} clases.")

    while True:
        mostrar_menu()
        opcion = input("  Selecciona una opción: ").strip()

        if opcion == '1':
            menu_clases(animales, clases)

        elif opcion == '2':
            menu_caracteristicas(animales)

        elif opcion == '3':
            agregar_animal(animales, clases)

        elif opcion == '4':
            print("\n  Guardando cambios en zoo.csv...")
            guardar_animales(RUTA_ZOO, animales)
            print("  ✔ Cambios guardados. ¡Hasta luego!")
            break

        else:
            print("  Opción no válida. Intenta de nuevo.")


if __name__ == '__main__':
    main()
