import os
from Backend.Model import DecisionLayer
from Frontend.GUI import VED_GUI


def start_ved():
    # Initialize the Intelligence Router
    brain = DecisionLayer()
    
    # Initialize the HUD (Graphical User Interface)
    # Passing the brain's routing function to the GUI
    app = VED_GUI(process_command=brain.route_query)
    
    print("V.E.D. System: Online. Authorized User: Mr. Surya.")
    app.mainloop()


if __name__ == "__main__":
    start_ved()
