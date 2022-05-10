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
        self.output_frame = None  # Frame that holds the plot
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
            self.output_frame.pack_forget()

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side='top')

        # creating the Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure,
                                   master=self.output_frame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        if self.first_plot:
            canvas.get_tk_widget().pack()
        self.first_plot = False


class binDist(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.input_n = None
        self.input_p = None
        self.first_plot = True
        self.plot_frame = None
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self)
        title_frame.pack(side="top", fill="x", expand=False)

        title = tk.Label(title_frame, text="Binomial Distribution", font=('Arial', 22), pady=20)
        title.pack()

        input_frame = tk.Frame(self)
        input_frame.pack(side="top")

        text_n = tk.Label(input_frame, text="Number of trials = ", font=('Arial', 11), padx=10, pady=10)
        text_n.pack(side="left")

        self.input_n = tk.Entry(input_frame)
        self.input_n.pack(side="left")

        text_p = tk.Label(input_frame, text="Probability of Success = ", font=('Arial', 11), padx=10, pady=10)
        text_p.pack(side="left")

        self.input_p = tk.Entry(input_frame)
        self.input_p.pack(side="left")

        submit_frame = tk.Frame(self)
        submit_frame.pack(side="top")

        submit_button = tk.Button(submit_frame, text="Submit", command=self.make_plot, padx=10, pady=10)
        submit_button.pack(side='left')

        help_button = tk.Button(submit_frame, text="Help", command=self.help_message, pady=10, padx=10)
        help_button.pack(side='left')

    def make_plot(self):
        n = float(self.input_n.get())
        p = float(self.input_p.get())

        figure = graph_Bin(n, p)

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

    def help_message(self):
        if not self.first_plot:
            self.plot_frame.pack_forget()

        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(side='top')

        message = tk.Label(self.plot_frame, text='X is the number of times for a specific outcome with N trails \n'
                                                 '  where P is the probability of success on each trial\n'
                                                 '      and N is the number of trials')

        message.pack()
        self.first_plot = False


class nbDist(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.input_r = None
        self.input_p = None
        self.first_plot = True
        self.output_frame = None
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self)
        title_frame.pack(side="top", fill="x", expand=False)

        title = tk.Label(title_frame, text="Negative Binomial Distribution", font=('Arial', 22), pady=20)
        title.pack()

        input_frame = tk.Frame(self)
        input_frame.pack(side="top")

        text_r = tk.Label(input_frame, text="R = ", font=('Arial', 11), padx=10, pady=10)
        text_r.pack(side="left")

        self.input_r = tk.Entry(input_frame)
        self.input_r.pack(side="left")

        text_p = tk.Label(input_frame, text="P = ", font=('Arial', 11), padx=10, pady=10)
        text_p.pack(side="left")

        self.input_p = tk.Entry(input_frame)
        self.input_p.pack(side="left")

        warning_frame = tk.Frame(self)
        warning_frame.pack(side="top")

        warning_text = tk.Label(warning_frame, text='*Warning: Extremely high values for R and/or low values for P can '
                                                    'cause application to freeze', fg='red')
        warning_text.pack()

        submit_frame = tk.Frame(self)
        submit_frame.pack(side="top")

        submit_button = tk.Button(submit_frame, text="Submit", command=self.make_plot, pady=10, padx=10)
        submit_button.pack(side='left')

        help_button = tk.Button(submit_frame, text="Help", command=self.help_message, padx=10, pady=10)
        help_button.pack(side='left')

    def make_plot(self):
        r = float(self.input_r.get())
        p = float(self.input_p.get())

        figure = graph_NB(r, p)

        if not self.first_plot:
            self.output_frame.pack_forget()

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side='top')

        # creating the Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure,
                                   master=self.output_frame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        if self.first_plot:
            canvas.get_tk_widget().pack()
        self.first_plot = False

    def help_message(self):
        if not self.first_plot:
            self.output_frame.pack_forget()

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side='top')

        message = tk.Label(self.output_frame, text='X is the trial in which you get R successes\n'
                                                   '  where P is the probability of success for each trial')
        message.pack()
        self.first_plot = False


class poisDist(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.expected_mean = None
        self.input_mean = None
        self.first_plot = True
        self.output_frame = None
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self)
        title_frame.pack(side="top", fill="x", expand=False)

        title = tk.Label(title_frame, text="Poisson Distribution", font=('Arial', 22), pady=20)
        title.pack()

        input_frame = tk.Frame(self)
        input_frame.pack(side="top")

        text = tk.Label(input_frame, text="Expected mean = ", font=('Arial', 11), padx=10, pady=10)
        text.pack(side="left")

        self.input_mean = tk.Entry(input_frame)
        self.input_mean.pack(side='left')

        submit_frame = tk.Frame(self)
        submit_frame.pack(side="top")

        submit_button = tk.Button(submit_frame, text="Submit", command=self.make_plot, pady=10, padx=10)
        submit_button.pack(side='left')

        help_button = tk.Button(submit_frame, text="Help", command=self.help_message, padx=10, pady=10)
        help_button.pack(side='left')

    def make_plot(self):
        mean = float(self.input_mean.get())

        figure = graph_Pois(mean)

        if not self.first_plot:
            self.output_frame.pack_forget()

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side='top')

        # creating the Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure,
                                   master=self.output_frame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        if self.first_plot:
            canvas.get_tk_widget().pack()
        self.first_plot = False

    def help_message(self):
        if not self.first_plot:
            self.output_frame.pack_forget()

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side='top')

        message = tk.Label(self.output_frame, text='X is the number of occurrences of an event in a fixed time '
                                                   'interval\n '
                                                   'where the Expected Mean is the expected number of occurrences of '
                                                   'that event in the same time interval')

        message.pack()
        self.first_plot = False


class expoDist(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

    def create_widgets(self):
        return

    def make_plot(self):
        return


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainPage(self)
        p2 = normalDist(self)
        p3 = binDist(self)
        p4 = nbDist(self)
        p5 = poisDist(self)
        p6 = expoDist(self)

        page_frame = tk.Frame(self)
        container = tk.Frame(self)
        page_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(page_frame, text="Main Page", command=p1.show)
        b2 = tk.Button(page_frame, text="Normal Distribution", command=p2.show)
        b3 = tk.Button(page_frame, text="Binomial Distribution", command=p3.show)
        b4 = tk.Button(page_frame, text="Negative Binomial Distribution", command=p4.show)
        b5 = tk.Button(page_frame, text="Poisson Distribution", command=p5.show)
        b6 = tk.Button(page_frame, text="Exponential Distribution", command=p6.show)
        exit_button = tk.Button(page_frame, text="Exit", command=root.destroy)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        exit_button.pack(side="right")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.attributes("-fullscreen", True)
    root.mainloop()
