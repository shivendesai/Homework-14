#Written by Shiven Desai
import tkinter

class TestAvg:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the five frames.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.test5_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.sum_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for test 1.
        self.test1_label = tkinter.Label(self.test1_frame,
                                          text='Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                          width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack the widgets for test 2.
        self.test2_label = tkinter.Label(self.test2_frame,
                                          text='Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                          width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Create and pack the widgets for test 3.
        self.test3_label = tkinter.Label(self.test3_frame,
                                          text='Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                          width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Create and pack the widgets for test 4.
        self.test4_label = tkinter.Label(self.test4_frame,
                                          text='Enter the score for test 4:')
        self.test4_entry = tkinter.Entry(self.test4_frame,
                                          width=10)
        self.test4_label.pack(side='left')
        self.test4_entry.pack(side='left')

        # Create and pack the widgets for test 5.
        self.test5_label = tkinter.Label(self.test5_frame,
                                          text='Enter the score for test 5:')
        self.test5_entry = tkinter.Entry(self.test5_frame,
                                          width=10)
        self.test5_label.pack(side='left')
        self.test5_entry.pack(side='left')

        # Create and pack the widgets for the average.
        self.avg_label = tkinter.Label(self.avg_frame,
                                          text='Average:')
        self.avg = tkinter.StringVar() # To update avg_label
        self.avg_result = tkinter.Label(self.avg_frame,
                                          textvariable=self.avg)
        self.avg_label.pack(side='left')
        self.avg_result.pack(side='left')

        # Create and pack the widgets for the sum.
        self.sum_label = tkinter.Label(self.sum_frame,
                                          text='Sum:')
        self.sum = tkinter.StringVar() # To update sum_label
        self.sum_result = tkinter.Label(self.sum_frame,
                                          textvariable=self.sum)
        self.sum_label.pack(side='left')
        self.sum_result.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Calculate',
                                          command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
                # Pack the frames.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.test5_frame.pack()
        self.avg_frame.pack()
        self.sum_frame.pack()
        self.button_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    # The calculate method is the callback function for
    # the calc_button widget.

    def calculate(self):
        # Get the three test scores and store them
        # in variables.
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        test4 = float(self.test4_entry.get())
        test5 = float(self.test5_entry.get())

        # Calculate the average.
        average = (test1 + test2 + test3 + test4 + test5) / 5

        # Update the average label.
        self.avg.set(format(average, ',.2f'))

        # Calculate the sum.
        total = test1 + test2 + test3 + test4 + test5

        # Update the sum label.
        self.sum.set(format(total, ',.2f'))

# Create an instance of the TestAvg class.
test_avg = TestAvg()
