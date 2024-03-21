import random
def monty_hall():
    print("Ingresa 0 para jugar o la cantidad de intentos que quieras simular: ")
    attempts = int(input())
    doors = [1, 2, 3]

    if attempts == 0:
        chosen_door = input("Elige una puerta (1, 2, o 3): ")
    else:
        simulate_monty_hall(attempts)
        chosen_door = random.randint(1, 3)
   
    correct_door = random.randint(1, 3)
    
    if int(chosen_door) == correct_door:
        doors.remove(int(chosen_door))
    else:
        doors.remove(int(chosen_door))
        doors.remove(correct_door)
    presenters_door = random.choice(doors) 
    print("El presentador muestra la puerta " + str(presenters_door))
    if attempts == 0:
        change_door = input("Decide cambiar de puerta (y/n): ")
    else:
        change_door = random.randint(0, 1)
    if change_door == "y" or change_door == 1:
        doors = [1, 2, 3]
        doors.remove(int(chosen_door))
        doors.remove(presenters_door)
        chosen_door = doors[0]
        print("Has decidido cambiar a la puerta " + str(chosen_door))
    print("El auto se encuentra en la puerta " + str(correct_door))
    if int(chosen_door) == correct_door:
        print("GANASTE!")
    else:
        print("PERDISTE!")


def simulate_monty_hall(attempts):
    wins_switch = 0
    wins_stay = 0
    losses = 0

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
        
        switch = random.randint(0, 1)
        if switch == 1:
            doors = [1, 2, 3]
            doors.remove(chosen_door)
            doors.remove(presenters_door)
            chosen_door = doors[0]
        
        if chosen_door == correct_door and switch == 1:
            wins_switch += 1
        elif chosen_door == correct_door and switch == 0:
            wins_stay += 1
        else:
            losses += 1
        
        attempts -= 1
    
    print("Cantidad de veces ganadas sin cambiar: " + str(wins_stay))
    print("Cantidad de veces ganadas cambiando: " + str(wins_switch))
    print("Cantidad de veces perdidas: " + str(losses))

monty_hall()