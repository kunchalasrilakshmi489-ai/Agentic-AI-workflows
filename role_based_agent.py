def temperature_agent(temp):
    if temp > 100:
        return "cool"
    else:
        return "idle"


# Example
temperature = 105
action = temperature_agent(temperature)


print(action)
