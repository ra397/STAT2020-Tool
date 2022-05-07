import tkinter as tk
from tkinter import ttk


# template used from https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

class App(tk.Tk):

    # __init__ function for class main page
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # fill frames with
        for F in (StartPage, Page1, Page2):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # Show the main page first

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame displayed
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Statistics Calculator", font=12)

        # putting the grid in its place by using
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Discrete Distributions",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Continuous Distributions",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=1, column=2, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Discrete Distributions", font=12)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Main Page",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Continuous Distributions",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Continuous Distributions", font=12)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Discrete Distributions",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Main Page",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = App()
app.mainloop()

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
