temp = 80
goal = 72

for i in range(3):
    # Observe
    print(f"Iteration {i + 1}: Observe -> Temperature = {temp}")

    # Decide
    if temp > goal:
        action = "cool"
    elif temp < goal:
        action = "heat"
    else:
        action = "idle"

    print(f"Decide -> {action}")

    # Act
    if action == "cool":
        temp -= 1
    elif action == "heat":
        temp += 1

    print(f"Act -> Temperature = {temp}\n")
