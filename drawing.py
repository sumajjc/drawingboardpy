
import tkinter as tk # Built in GUI framework from Python's standard lib --https://realpython.com/python-gui-tkinter/  

from math import cos, sin, pi  # what allows the program to perform mathematical tasks https://www.w3schools.com/python/python_math.asp 

 

class HexagonDrawerBoard: 

    def __init__(self, artboard): 

        self.artboard = artboard 

        self.artboard.title("Drawing Board") 

 

        self.canvas = tk.Canvas(self.artboard, width=800, height=400, bg="white") 

        self.canvas.pack(side=tk.LEFT) # 'pack' is the layout manager within Tkinter 

 

        self.mode = None # Initializes drawing mode 

        self.start_x = None # Initializes starting coordinates 

        self.start_y = None 

 

        "Binds user click/events to mouse and methods" 

        self.canvas.bind("<Button-1>", self.when_clicked) 

        self.canvas.bind("<B1-Motion>", self.when_dragged) 

        self.canvas.bind("<ButtonRelease-1>", self.when_released) 

        '''create an event == user click, in the canvas and the 'bind' binds the event to the object 

        <Button-1> - The primary mouse button being clicked. - https://www.hashbangcode.com/article/using-events-tkinter-canvas-elements-python''' 

        # Creates frame for buttons 

        self.button_frame = tk.Frame(self.artboard) 

        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y) 

 

        # Buttons for different modes based on project requirements 

        self.circle_button = tk.Button(self.button_frame, text="Concentric Circles", command=lambda: self.mode_setting("circle"), width=15) 

        self.circle_button.pack(side=tk.TOP, pady=5) #https://www.tutorialspoint.com/python/tk_button.htm 

 

        self.hexagon_button = tk.Button(self.button_frame, text="Hexagons", command=lambda: self.mode_setting("hexagon"), width=15) 

        self.hexagon_button.pack(side=tk.TOP, pady=5) 

 

        self.line_button = tk.Button(self.button_frame, text="Arbitrary Lines", command=lambda: self.mode_setting("line"), width=15) 

        self.line_button.pack(side=tk.TOP, pady=5) 

 

        # Restart button 

        self.restart_button = tk.Button(self.button_frame, text="Restart", command=self.restart_artboard, width=15) 

        self.restart_button.pack(side=tk.TOP, pady=5) 

 

    def mode_setting(self, mode): 

        self.mode = mode # Sets the drawing mode based on users click on button 

 

    def when_clicked(self, event): 

        self.startpoint_x = event.x 

        self.startpoint_y = event.y 

        # If statements to perform loop based on user choice of mode 

        if self.mode == "circle": 

            radius = ((event.x - self.startpoint_x) ** 2 + (event.y - self.startpoint_y) ** 2) ** 0.5 

            num_circles = int(radius / 10) 

            radius = num_circles * 10 

            self.canvas.create_oval(self.startpoint_x - radius, self.startpoint_y - radius, 

                                     self.startpoint_x + radius, self.startpoint_y + radius, outline="black") 

 

        elif self.mode == "hexagon": 

            self.draw_hexagon(event) 

 

        elif self.mode == "line": 

            self.canvas.delete("temp_line") 

            self.canvas.create_line(self.startpoint_x, self.startpoint_y, event.x, event.y, tags="temp_line") 

    # defined mouse drag events to create concentric circles with 10 dispacement between 

    def when_dragged(self, event): 

        if self.mode == "circle": 

            radius = ((event.x - self.startpoint_x) ** 2 + (event.y - self.startpoint_y) ** 2) ** 0.5 

            num_circles = int(radius / 10) 

            radius = num_circles * 10 

            self.canvas.create_oval(self.startpoint_x - radius, self.startpoint_y - radius, 

                                     self.startpoint_x + radius, self.startpoint_y + radius, outline="red") 

 

    # defines mouse release event to ensure making line form one point to another  

    def when_released(self, event): 

        if self.mode == "line": 

            self.canvas.create_line(self.startpoint_x, self.startpoint_y, event.x, event.y) 

 

    def draw_hexagon(self, userclick): 

        x, y = userclick.x, userclick.y 

        size = 50 

 

        hexagon_points = self.calculating_hex_points(x, y, size, angle_offset=90) 

 

        # hexagon drawing using a loop 

        for i in range(6): 

            self.canvas.create_line(hexagon_points[2 * i], hexagon_points[2 * i + 1], 

                                    hexagon_points[(2 * i + 2) % 12], hexagon_points[(2 * i + 3) % 12], 

                                    fill="blue", width=2) 

 

    def calculating_hex_points(self, center_x, center_y, size, angle_offset=0): 

        angle = 360 / 6 

        points = [] 

        for i in range(6): 

            x = center_x + size * cos((angle * i + angle_offset) * pi / 180) 

            y = center_y + size * sin((angle * i + angle_offset) * pi / 180) 

            points.extend([x, y]) 

        return points 

 

    def restart_artboard(self): 

        self.canvas.delete("all")  # Clears the canvas 

 

def main(): 

    root = tk.Tk() # created the main Tkinter application window 

    app = HexagonDrawerBoard(root) 

    root.mainloop() 

 

if __name__ == "__main__": 

    main() 

 

 

 

OUTPUT 

 

 

 

 
