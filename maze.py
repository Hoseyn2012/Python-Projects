import tkinter as tk
from tkinter import messagebox

maze = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,1,0,0,0,2],
    [1,0,1,0,1,0,1,0,1,1,1],
    [1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1],
]

cell_size = 45
player_pos = [1, 1]

def draw_maze():
    canvas.delete("all")
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="black")
            elif maze[y][x] == 2:
                canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="green")
    px, py = player_pos
    canvas.create_oval(px * cell_size + 8, py * cell_size + 8, (px + 1) * cell_size - 8, (py + 1) * cell_size - 8, fill="pink")

def move_player(dx, dy):
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
        if maze[new_y][new_x] == 1:
            messagebox.showinfo("Game over", "You hit the wall! Game OVER!")
            root.destroy()
        elif maze[new_y][new_x] == 2:
            messagebox.showinfo("Congratulations!", "You found the exit!")
            root.destroy()
        else:
            player_pos[0] = new_x
            player_pos[1] = new_y
            draw_maze()

def key(event):
    if event.keysym == "Up":
        move_player(0, -1)
    elif event.keysym == "Down":
        move_player(0, 1)
    elif event.keysym == "Left":
        move_player(-1, 0)
    elif event.keysym == "Right":
        move_player(1, 0)

root = tk.Tk()
root.title("Maze Runner")
root.geometry(f"{len(maze[0]) * cell_size}x{len(maze) * cell_size}")
canvas = tk.Canvas(root, width=len(maze[0]) * cell_size, height=len(maze) * cell_size)
canvas.pack()
root.bind("<KeyPress>", key)
draw_maze()
root.mainloop()
