def temperature_agent(temp):
    goal = 72
    max_iters = 10

    state = {
        "temp": temp,
        "done": False,
        "steps": 0,
        "status": "running",
        "log": []
    }

    for i in range(max_iters):
        # Observe
        observation = state["temp"]

        # Check goal
        if observation == goal:
            state["done"] = True
            state["status"] = "success"
            state["log"].append({
                "step": state["steps"],
                "observe": observation,
                "decide": "goal reached",
                "act": "none"
            })
            return state

        # Decide
        if observation > goal:
            action = "cool"
        elif observation < goal:
            action = "heat"
        else:
            action = "invalid"

        # Handle invalid action
        if action not in ["cool", "heat"]:
            return {
                "status": "error",
                "error": f"Invalid action: {action}",
                "state": state
            }

        # Act
        if action == "cool":
            state["temp"] -= 1
        elif action == "heat":
            state["temp"] += 1
        else:
            return {
                "status": "error",
                "error": f"Invalid action: {action}",
                "state": state
            }

        state["steps"] += 1

        # Log step
        state["log"].append({
            "step": state["steps"],
            "observe": observation,
            "decide": action,
            "act": f"{action} -> {state['temp']}"
        })

    # Max iterations exceeded
    state["status"] = "failure"
    return state


result = temperature_agent(75)
print(result)
