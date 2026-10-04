def temperature_agent(temp):
    goal = 72
    max_iters = 10

    state = {
        "temp": temp,
        "done": False,
        "steps": 0
    }

    for i in range(max_iters):
        # Observe
        print(f"Iteration {i + 1}: Temperature = {state['temp']}")

        # Check goal
        if state["temp"] == goal:
            state["done"] = True
            return state

        # Decide
        if state["temp"] > goal:
            action = "cool"
        else:
            action = "heat"

        # Act
        if action == "cool":
            state["temp"] -= 1
        else:
            state["temp"] += 1

        state["steps"] += 1

    return state


# Example
state = temperature_agent(80)
print(state)
