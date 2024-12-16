import tkinter as tk

class MazeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Navigation using Depth Limited Search")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        
        self.start_coord = None
        self.goal_coord = None
        self.depth = None
        
        self.canvas.bind("<Button-1>", self.place_object)
        self.label_result = tk.Label(root, text="")
        self.label_result.pack()
        self.maze = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                     [0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                     [1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
                     [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                     [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                     [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
                     [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.panel1 = tk.Frame(root)
        self.panel1.pack()
        self.panel2 = tk.Frame(root)
        self.panel2.pack()
        self.depth_label = tk.Label(self.panel1, text="Depth:")
        self.depth_label.pack(side=tk.LEFT)
        self.depth_entry = tk.Entry(self.panel1)
        self.depth_entry.pack(side=tk.RIGHT)
        self.solve_button = tk.Button(self.panel2, text="Solve", command=self.solve_maze)
        self.solve_button.pack(side=tk.LEFT)
        self.button_reset = tk.Button(self.panel2, text="Reset", command=self.reset_canvas)
        self.button_reset.pack(side=tk.RIGHT)
        self.draw_maze()
        
    def place_object(self, event):
        x, y = event.x // 40, event.y // 40
        if not self.start_coord:
            self.start_coord = (x, y)
            self.draw_object(x, y, 'green')
        elif not self.goal_coord:
            self.goal_coord = (x, y)
            self.draw_object(x, y, 'red')
         
        
    
    def draw_object(self, x, y, color):
        self.canvas.create_rectangle(x*40, y*40, (x+1)*40, (y+1)*40, fill=color)
        
    def draw_maze(self):
        for y, row in enumerate(self.maze):
            for x, val in enumerate(row):
                color = 'black' if val == 1 else 'white'
                self.canvas.create_rectangle(x*40, y*40, (x+1)*40, (y+1)*40, fill=color)
    
    def solve_maze(self):
        self.depth=int(self.depth_entry.get())
        if not (self.start_coord and self.goal_coord and self.depth):
            print("Please select start, goal, and depth coordinates.")
            self.label_result.setvar("Please select start, goal, and depth coordinates.")
            
            self.label_result.config()
            return
        
        
        path = self.dfs()
       
        
        if path==None:
            self.label_result.config(text="No solution found!")
        else:
            self.label_result.config(text="Solution found!")
            for x, y in path:
                
                self.draw_object(x, y, 'yellow')
        
        
    
    def dfs(self):
        visited = set()
        stack = [(self.start_coord,[self.start_coord])]
        
        while stack:
            current, path = stack.pop()
            visited.add(current)
            if current == self.goal_coord:
                return path
            if len(path) >= self.depth:
                continue
            
            x, y = current
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for neighbor in neighbors:
                if 0 <= neighbor[0] < len(self.maze) and 0 <= neighbor[1] < len(self.maze[0]) \
                        and self.maze[neighbor[1]][neighbor[0]] == 0 and neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
        
        return None
    
    def reset_canvas(self):
        self.canvas.delete("all")
        self.start_coord = None
        self.goal_coord = None
        self.depth_coord = None
        self.label_result.config(text=" ")
        self.draw_maze()

root = tk.Tk()
maze_gui = MazeGUI(root)
root.mainloop()

