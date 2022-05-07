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
        self.input_mean = None  # entry widget that holds mean value
        self.input_sd = None  # entry widget that hold standard deviation
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self)
        title_frame.pack(side="top", fill="x", expand=False)

        title = tk.Label(title_frame, text="Normal Distribution", font=('Arial', 25), pady=20)
        title.pack()

        input_frame = tk.Frame(self)
        input_frame.pack(side="top")

        text_mean = tk.Label(input_frame, text="Mean = ", font=('Arial', 11), padx=10, pady=10)
        text_mean.pack(side="left")

        self.input_mean = tk.Entry(input_frame)
        self.input_mean.pack(side="left")

        text_sd = tk.Label(input_frame, text="Standard deviation = ", font=('Arial', 11), padx=10, pady=10)
        text_sd.pack(side="left")

        self.input_sd = tk.Entry(input_frame)
        self.input_sd.pack(side="left")

        rb_frame = tk.Frame(self)
        rb_frame.pack(side="top")

        var = tk.IntVar()

        rb1 = tk.Radiobutton(rb_frame, text='Area to the left', variable=var, value=1)
        rb1.pack(side="left")

        rb2 = tk.Radiobutton(rb_frame, text='Area to the right', variable=var, value=2)
        rb2.pack(side="left")

        submit_frame = tk.Frame(self)
        submit_frame.pack(side="top")

        submit_button = tk.Button(submit_frame, text="Submit", command=self.make_plot)
        submit_button.pack()

    def make_plot(self):
        mean = self.input_mean.get()
        sd = self.input_sd.get()
        print(mean, sd)


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
