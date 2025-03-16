# A text adventure game
class Room:
    """
    this class represents the rooms in the playing area
    """

    def __init__(self, name, descr, north, east, south, west, go_up, go_down):
        """ This is a method that sets up the variables in the object. """
        self.name = name
        self.description = descr
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = go_up
        self.down = go_down

def main():
    """ This is my main program function """

    # this code populates the room info
    room_list = []
    names = ['secret room', 'bathroom', 'start room', 'living room', 'second living room', 'bedroom']
    descriptions = [
        'You found the secret room. You are the only person that has entered this room. You are the best!',
        'This is a bathroom with 2 doors one east and one south.',
        'This is the start room with one door west.',
        'This is the living room with two doors, one north and one west.',
        'This is the second living room with two doors one west and one east.',
        'This a bedroom with only one west door.'
    ]
    norths = [3, None, None, None, None, None]
    easts = [None, 2, None, 4, 5, None]
    souths = [None, 3, None, 0, None, None]
    wests = [None, None, 1, None, 3, 4]
    ups = [None, None, None, None, None, None]
    downs = [None, None, None, None, None, None]
    for i in range(len(names)):
        room = Room(names[i], descriptions[i], norths[i], easts[i], souths[i], wests[i], ups[i], downs[i])
        room_list.append(room)

    # this code sets the game
    current_room = 2
    done = False
    while not done:
        print(room_list[current_room].description)
        answer = input('What do you want to do? Enter n for north, e for east, s for south, w for west, u for up, '
                       'd for down, q to quit: ')
        print()
        low_answer = answer.lower()
        move = low_answer[0]

        if move == 'n':
            new_room = room_list[current_room].north
            if new_room is None:
                print("Sorry, you can't go that way")
            else:


















                current_room = new_room
        elif move == 'e':
            new_room = room_list[current_room].east
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'w':
            new_room = room_list[current_room].west
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 's':
            new_room = room_list[current_room].south
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'u':
            new_room = room_list[current_room].up
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'd':
            new_room = room_list[current_room].down
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'q':
            print('Goodbye. I hope you liked exploring the house.')
            done = True
        else:
            print('Sorry, I did not understand your answer')


main()
