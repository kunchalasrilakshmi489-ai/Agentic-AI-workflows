def temperature_agent(temp):
    goal = 72
    max_iters = 10

    state = {
        "temp": temp,
        "done": False,
        "steps": 0,
        "status": "running"
    }

    for i in range(max_iters):
        # Observe
        print(f"Iteration {i + 1}: Temperature = {state['temp']}")

        # Check goal
        if state["temp"] == goal:
            state["done"] = True
            state["status"] = "success"
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

    # Max iterations exceeded
    state["status"] = "failure"
    return state


# Example
result = temperature_agent(80)
print(result)
