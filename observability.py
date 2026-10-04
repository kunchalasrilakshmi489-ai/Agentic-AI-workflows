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
        else:
            action = "heat"

        # Act
        if action == "cool":
            state["temp"] -= 1
        else:
            state["temp"] += 1

        state["steps"] += 1

        # Log the step
        state["log"].append({
            "step": state["steps"],
            "observe": observation,
            "decide": action,
            "act": f"{action} -> {state['temp']}"
        })

    # Max iterations exceeded
    state["status"] = "failure"
    return state


# Example
result = temperature_agent(75)

print("Status:", result["status"])
print("Done:", result["done"])
print("Steps:", result["steps"])
print("Full log:")

for entry in result["log"]:
    print(entry)
