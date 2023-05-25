# Importing necessary modules
import tkinter as tk
from process import Process
from scheduler import ProcessScheduler
import sys, os

class Application(tk.Frame):
    # Initializing our Application
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # Creating our GUI Widgets
    def create_widgets(self):
        self.processes = {}
        self.count_process = 0
        self.quantum = 0

        self.quantum_label = tk.Label(self, text="Quantum")
        self.quantum_label.pack()

        self.quantum_entry = tk.Entry(self)
        self.quantum_entry.pack()

        self.add_quantum_button = tk.Button(self, text="Add Quantum", command=self.add_quantum)
        self.add_quantum_button.pack()

        self.process_name_label = tk.Label(self, text="Process Name")
        self.process_name_label.pack()

        self.process_name_entry = tk.Entry(self)
        self.process_name_entry.pack()

        self.burst_time_label = tk.Label(self, text="Burst Time")
        self.burst_time_label.pack()

        self.burst_time_entry = tk.Entry(self)
        self.burst_time_entry.pack()

        self.arrival_time_label = tk.Label(self, text="Arrival Time")
        self.arrival_time_label.pack()

        self.arrival_time_entry = tk.Entry(self)
        self.arrival_time_entry.pack()

        self.priority_label = tk.Label(self, text="Priority")
        self.priority_label.pack()

        self.priority_entry = tk.Entry(self)
        self.priority_entry.pack()

        self.add_button = tk.Button(self, text="Add Process", command=self.add_process)
        self.add_button.pack()

        self.fcfs_button = tk.Button(self, text="FCFS", command=self.run_fcfs)
        self.fcfs_button.pack(side="left")

        self.rr_button = tk.Button(self, text="RR", command=self.run_rr)
        self.rr_button.pack(side="left")

        self.srtf_button = tk.Button(self, text="SRTF", command=self.run_srtf)
        self.srtf_button.pack(side="left")

        self.srtf_button = tk.Button(self, text="SJF", command=self.run_sjf)
        self.srtf_button.pack(side="right")

        self.srtf_button = tk.Button(self, text="PS", command=self.run_ps)
        self.srtf_button.pack(side="right")

        self.srtf_button = tk.Button(self, text="PS with RR", command=self.run_ps_rr)
        self.srtf_button.pack(side="right")

        self.refresh_button = tk.Button(self, text="Refresh", command=self.refresh_app)
        self.refresh_button.pack()

        self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.quit.pack()

        # Create a text widget to display the output
        self.output_text = tk.Text(self)
        self.output_text.pack()

    # Refreshing the Application
    def refresh_app(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    # Adding a Process
    def add_process(self):
        self.count_process += 1
        process_name = self.process_name_entry.get()
        burst_time = int(self.burst_time_entry.get())
        arrival_time = int(self.arrival_time_entry.get())
        priority = int(self.priority_entry.get())
        self.processes[process_name] = [priority, arrival_time, burst_time]
        self.process_name_entry.delete(0, tk.END)
        self.burst_time_entry.delete(0, tk.END)
        self.arrival_time_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    # Intializing Quantum
    def add_quantum(self):
        self.quantum = int(self.quantum_entry.get())

    # Calling the FCFS Algorithm
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

    # Calling the SJF Algorithm
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

    # Calling the RR Algorithm
    def run_rr(self):
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

        scheduler.rr(self.quantum)

    # Calling the SRTF Algorithm
    def run_srtf(self):
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

        scheduler.srtf()

    # Calling the PS Algorithm
    def run_ps(self):
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

        scheduler.ps()

    # Calling the PS with RR Algorithm
    def run_ps_rr(self):
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

        scheduler.ps_rr(self.quantum)

# Launching Our Application
root = tk.Tk()
app = Application(master=root)
app.mainloop()
