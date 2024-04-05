import random
def monty_hall():
    print("Ingrese:\n- 'True' para simular 100000 intentos cambiando de puerta\n- 'False' para simular 100000 intentos sin cambiar de puerta\n- 0 para jugar tú")
    answer = input()
    doors = [1, 2, 3]

    if answer == "0":
        chosen_door = input("Elige una puerta (1, 2, o 3): ")
        print("Has elegido la puerta " + chosen_door)
    else:
        answer = bool(answer == "True")
        simulate_monty_hall(answer)
        exit()
   
    correct_door = random.randint(1, 3)
    
    if int(chosen_door) == correct_door:
        doors.remove(int(chosen_door))
    else:
        doors.remove(int(chosen_door))
        doors.remove(correct_door)
    presenters_door = random.choice(doors) 
    print("El presentador muestra la puerta " + str(presenters_door))
    change_door = input("Decide cambiar de puerta (y/n): ")
    if change_door == "y" or change_door == 1:
        doors = [1, 2, 3]
        doors.remove(int(chosen_door))
        doors.remove(presenters_door)
        chosen_door = doors[0]
        print("Has decidido cambiar a la puerta " + str(chosen_door))
    print("El auto se encuentra en la puerta " + str(correct_door))
    if int(chosen_door) == correct_door:
        print("GANASTE EL AUTO!")
    else:
        print("PERDISTE!")


def simulate_monty_hall(decision):
    wins = 0
    losses = 0
    attempts = 100000
    while attempts > 0:
        doors = [1, 2, 3]
        chosen_door = random.randint(1, 3)
        correct_door = random.randint(1, 3)
        
        if chosen_door != correct_door:
            doors.remove(chosen_door)
            doors.remove(correct_door)
        else:
            doors.remove(chosen_door)
        
        presenters_door = random.choice(doors) 
        
        if decision == True:
            doors = [1, 2, 3]
            doors.remove(chosen_door)
            doors.remove(presenters_door)
            chosen_door = doors[0]
        
        if chosen_door == correct_door:
            wins += 1
        else:
            losses += 1
        attempts -= 1
        if decision == True:
            if attempts == 99000:
                print("Cantidad de veces ganadas cambiando de puerta en 1000 intentos: " + str(wins))
                print("Frecuencia Relativa: " + str(wins / (wins+losses)))
            if attempts == 90000:
                print("Cantidad de veces ganadas cambiando de puerta en 10000 intentos: " + str(wins))
                print("Frecuencia Relativa: " + str(wins / (wins+losses)))
            if attempts == 0:
                print("Cantidad de veces ganadas cambiando de puerta en 100000 intentos: " + str(wins))
                print("Frecuencia Relativa: " + str(wins / (wins+losses)))
        if decision == False:
            if attempts == 99000:
                print("Cantidad de veces ganadas sin cambiar de puerta en 1000 intentos: " + str(wins))
                print("Frecuencia Relativa: " + str(wins / (wins+losses)))
            if attempts == 90000:
                print("Cantidad de veces ganadas sin cambiar de puerta en 10000 intentos: " + str(wins))
                print("Frecuencia Relativa: " + str(wins / (wins+losses)))
            if attempts == 0:
                print("Cantidad de veces ganadas sin cambiar de puerta en 100000 intentos: " + str(wins))
                print("Frecuencia Relativa: " + str(wins / (wins+losses)))

monty_hall()
