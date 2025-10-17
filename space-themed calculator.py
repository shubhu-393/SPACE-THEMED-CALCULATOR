# 🌌 Spaced-themed calculator

planets_gravity={
    "Mercury": 3.7,                           #gravity values for each planet
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Jupiter":24.79 ,
    "Saturn": 10.44,
    "uranus": 8.69,
    "neptune": 11.15,
    "pluto": 0.62
}
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y:float):
    return x*y
def div(x,y:float):
    try:
        return x/y
    except ZeroDivisionError:
        return "cannot divide by zero🚫"
    #calculate mass for multiple peoples
def calculate_mass_for_group(planets, people_count):
    if planet not in planets_gravity:
        return "🚫 Invalid planet name!"

    gravity_ratio = planets_gravity[planet] / planets_gravity["Earth"]
    total_mass = 0

    print(f"\n⚖️ Enter the Earth weight for each of the {people_count} visitors:")
    for i in range(people_count):
        try:
            weight = float(input(f"Person {i+1} weight (kg): "))
            planetary_mass = weight * gravity_ratio
            total_mass += planetary_mass
        except ValueError:
            print("🚫 Invalid input. Skipping this person.")

    return round(total_mass, 2)

#main menu
def show_menu():
    print("\n🌌 Welcome to the Space Calculator 🌌")
    print("1. Combine star masses (Add)")
    print("2. Calculate fuel difference (Subtract)")
    print("3. Boost thrust power (Multiply)")
    print("4. Split orbital distance (Divide)")
    print("5. Calculate total mass on a planet")
    print("6. Exit")
#main loop
while True:
    show_menu()
    choice=input("choose an operation(1-6): ")
    if choice=="6":
        print("👋 Exiting Space Calculator. Safe travels!")
        break
    if choice in ["1","2","3","4"]:
        try:
            num1 = float(input("Enter first cosmic value: "))
            num2 = float(input("Enter second cosmic value: "))
        except ValueError:
            print(" Invalid input🚫. Please enter numbers.")
            continue
        if choice=="1":
            print("🪐result: ",add(num1,num2))
        elif choice=="2":
            print("🪐result: ",sub(num1,num2))
        elif choice=="3":
            print("🪐result: ",mul(num1,num2))
        elif choice=="4":
            print("🪐result: ",div(num1,num2))
    elif choice == "5":
        planet = input("Enter planet name (e.g., Mars): ").capitalize()
        try:
         people = int(input("How many people are visiting?: "))
         result = calculate_mass_for_group(planet, people)
         print(f"\n🪐 Total mass on {planet}: {result} kg")
        except ValueError:
            print("🚫 Invalid input. Please enter a valid number.")
        else:
            print("🚫 Invalid choice. Please select from the menu.")


















