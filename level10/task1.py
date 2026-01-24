groom_guests = {"Ivan", "Petro", "Olga", "Darka"}
bride_guests = {"Darka", "Maria", "Ivan", "Oksana"}

def combine(groom, bride):
    return groom | bride

print(combine(groom_guests,bride_guests))