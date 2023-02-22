class Tank:
# Create a Tank object with the given armor, penetration, and armor type.
    def __init__(self, armor, penetration, armor_type):
        self.armor = armor
        self.penetration = penetration
        self.armor_type = armor_type
        
        # Check if the armor type is valid.
        if not (armor_type == 'chobham' or armor_type == 'composite' or armor_type == 'ceramic'):
            raise Exception('Invalid armor type %s' % (armor_type))
        
        self.name = "Tank"  # Set a default name for the tank.

    # Set the name of the tank.
    def set_name(self, name):
        self.name = name

    # Check if the tank is vulnerable to another tank.
    def vulnerable(self, other_tank):
        real_armor = self.armor
        if self.armor_type == 'chobham':
            real_armor += 100
        elif self.armor_type == 'composite' or self.armor_type == 'ceramic':
            real_armor += 50
        # Check if the tank's armor is penetrated by an other tank.
        if real_armor <= other_tank.penetration:
            return True
        return False

    # Swap armor with another tank.
    def swap_armor(self, other_tank):
        tmp = other_tank.armor
        other_tank.armor = self.armor
        self.armor = tmp
        return other_tank

    # Return a string representation of the tank.
    def __repr__(self):
        tmp = self.name.lower()
        tmp = tmp.replace(' ', '-')
        return tmp


# Create two chobham tanks.
m1_1 = Tank(600, 670, 'chobham')
m1_2 = Tank(620, 670, 'chobham')

# Check if the first tank is vulnerable to the second tank.
if m1_1.vulnerable(m1_2):
    print('Vulnerable to self')

# Create a list of five steel tanks.
tanks = []
for i in range(5):
    tanks.append(Tank(400, 400, 'steel'))

# Set names for the tanks.
index = 0
for tank in tanks:
    tank.set_name('Tank' + str(index) + "_Small")
    index += 1

# Check if the tanks are vulnerable to the first chobham tank.
test = []
index = 0
while index < len(tanks):
    test.append(tanks[index].vulnerable(m1_1))
    index += 1

# Check if any tank is safe from the first chobham tank.
def test_tank_safe(shooter, test_vehicles=[]):
    at_least_one_safe = False
    for t in test_vehicles:
        if not shooter.vulnerable(t):
            at_least_one_safe = True
            break
            
    if at_least_one_safe:
        print("A tank is safe")
    else:
        print("No tank is safe")

test_tank_safe(m1_1, tanks)  # Check if any tank is safe from the first chobham tank.