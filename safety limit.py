def temperature_agent(temp):
    goal = 72
    max_iters = 10

    for i in range(max_iters):
        # Observe
        print(f"Iteration {i + 1}: Temperature = {temp}")

        # Check goal
        if temp == goal:
            return "success"

        # Decide
        if temp > goal:
            action = "cool"
        else:
            action = "heat"

        # Act
        if action == "cool":
            temp -= 1
        else:
            temp += 1

    return "failure"


# Example
result = temperature_agent(80)
print(result)
