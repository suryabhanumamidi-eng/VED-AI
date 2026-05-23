from Backend.Model import DecisionLayer


def run_demo():
    brain = DecisionLayer()
    sample_commands = [
        "Hello V.E.D., how are you today?",
        "Generate image of a futuristic AI control room.",
        "Run demo",
        "Open browser"
    ]

    print("=== V.E.D. Demo ===")
    for command in sample_commands:
        print(f"> {command}")
        result = brain.route_query(command)
        print(result)
        print()


if __name__ == "__main__":
    run_demo()
