from tkinter import *
import time

class ProcessScheduler:
    def __init__(self, processes, output, count_process):
        self.processes = processes
        self.output = output
        self.count_process = count_process

    # First Come First Serve Algorithm
    def fcfs(self):
        self.output.insert(END, "FCFS Scheduling:\n")
        process_queue = self.processes
        # Making a copy of our ready queue
        process_queue_fcfs = process_queue.copy()

        # To keep track of run time and wait time
        run_time = 0
        wait_time = 0

        for i in range(5):
            time.sleep(1)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        # Applying FCFS logic
        for item in process_queue:
            run_time += process_queue[item]
            del process_queue_fcfs[item]
            if process_queue_fcfs:
                wait_time += run_time
            for i in range(10):
                self.output.insert(END, "[]")
                self.output.update_idletasks()
                time.sleep(0.5)
            self.output.insert(END, "\n")
            self.output.insert(END, "{}: completed. Time: {}\n".format(item, run_time))
            self.output.update_idletasks()

        # Calculate and print Average Wait Time
        avg_wait = wait_time / self.count_process
        time.sleep(2)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()
    
    # Shortest Job First Algorithm
    def sjf(self):
        self.output.insert(END, "SJF Scheduling:\n")
        process_queue = self.processes
        # Making a copy of our ready queue
        process_queue_sjf = process_queue.copy()

        for i in range(5):
            time.sleep(1)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        # Sort queue with respect to burst time
        process_queue_sjf = dict(sorted(process_queue_sjf.items(), key=lambda x:x[1]))
        process_queue_sjf2 = process_queue_sjf.copy()

        # To keep track of run time and wait time
        run_time = 0
        wait_time = 0

        # Applying SJF logic
        for item in process_queue_sjf:
            run_time+=process_queue_sjf[item] 
            del process_queue_sjf2[item]
            if process_queue_sjf2:
                wait_time += run_time
            for i in range(10):
                self.output.insert(END, "[]")
                self.output.update_idletasks()
                time.sleep(0.5)
            self.output.insert(END, "\n")
            self.output.insert(END, "{}: completed. Time: {}\n".format(item, run_time))
            self.output.update_idletasks()

        # Calculate and print Average Wait Time
        avg_wait = wait_time / self.count_process
        time.sleep(2)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()

