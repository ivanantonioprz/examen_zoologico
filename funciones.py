import csv

# ─────────────────────────────────────────────
# CLASE Animal
# ─────────────────────────────────────────────

class Animal:
    def __init__(self, nombre, pelo, plumas, huevos, leche, vuela, acuatico,
                 depredador, dientes, espinazo, respira, venenoso, aletas,
                 patas, cola, domestico, tamanio_gato, clase):
        self.nombre = nombre
        self.pelo = int(pelo)
        self.plumas = int(plumas)
        self.huevos = int(huevos)
        self.leche = int(leche)
        self.vuela = int(vuela)
        self.acuatico = int(acuatico)
        self.depredador = int(depredador)
        self.dientes = int(dientes)
        self.espinazo = int(espinazo)
        self.respira = int(respira)
        self.venenoso = int(venenoso)
        self.aletas = int(aletas)
        self.patas = int(patas)
        self.cola = int(cola)
        self.domestico = int(domestico)
        self.tamanio_gato = int(tamanio_gato)
        self.clase = int(clase)

    def __str__(self):
        return f"Animal: {self.nombre} | Clase: {self.clase}"

    def __repr__(self):
        return f"Animal({self.nombre!r}, clase={self.clase})"

    def a_lista(self):
        """Devuelve los datos del animal como lista (para guardar en CSV)."""
        return [
            self.nombre, self.pelo, self.plumas, self.huevos, self.leche,
            self.vuela, self.acuatico, self.depredador, self.dientes,
            self.espinazo, self.respira, self.venenoso, self.aletas,
            self.patas, self.cola, self.domestico, self.tamanio_gato, self.clase
        ]


# ─────────────────────────────────────────────
# FUNCIONES DE CARGA Y GUARDADO
# ─────────────────────────────────────────────

def cargar_csv(ruta):
    """
    Carga un archivo CSV y devuelve una lista de diccionarios.
    Sirve tanto para clases.csv como para zoo.csv.
    """
    datos = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(dict(fila))
    return datos


def guardar_animales(ruta, animales):
    """Guarda la lista de objetos Animal en un archivo CSV."""
    encabezado = [
        'nombre_animal', 'pelo', 'plumas', 'huevos', 'leche', 'vuela',
        'acuatico', 'depredador', 'dientes', 'espinazo', 'respira',
        'venenoso', 'aletas', 'patas', 'cola', 'domestico', 'tamanio_gato', 'clase'
    ]
    with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)
        for animal in animales:
            escritor.writerow(animal.a_lista())


# ─────────────────────────────────────────────
# FUNCIONES DE LISTADO
# ─────────────────────────────────────────────

def listar_por_clase(animales, clases, clase_id):
    """Muestra todos los animales que pertenecen a la clase indicada."""
    nombre_clase = clases.get(str(clase_id), "Desconocida")
    print(f"\n  Animales de la clase: {nombre_clase}")
    print("  " + "-" * 40)
    encontrados = [a for a in animales if a.clase == clase_id]
    if encontrados:
        for a in encontrados:
            print(f"    - {a.nombre}")
    else:
        print("    No se encontraron animales.")
    print(f"\n  Total: {len(encontrados)} animal(es).")


# Diccionario de características disponibles
CARACTERISTICAS = {
    '1':  ('pelo',        'Tiene pelo'),
    '2':  ('plumas',      'Tiene plumas'),
    '3':  ('huevos',      'Pone huevos'),
    '4':  ('leche',       'Produce leche'),
    '5':  ('vuela',       'Vuela'),
    '6':  ('acuatico',    'Es acuático'),
    '7':  ('depredador',  'Es depredador'),
    '8':  ('dientes',     'Tiene dientes'),
    '9':  ('espinazo',    'Tiene espinazo'),
    '10': ('respira',     'Respira (con branquias)'),
    '11': ('venenoso',    'Es venenoso'),
    '12': ('domestico',   'Es doméstico'),
}


def listar_por_caracteristica(animales, atributo):
    """Muestra todos los animales que tienen el atributo indicado en 1."""
    print(f"\n  Animales con la característica '{atributo}':")
    print("  " + "-" * 40)
    encontrados = [a for a in animales if getattr(a, atributo) == 1]
    if encontrados:
        for a in encontrados:
            print(f"    - {a.nombre}")
    else:
        print("    No se encontraron animales.")
    print(f"\n  Total: {len(encontrados)} animal(es).")


# ─────────────────────────────────────────────
# FUNCIÓN PARA AGREGAR ANIMAL
# ─────────────────────────────────────────────

def pedir_si_no(pregunta):
    """Pide 1 (sí) o 0 (no) al usuario."""
    while True:
        respuesta = input(f"    {pregunta} (1=Sí / 0=No): ").strip()
        if respuesta in ('0', '1'):
            return int(respuesta)
        print("    Ingresa solo 1 o 0.")


def agregar_animal(animales, clases):
    """Permite al usuario agregar uno o varios animales."""
    while True:
        print("\n  ── Agregar nuevo animal ──")
        nombre = input("  Nombre del animal: ").strip()
        if not nombre:
            print("  El nombre no puede estar vacío.")
            continue

        # Verificar que no exista ya
        if any(a.nombre.lower() == nombre.lower() for a in animales):
            print(f"  El animal '{nombre}' ya existe en el listado.")
        else:
            print("  Responde las siguientes características (1=Sí, 0=No):\n")
            pelo       = pedir_si_no("¿Tiene pelo?")
            plumas     = pedir_si_no("¿Tiene plumas?")
            huevos     = pedir_si_no("¿Pone huevos?")
            leche      = pedir_si_no("¿Produce leche?")
            vuela      = pedir_si_no("¿Vuela?")
            acuatico   = pedir_si_no("¿Es acuático?")
            depredador = pedir_si_no("¿Es depredador?")
            dientes    = pedir_si_no("¿Tiene dientes?")
            espinazo   = pedir_si_no("¿Tiene espinazo?")
            respira    = pedir_si_no("¿Respira con branquias?")
            venenoso   = pedir_si_no("¿Es venenoso?")
            aletas     = input("    ¿Cuántas aletas tiene? (número): ").strip() or "0"
            patas      = input("    ¿Cuántas patas tiene? (número): ").strip() or "0"
            cola       = pedir_si_no("¿Tiene cola?")
            domestico  = pedir_si_no("¿Es doméstico?")
            tamanio    = pedir_si_no("¿Es del tamaño de un gato o menor?")

            # Seleccionar clase
            print("\n  Clases disponibles:")
            for cid, ctipo in clases.items():
                print(f"    {cid}. {ctipo}")
            while True:
                clase_input = input("  Ingresa el número de clase: ").strip()
                if clase_input in clases:
                    clase = int(clase_input)
                    break
                print("  Clase no válida, intenta de nuevo.")

            nuevo = Animal(nombre, pelo, plumas, huevos, leche, vuela, acuatico,
                           depredador, dientes, espinazo, respira, venenoso,
                           aletas, patas, cola, domestico, tamanio, clase)
            animales.append(nuevo)
            print(f"\n  ✔ Animal '{nombre}' agregado correctamente.")

        otro = input("\n  ¿Deseas agregar otro animal? (s/n): ").strip().lower()
        if otro != 's':
            break
