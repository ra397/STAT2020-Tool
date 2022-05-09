import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from calculate import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    # moves frame to the top to display
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
        self.input_sd = None  # entry widget that holds standard deviation
        self.input_x = None  # Entry widget that holds x value
        self.rb_var = tk.IntVar()  # radio button variable
        self.plot_frame = None  # Frame that holds the plot
        self.first_plot = True
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self)
        title_frame.pack(side="top", fill="x", expand=False)

        title = tk.Label(title_frame, text="Normal Distribution", font=('Arial', 22), pady=20)
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

        text_x = tk.Label(input_frame, text='X = ', font=('Arial', 11), padx=10, pady=10)
        text_x.pack(side="left")

        self.input_x = tk.Entry(input_frame)
        self.input_x.pack(side="left")

        rb_frame = tk.Frame(self)
        rb_frame.pack(side="top")

        rb1 = tk.Radiobutton(rb_frame, text='Area to the left of X', variable=self.rb_var, value=1)
        rb1.select()
        rb1.pack(side="left")

        rb2 = tk.Radiobutton(rb_frame, text='Area to the right of X', variable=self.rb_var, value=2)
        rb2.pack(side="left")

        submit_frame = tk.Frame(self)
        submit_frame.pack(side="top")

        submit_button = tk.Button(submit_frame, text="Submit", command=self.make_plot)
        submit_button.pack()

    def make_plot(self):
        mean = float(self.input_mean.get())
        sd = float(self.input_sd.get())
        x = float(self.input_x.get())
        if self.rb_var == 0:
            choice = False
        else:
            choice = True

        figure = graph_normal(mean, sd, x, left=choice)

        if not self.first_plot:
            self.plot_frame.pack_forget()

        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(side='top')

        # creating the Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure,
                                   master=self.plot_frame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        if self.first_plot:
            canvas.get_tk_widget().pack()
        self.first_plot = False


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainPage(self)
        p2 = normalDist(self)

        page_frame = tk.Frame(self)
        container = tk.Frame(self)
        page_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(page_frame, text="Main Page", command=p1.show)
        b2 = tk.Button(page_frame, text="Normal Distribution", command=p2.show)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("675x650")
    root.mainloop()
