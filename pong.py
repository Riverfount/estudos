import tkinter as tk


class Game(tk.Frame):

    def __init__(self, master):

        super(Game,  self).__init__(master)
        self.lives = 3
        self.width = 600
        self.height = 400
        self.background = '#aaaaff'
        self.canvas = tk.canvas = tk.Canvas(self, width = self.width, height = self.height, bg = self.background)
        item = self.canvas.create_rectangle(10, 10, 100, 80, fill = 'green')
        game_object = GameObject(self.canvas, item)  # create new instance
        print(game_object.get_position())
        # [10, 10, 100, 80]
        game_object.move(20, -10)
        print(game_object.get_position())
        # [30, 0, 120, 70]
        game_object.delete()

        self.canvas.pack()
        self.pack()

class GameObject(object):

    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


if __name__ == '__main__':

    root = tk.Tk()
    root.title('Hello Pong')
    game = Game(root)
    game.mainloop()
