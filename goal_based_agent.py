def temperature_agent(temp):
    goal = 72

    while temp != goal:
        if temp > goal:
            temp -= 1
            print(f"Cooling... Temperature: {temp}")
        else:
            temp += 1
            print(f"Heating... Temperature: {temp}")

    print("Goal reached: Temperature = 72")


# Example
temperature_agent(80)
