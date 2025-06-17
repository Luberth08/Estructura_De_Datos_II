from .BD import MotorIndexacion

if __name__ == "__main__":
    # Primera ejecución: crear base de datos
    with MotorIndexacion("clientes.bin") as motor:
        motor.insertar_registro(101, "Ana García", "ana@gmail.com", "60111222")
        motor.insertar_registro(102, "Carlos Ruiz", "carlos@gmail.com", "65544333")

    # Segunda ejecución: reabrir base existente
    with MotorIndexacion("clientes.bin") as motor:
        print(motor.buscar_registro(101))  # Debe funcionar sin insertar nuevamente
        print(motor.buscar_registro(102))  # Debería mostrar a Carlos
        motor.__arbol.imprimir_arbol()  # Imprime la estructura del árbol
        print(motor.__arbol.obtener_estructura())  # Obtiene la estructura del árbol para visualización web
