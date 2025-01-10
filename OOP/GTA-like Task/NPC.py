import random

# Define the size of the map (adjust as needed)
MAP_SIZE = 100

# Create a 2D array to track NPC positions (initialized with None)
world_map = [[None for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

class NPC:
    """
    Represents a Non-Player Character with attributes and methods.
    """

    def __init__(self, name, gender, appearance, age, position, mood='relaxed'):
        """
        Initializes an NPC instance.

        Args:
            name (str): The name of the NPC.
            gender (str): The gender of the NPC.
            appearance (str): The appearance of the NPC.
            age (str): The age of the NPC (minor, adult, senior).
            position (tuple): A 2D coordinate representing the NPC's position (x, y).
            mood (str, optional): The initial mood of the NPC (relaxed, nervous, angry, attack). 
                                Defaults to 'relaxed'.

        Raises:
            ValueError: If the NPC's appearance is 'police' and their age is not 'adult'.
        """
        if appearance == 'police' and age != 'adult':
            raise ValueError("Only adult NPCs can have the police appearance.")
        self.name = name
        self.gender = gender
        self.appearance = appearance
        self.age = age
        self.position = position
        self.mood = mood

        # Update the world_map with the initial position
        global world_map
        world_map[position[0]][position[1]] = self

    def move(self, newPosition, speed=1):
        """
        Moves the NPC to a new position.

        Args:
            newPosition (tuple): The new position of the NPC.
            speed (int, optional): The speed of the NPC's movement. Defaults to 1.

        Displays a message indicating the NPC's movement.
        """
        if self.is_position_occupied(newPosition):  # Check if destination is occupied
            newPosition = self.find_empty_position(newPosition) 
        original_position = self.position
        self.position = newPosition

        # Update the world_map
        global world_map
        world_map[newPosition[0]][newPosition[1]] = self
        world_map[original_position[0]][original_position[1]] = None

        movement_type = "walking" if speed == 1 else "running"
        print(f"NPC {self.name} is {movement_type} from {original_position} to {newPosition}")

    def is_position_occupied(self, position):
        """
        Checks if the given position is already occupied by another NPC.
        """
        global world_map
        return world_map[position[0]][position[1]] is not None
    
    def find_empty_position(self, target_position):
        # This method finds a random empty position near the target position.
        # You'll need to define the range of positions to check.
        x, y = target_position
        while True:
            new_x = random.randint(x - 1, x + 1)
            new_y = random.randint(y - 1, y + 1)
            if not self.is_position_occupied((new_x, new_y)):
                return (new_x, new_y)

    def calculate_distance(self, other_position):
        # Calculate the distance between the NPC's current position and the other NPC's position.
        x1, y1 = self.position
        x2, y2 = other_position
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def changeMood(self, newMood):
        """
        Changes the mood of the NPC.

        Args:
            newMood (str): The new mood of the NPC.

        Displays a message indicating the NPC's mood change.
        """
        self.mood = newMood
        print(f"NPC {self.name} is now in {newMood} mood")

    def alerted(self):
        """
        Alerts the NPC, changing their mood accordingly.
        """
        if self.appearance == 'police':
            self.changeMood('attack')
        else:
            self.changeMood(random.choice(['nervous', 'attack']))

# Create some NPC instances
npc1 = NPC("John Doe", "male", "casual", "adult", (10, 20))
npc2 = NPC("Jane Smith", "female", "business", "adult", (50, 30))
npc3 = NPC("Bob Jones", "male", "police", "adult", (80, 70))

# Move NPCs
npc1.move((30, 50))
npc2.move((20, 40)) 

# Alert NPCs
npc1.alerted()
npc3.alerted()

# Print NPC information
print(f"NPC1: {npc1.__dict__}")
print(f"NPC2: {npc2.__dict__}")
print(f"NPC3: {npc3.__dict__}")