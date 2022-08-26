my_name = 'Magnus Daniel B Einarsson'
my_age = 28
my_height_cm = 189 # 189 cm
my_height_ft = round(189 / 30.48 ,1)
my_weight = 106 # kg
my_eyes = 'brown'
my_teeth = 'yellow'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_ft} centimeters tall.")
print(f"He's {my_weight} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_weight + my_height_ft
print (f"If I add {my_age}, {my_height_ft}, and {my_weight} I get {total}. ")
