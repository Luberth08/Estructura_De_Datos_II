'''
    Title: Programa que simula una partida de Dados con la clase Dado
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 24/03/2025
    Version: 1.0 
'''


# Importamos la clase Dado
from ClaseDado import Dado


def lanzar_dado(dado: Dado):
    '''
        Simula el lanzamiento de un dado y muestra el resultado en pantalla.
        
        Parameters:
            dado (Dado): Objeto de la clase Dado.

        Returns:
            None
    '''
    # Lanzamos el dado
    input("Presiona ENTER para lanzar el dado... ")
    # Lanzamos el dado hasta que no salga el número máximo de caras
    while(True): 
        dado.lanzar()
        if dado.get_valor() != dado.get_caras():
            break

    # Mostramos el resultado
    print("\n¡Lanzaste el dado y te salio: " + str(dado.get_valor()) + "!")


def jugar():
    '''
        Simula un juego de dados donde las instrucciones se muestran en pantalla.
        
        Parameters:
            None

        Returns:
            None
    '''
    # Mostramos las instrucciones del juego
    print(  "/////////////////////////  INSTRUCCIONES  //////////////////////////\n" +
            "- Lanza el dado y observa el resultado.\n" +
            "- Adivina el siguiente numero.\n" +
            "- Si aciertas, el dado ajusta su numero de caras.\n" +
            "- Si fallas, el número de caras del dado se duplica.\n" +
            "- Ganas si consigues que el dado tenga 2 caras.\n" +
            "¡Suerte! \n" + 
            "////////////////////////////////////////////////////////////////////")
    
    # Creamos un dado de 6 caras
    dado = Dado()   
    print("\n-------------------  INICIO DEL JUEGO  -------------------\n")

    # Iniciamos el bucle que da inicio al juego
    while dado.get_caras() != 2:

        # Mostramos el numero actual de caras del dado
        print("\n*** Tu dado tiene [" + str(dado.get_caras()) + "] caras ***\n")

        # Lanzamos el dado hasta que no salga el número máximo de caras
        lanzar_dado(dado)

        # Guardamos el resultado del lanzamiento
        result_ini = dado.get_valor()
        
        # Preguntamos al usuario si el siguiente número será mayor o menor igual
        print("La pregunta es: ¿El siguiente número será mayor o menor igual que [" + str(result_ini) + "]?")

        # Validamos la elección del usuario
        while(True):
            eleccion = input("Ingresa 'm' para menor igual o 'M' para mayor: ") 
            if(eleccion == 'm' or eleccion == 'M'):
                break
            else:
                print("¡¡¡ Por favor, ingresa una opción válida  !!!")

        # Lanzamos el dado nuevamente
        lanzar_dado(dado)
        result_fin = dado.get_valor()

        # Comparamos los resultados
        if (eleccion == 'm' and result_fin <= result_ini) or (eleccion == 'M' and result_fin > result_ini):
            print("\n¡Felicidades! Acertaste :)\n")

            # Ajustamos el número de caras del dado si sale 1
            if(result_ini == 1):
                dado.set_caras(2)   
            else:
                dado.set_caras(result_ini)
        else:

            # Duplicamos el número de caras del dado si falla
            print("\n¡Fallaste! :(, el numero de caras de tu dado se ha duplicado\n")
            dado.set_caras(dado.get_caras() * 2)

            # Preguntamos al usuario si desea terminar el juego
            print("¿Te rindes?\n")
            opcion = int(input("1 para Si, 2 para No: "))
            if opcion == 1:
                break

    
    # Mostramos el resultado final
    print("Bien jugado, conseguiste que el dado tuviera 2 caras. ¡Ganaste!")
    print("-------------------  FIN DEL JUEGO  -------------------")



if __name__ == "__main__":
    # Iniciamos el juego
    jugar()

