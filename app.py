import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    # lefts frame to the top to display
    def show(self):
        self.lift()


class MainPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Statistics Visualization Tool")
        label.pack(side="top", fill="both", expand=True)


class normalDist(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Normal Distribution", font=20, pady=20)
        label.pack(side=tk.LEFT)





class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainPage(self)
        p2 = normalDist(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Main Page", command=p1.show)
        b2 = tk.Button(buttonframe, text="Normal Distribution", command=p2.show)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("650x650")
    root.mainloop()

# # The main tkinter window
# window = Tk()
#
# # setting the title and
# window.title('Plotting in Tkinter')
#
# # setting the dimensions of
# # the main window
# window.geometry("500x500")
#
#
# # button that would display the plot
# def plot_graph():
#     figure = graph_normal(0, 1)
#     canvas = FigureCanvasTkAgg(figure,
#                                master=window)
#     # creating the Tkinter canvas
#     # containing the Matplotlib figure
#     canvas = FigureCanvasTkAgg(figure,
#                                master=window)
#     canvas.draw()
#
#     # placing the canvas on the Tkinter window
#     canvas.get_tk_widget().pack()
#
#     # creating the Matplotlib toolbar
#     toolbar = NavigationToolbar2Tk(canvas,
#                                    window)
#     toolbar.update()
#
#     # placing the toolbar on the Tkinter window
#     canvas.get_tk_widget().pack()
#
#
# plot_button = Button(master=window,
#                      height=2,
#                      width=10,
#                      command=plot_graph,
#                      text="Plot")
# # place the button
# # into the window
# plot_button.pack()
#
# # run the gui
# window.mainloop()
