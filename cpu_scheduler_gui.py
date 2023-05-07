import tkinter as tk
from process import Process
from scheduler import ProcessScheduler
import sys

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.processes = {}
        self.count_process = 0

        self.process_name_label = tk.Label(self, text="Process Name")
        self.process_name_label.pack(side="left")

        self.process_name_entry = tk.Entry(self)
        self.process_name_entry.pack(side="left")

        self.burst_time_label = tk.Label(self, text="Burst Time")
        self.burst_time_label.pack(side="left")

        self.burst_time_entry = tk.Entry(self)
        self.burst_time_entry.pack(side="left")

        self.add_button = tk.Button(self, text="Add Process", command=self.add_process)
        self.add_button.pack(side="left")

        self.fcfs_button = tk.Button(self, text="FCFS", command=self.run_fcfs)
        self.fcfs_button.pack(side="left")

        self.sjf_button = tk.Button(self, text="SJF", command=self.run_sjf)
        self.sjf_button.pack(side="left")

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="left")

        # Create a text widget to display the output
        self.output_text = tk.Text(self)
        self.output_text.pack()

    def add_process(self):
        self.count_process += 1
        process_name = self.process_name_entry.get()
        burst_time = int(self.burst_time_entry.get())
        self.processes[process_name] = burst_time
        self.process_name_entry.delete(0, tk.END)
        self.burst_time_entry.delete(0, tk.END)

    def run_fcfs(self):
        scheduler = ProcessScheduler(self.processes, self.output_text, self.count_process)

        # Clear the output text widget before appending new output
        self.output_text.delete('1.0', tk.END)

        # Redirect standard output to the text widget
        def redirect_output(text_widget):
            def write_to_text_widget(s):
                text_widget.insert(tk.END, s)
                text_widget.see(tk.END)
            return write_to_text_widget

        sys.stdout.write = redirect_output(self.output_text)

        scheduler.fcfs()

    def run_sjf(self):
        scheduler = ProcessScheduler(self.processes, self.output_text, self.count_process)

        # Clear the output text widget before appending new output
        self.output_text.delete('1.0', tk.END)

        # Redirect standard output to the text widget
        def redirect_output(text_widget):
            def write_to_text_widget(s):
                text_widget.insert(tk.END, s)
                text_widget.see(tk.END)
            return write_to_text_widget

        sys.stdout.write = redirect_output(self.output_text)

        scheduler.sjf()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
