from .MotorIndexacion import MotorIndexacion

if __name__ == "__main__":
    # Crear motor de indexación
    motor = MotorIndexacion(orden_arbol=5)

    # Lista de 20 estudiantes con datos diversos
    estudiantes = [
        {"CI": "12345678", "nombre": "Ana", "apellido_paterno": "García", "apellido_materno": "López", "telefono": "555-1234", "email": "ana@example.com", "ppa": "8.5"},
        {"CI": "23456789", "nombre": "Carlos", "apellido_paterno": "Martínez", "apellido_materno": "Sánchez", "telefono": "555-5678", "email": "carlos@example.com", "ppa": "7.2"},
        {"CI": "34567890", "nombre": "María", "apellido_paterno": "Rodríguez", "apellido_materno": "Fernández", "telefono": "555-9012", "email": "maria@example.com", "ppa": "9.1"},
        {"CI": "45678901", "nombre": "Juan", "apellido_paterno": "Pérez", "apellido_materno": "Gómez", "telefono": "555-3456", "email": "juan@example.com", "ppa": "6.8"},
        {"CI": "56789012", "nombre": "Laura", "apellido_paterno": "Hernández", "apellido_materno": "Díaz", "telefono": "555-7890", "email": "laura@example.com", "ppa": "8.9"},
        {"CI": "67890123", "nombre": "Pedro", "apellido_paterno": "López", "apellido_materno": "Martín", "telefono": "555-2345", "email": "pedro@example.com", "ppa": "7.5"},
        {"CI": "78901234", "nombre": "Sofía", "apellido_paterno": "González", "apellido_materno": "Ruiz", "telefono": "555-6789", "email": "sofia@example.com", "ppa": "8.2"},
        {"CI": "89012345", "nombre": "Diego", "apellido_paterno": "Sánchez", "apellido_materno": "Jiménez", "telefono": "555-0123", "email": "diego@example.com", "ppa": "9.3"},
        {"CI": "90123456", "nombre": "Elena", "apellido_paterno": "Ramírez", "apellido_materno": "Serrano", "telefono": "555-4567", "email": "elena@example.com", "ppa": "6.5"},
        {"CI": "11223344", "nombre": "Pablo", "apellido_paterno": "Torres", "apellido_materno": "Vargas", "telefono": "555-8901", "email": "pablo@example.com", "ppa": "8.0"},
        {"CI": "22334455", "nombre": "Lucía", "apellido_paterno": "Flores", "apellido_materno": "Molina", "telefono": "555-2345", "email": "lucia@example.com", "ppa": "7.8"},
        {"CI": "33445566", "nombre": "Jorge", "apellido_paterno": "Díaz", "apellido_materno": "Ortega", "telefono": "555-6789", "email": "jorge@example.com", "ppa": "9.0"},
        {"CI": "44556677", "nombre": "Carmen", "apellido_paterno": "Cruz", "apellido_materno": "Reyes", "telefono": "555-0123", "email": "carmen@example.com", "ppa": "6.9"},
        {"CI": "55667788", "nombre": "Francisco", "apellido_paterno": "Morales", "apellido_materno": "Guerrero", "telefono": "555-4567", "email": "francisco@example.com", "ppa": "8.7"},
        {"CI": "66778899", "nombre": "Isabel", "apellido_paterno": "Ortiz", "apellido_materno": "Delgado", "telefono": "555-8901", "email": "isabel@example.com", "ppa": "7.1"},
        {"CI": "77889900", "nombre": "Miguel", "apellido_paterno": "Gómez", "apellido_materno": "Herrera", "telefono": "555-2345", "email": "miguel@example.com", "ppa": "8.4"},
        {"CI": "88990011", "nombre": "Teresa", "apellido_paterno": "Jiménez", "apellido_materno": "Lorenzo", "telefono": "555-6789", "email": "teresa@example.com", "ppa": "9.2"},
        {"CI": "99001122", "nombre": "Ricardo", "apellido_paterno": "Santos", "apellido_materno": "Campos", "telefono": "555-0123", "email": "ricardo@example.com", "ppa": "6.7"},
        {"CI": "10020030", "nombre": "Patricia", "apellido_paterno": "Vega", "apellido_materno": "Fuentes", "telefono": "555-4567", "email": "patricia@example.com", "ppa": "8.1"},
        {"CI": "20030040", "nombre": "Alberto", "apellido_paterno": "Méndez", "apellido_materno": "Cabrera", "telefono": "555-8901", "email": "alberto@example.com", "ppa": "7.9"}
    ]

    def imprimir_estado(motor, titulo):
        print("\n" + "="*60)
        print(f" {titulo.upper()} ".center(60, "="))
        print("="*60)
        print(motor)
        print(f"CIs indexados: {motor.arbol.inorden()}")

    # 1. Estado inicial
    imprimir_estado(motor, "Estado Inicial")

    # 2. Insertar todos los estudiantes
    print("\nInsertando estudiantes...")
    for i, estudiante in enumerate(estudiantes):
        success, msg = motor.insertar(estudiante)
        print(f"{i+1}. Insertando {estudiante['CI']}: {msg}")
        
        # Mostrar estado cada 5 inserciones
        if (i+1) % 5 == 0:
            imprimir_estado(motor, f"Después de {i+1} inserciones")

    # 3. Estado después de todas las inserciones
    imprimir_estado(motor, "Después de todas las inserciones")

    # # 4. Realizar búsquedas
    # cis_buscar = ["34567890", "55667788", "00000000", "99999999", "20030040"]
    # print("\nRealizando búsquedas:")
    # for ci in cis_buscar:
    #     resultado = motor.buscar(ci)
    #     if resultado:
    #         print(f"✓ Encontrado CI {ci}: {resultado['nombre']} {resultado['apellido_paterno']}")
    #     else:
    #         print(f"✗ No encontrado CI {ci}")

    # # 5. Eliminar algunos estudiantes
    # cis_eliminar = ["23456789", "45678901", "77889900", "11223344"]
    # print("\nEliminando estudiantes:")
    # for ci in cis_eliminar:
    #     if motor.eliminar(ci):
    #         print(f"✓ Eliminado CI {ci}")
    #     else:
    #         print(f"✗ No se pudo eliminar CI {ci}")

    # # 6. Estado después de eliminaciones
    # imprimir_estado(motor, "Después de eliminaciones")

    # # 7. Búsquedas después de eliminar
    # print("\nBúsquedas después de eliminar:")
    # for ci in cis_eliminar + ["34567890"]:
    #     resultado = motor.buscar(ci)
    #     if resultado:
    #         print(f"✓ Encontrado CI {ci}: {resultado['nombre']} {resultado['apellido_paterno']}")
    #     else:
    #         print(f"✗ No encontrado CI {ci}")

    # # 8. Mostrar estructura del árbol
    # print("\nEstructura del árbol:")
    # motor.imprimir_arbol()

    # # 9. Mostrar archivo de datos
    # print("\nContenido de estudiantes.dat:")
    # with open("estudiantes.dat", "r", encoding="utf-8") as f:
    #     print(f.read())

    # # 10. Mostrar archivo de índice
    # print("\nContenido de indice_ci.dat:")
    # with open("indice_ci.dat", "r", encoding="utf-8") as f:
    #     print(f.read())




    # Crear motor con árbol de orden 3 (árbol B mínimo)
    # motor = MotorIndexacion(orden_arbol=3)
    # print(motor)

    # estudiantes = [
    #     {"CI": "111", "nombre": "Ana", "apellido_paterno": "Gómez", "apellido_materno": "López", "telefono": "123", "email": "ana@example.com", "ppa": "8.5"},
    #     {"CI": "222", "nombre": "Juan", "apellido_paterno": "Pérez", "apellido_materno": "Martínez", "telefono": "456", "email": "juan@example.com", "ppa": "7.2"},
    #     {"CI": "333", "nombre": "María", "apellido_paterno": "Rodríguez", "apellido_materno": "Sánchez", "telefono": "789", "email": "maria@example.com", "ppa": "9.1"},
    #     {"CI": "444", "nombre": "Carlos", "apellido_paterno": "Díaz", "apellido_materno": "Fernández", "telefono": "012", "email": "carlos@example.com", "ppa": "6.8"},
    #     {"CI": "555", "nombre": "Luisa", "apellido_paterno": "Hernández", "apellido_materno": "García", "telefono": "345", "email": "luisa@example.com", "ppa": "8.9"}
    # ]

    # for est in estudiantes:
    #     success, msg = motor.insertar(est)
    #     print(f"Insertando {est['CI']}: {msg}")

    # motor.imprimir_arbol()

    # print("\nBúsquedas:")
    # print(motor.buscar("333"))  # Maria
    # print(motor.buscar("444"))  # Carlos
    # print(motor.buscar("999"))  # None (no existe)

    # print("\nEliminar CI 222 (Juan):")
    # if motor.eliminar("222"):
    #     print("✅ Eliminado correctamente")
    # else:
    #     print("❌ No se encontró el CI")

    # print("\nEstado después de eliminar:")
    # print(motor)

    # print("\nÁrbol después de eliminar:")
    # motor.imprimir_arbol()

    # print("\nVerificar búsquedas post-eliminación:")
    # print("Buscar 444:", motor.buscar("444"))  # Carlos
    # print("Buscar 222:", motor.buscar("222"))  # None (eliminado)