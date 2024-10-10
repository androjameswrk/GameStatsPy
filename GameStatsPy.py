base_attack_speed = float(input("Enter the base attack speed: "))
bonus_attack_speed_percent = float(input("Enter the bonus attack speed %: ")) / 100
level = int(input("Enter the level: "))

current_attack_speed = base_attack_speed * (1 + (bonus_attack_speed_percent * (level - 1)))
current_attack_speed = round(current_attack_speed, 3)

print(f"The character's current attack speed is {current_attack_speed}.")