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
            time.sleep(0.3)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        # Applying FCFS logic
        for item in process_queue:
            run_time += process_queue[item][2]
            del process_queue_fcfs[item]
            if process_queue_fcfs:
                wait_time += run_time
            for i in range(10):
                self.output.insert(END, "[]")
                self.output.update_idletasks()
                time.sleep(0.3)
            self.output.insert(END, "\n")
            self.output.insert(END, "{}: completed. Time: {}\n".format(item, run_time))
            self.output.update_idletasks()

        # Calculate and print Average Wait Time
        avg_wait = wait_time / self.count_process
        time.sleep(0.3)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()
    
    # Shortest Job First Algorithm
    def sjf(self):
        self.output.insert(END, "SJF Scheduling:\n")
        process_queue = self.processes
        # Making a copy of our ready queue
        process_queue_sjf = process_queue.copy()

        for i in range(5):
            time.sleep(0.3)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        # Sort queue with respect to burst time
        process_queue_sjf = dict(sorted(process_queue_sjf.items(), key=lambda x:x[1][2]))
        process_queue_sjf2 = process_queue_sjf.copy()

        # To keep track of run time and wait time
        run_time = 0
        wait_time = 0

        # Applying SJF logic
        for item in process_queue_sjf:
            run_time+=process_queue_sjf[item][2]
            del process_queue_sjf2[item]
            if process_queue_sjf2:
                wait_time += run_time
            for i in range(10):
                self.output.insert(END, "[]")
                self.output.update_idletasks()
                time.sleep(0.3)
            self.output.insert(END, "\n")
            self.output.insert(END, "{}: completed. Time: {}\n".format(item, run_time))
            self.output.update_idletasks()

        # Calculate and print Average Wait Time
        avg_wait = wait_time / self.count_process
        time.sleep(0.3)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()

    # Round Robin Algorithm
    def rr(self, quantum):
        self.output.insert(END, "RR Scheduling:\n")
        processes = self.processes
        time_quantum = quantum

        # Making a copy of our ready queue
        copied_processes = processes.copy()

        temporary_dic = {}
        total_time = 0

        for i in range(5):
            time.sleep(0.3)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        while True:
            for process, value in processes.items():
                if process not in copied_processes:
                    continue
                if ((processes[process][2]) <= time_quantum):
                    for i in range(10):
                        self.output.insert(END, "[]")
                        self.output.update_idletasks()
                    time.sleep(0.3)
                    self.output.insert(END, "\n")
                    total_time += processes[process][2]
                    self.output.insert(END, "{}: completed. Time: {}\n".format(process, total_time))
                    self.output.update_idletasks()
                    # total_time += processes[process][2]
                    copied_processes.pop(process)
                else:
                    for i in range(10):
                        self.output.insert(END, "[]")
                        self.output.update_idletasks()
                    time.sleep(0.3)
                    self.output.insert(END, "\n")
                    total_time += time_quantum
                    self.output.insert(END, "{}: completed. Time: {}\n".format(process, total_time))
                    self.output.update_idletasks()
                    processes[process][2] = processes[process][2] - time_quantum
                    # total_time += 5
                    temporary_dic[process] = value
                    copied_processes.pop(process)
                    copied_processes.update(temporary_dic)
                    temporary_dic.clear()

            if bool(copied_processes) == False:
                break

        # Calculate and print Average Wait Time
        avg_wait = total_time / self.count_process
        time.sleep(0.3)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()
        
    # Shortest Remaining Time First Algorithm
    def srtf(self):
        self.output.insert(END, "SRTF Scheduling:\n")
        for i in range(5):
            time.sleep(0.3)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        processes = self.processes
        waiting_queue = {}
        current_time = 0
        temporary_dic = {}
        process_with_CPU = {}
        num_items = len(processes)

        # sort process according to arrival time
        processes = dict(sorted(processes.items(), key=lambda x: x[1][1]))


        while True:
            if (all(process[2] == 0 for process in processes.values())):
                break

            for process, value in processes.items():
                # if burst time is 0, process not given to cpu
                if (processes[process][2] == 0):
                    continue

                # processes added to waiting queue, if it is equal to current time
                if (current_time == value[1]):

                    waiting_queue[process] = value

            # waiting sorted according to burst time
            waiting_queue = dict(sorted(waiting_queue.items(), key=lambda x: x[1][2]))
            copied_waiting_queue = waiting_queue.copy()

            for waiting_process, value in copied_waiting_queue.items():

                if bool(process_with_CPU) == False:
                    # burst time decreaments by 1
                    waiting_queue[waiting_process][2] = waiting_queue[waiting_process][2] - 1

                    # a reference created for the precess who got the cpu and process removed from waiting_queue
                    process_with_CPU[waiting_process] = waiting_queue.pop(
                        waiting_process)

                    # printing proocess
                    keys_of_item_with_CPU = process_with_CPU.keys()
                    keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                    key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                    for i in range(10):
                        self.output.insert(END, "[]")
                        self.output.update_idletasks()
                    time.sleep(0.3)
                    self.output.insert(END, "\n")
                    self.output.insert(END, "{}: completed. Time: 1s\n".format(waiting_process))
                    self.output.update_idletasks()

                    # current time increamented
                    current_time += 1
                    break

                # If cpu not empty
                elif bool(process_with_CPU) == True:

                    # First check if burst time of process with cpu is 0 or not

                    key = process_with_CPU.keys()
                    key_list = list(key)

                    key2 = key_list[0]
                    if (process_with_CPU[key2][2] != 0):

                        # then check if burst time of process with current cpu is greater than the process in waiting queue
                        if (waiting_queue[waiting_process][2] < process_with_CPU[key2][2]):

                            waiting_queue.update(process_with_CPU)
                            process_with_CPU.clear()

                            # burst time of new process getting the cpu decreamented
                            waiting_queue[waiting_process][2] = waiting_queue[waiting_process][2] - 1

                            # a reference created for the precess who got the cpu and process removed from waiting_queue
                            process_with_CPU[waiting_process] = waiting_queue.pop(
                                waiting_process)

                            # printing proocess
                            keys_of_item_with_CPU = process_with_CPU.keys()
                            keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                            key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                            for i in range(10):
                                self.output.insert(END, "[]")
                                self.output.update_idletasks()
                            time.sleep(0.3)
                            self.output.insert(END, "\n")
                            self.output.insert(END, "{}: completed. Time: 1s\n".format(waiting_process))
                            self.output.update_idletasks()

                            # current time increamented
                            current_time += 1
                            break

                        # if burst time of process with current cpu is less than the process in waiting queue
                        elif (waiting_queue[waiting_process][2] > process_with_CPU[key2][2] and process_with_CPU[key2][2] != 0):

                            # burst time of process with cpu decrements
                            process_with_CPU[key2][2] = process_with_CPU[key2][2] - 1

                            # printing proocess
                            keys_of_item_with_CPU = process_with_CPU.keys()
                            keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                            key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                            for i in range(10):
                                self.output.insert(END, "[]")
                                self.output.update_idletasks()
                            time.sleep(0.3)
                            self.output.insert(END, "\n")
                            self.output.insert(END, "{}: completed. Time: 1s\n".format(key_of_item_with_CPU))
                            self.output.update_idletasks()

                            # current time increamented
                            current_time += 1
                            break

                        else:
                            process_with_CPU[key2][2] = process_with_CPU[key2][2] - 1

                            # printing proocess
                            keys_of_item_with_CPU = process_with_CPU.keys()
                            keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                            key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                            for i in range(10):
                                self.output.insert(END, "[]")
                                self.output.update_idletasks()
                            time.sleep(0.3)
                            self.output.insert(END, "\n")
                            self.output.insert(END, "{}: completed. Time: 1s\n".format(key_of_item_with_CPU))
                            self.output.update_idletasks()

                            # current time increamented
                            current_time += 1

                    # check if burst time of process with cpu is equal to 0
                    elif (process_with_CPU[key2][2] == 0):

                        process_with_CPU.clear()

                        # burst time of new process getting the cpu decreamented
                        waiting_queue[waiting_process][2] = waiting_queue[waiting_process][2] - 1

                        # process scheduled to cpu
                        # CPU_schedule[waiting_process] = value

                        # a reference created for the precess who got the cpu and process removed from waiting_queue
                        process_with_CPU[waiting_process] = waiting_queue.pop(
                            waiting_process)

                        if (bool(waiting_queue) == False):
                            waiting_queue.update(process_with_CPU)

                        # printing proocess
                        keys_of_item_with_CPU = process_with_CPU.keys()
                        keys_of_item_with_CPU_list = list(keys_of_item_with_CPU)
                        key_of_item_with_CPU = keys_of_item_with_CPU_list[0]

                        for i in range(10):
                            self.output.insert(END, "[]")
                            self.output.update_idletasks()
                        time.sleep(0.3)
                        self.output.insert(END, "\n")
                        self.output.insert(END, "{}: completed. Time: 1s\n".format(key_of_item_with_CPU))
                        self.output.update_idletasks()

                        # current time increamented
                        current_time += 1
                        break

            if (all(process[2] == 0 for process in processes.values())):
                break

        # Calculate and print Average Wait Time
        avg_wait = current_time / self.count_process
        time.sleep(0.3)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()

    # Priority Scheduling Algorithm
    def ps(self):
        self.output.insert(END, "PS Scheduling:\n")
        dict1 = self.processes
        dict1 = dict(sorted(dict1.items(), key=lambda x: x[1][0]))  
        for i in range(5):
            time.sleep(0.3)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()

        wt = {}
        total_wt = 0
        prev_end_time = 0
        for i in dict1:
            wt[i] = prev_end_time
            total_wt += wt[i]
            prev_end_time += dict1[i][2]
            
            print(f"Process {i}  runs from {wt[i]} to {prev_end_time}")

        # Calculate and print Average Wait Time
        avg_wait = total_wt / self.count_process
        time.sleep(0.3)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()

    # Priority Scheduling with Round Robin Algorithm
    def ps_rr(self, quantum):
        self.output.insert(END, "PS with RR Scheduling:\n")
        dict2 = self.processes
        dict2 = dict(sorted(dict2.items(), key=lambda x: x[1][0])) 
        for i in range(5):
            time.sleep(0.3)
            self.output.insert(END, ".\n")
            self.output.update_idletasks()
        print(dict2)
        waits = {key: 0 for key in dict2.keys()} #total waiting time
        prev_end = {key: 0 for key in dict2.keys()} #previous waiting time
        tq = quantum
        print("Time quantum = ", tq)


        cur_t = 0
        dict1 = {}
        for process, value in dict2.items():
            priority = value[0]
            if priority not in dict1:
                dict1[priority] = {}
            dict_temp = dict1[priority]
            dict_temp[process] = value[2]
        
        for i in dict1:
            cur_prio = dict1[i]

            while any(value > 0 for value in cur_prio.values()): # checking if priority has completed RR

                for j in cur_prio:     #j = process, curprio[j] = bt
                    if (cur_prio[j] > 0):
                        st = cur_t
                        waits[j] += cur_t - prev_end[j]

                        if (cur_prio[j] >= tq):    #comparing bt with tq
                            cur_prio[j] -= tq
                            cur_t += tq
                        else:
                            cur_t += cur_prio[j]
                            cur_prio[j] = 0

                        prev_end[j] = cur_t

                    print(f"Process {j}  runs from {st} to {cur_t}")

        # Calculate and print Average Wait Time
        avg_wait = sum(waits.values())  / self.count_process
        time.sleep(0.3)
        self.output.insert(END, "Average Waiting Time: {}\n".format(avg_wait))
        self.output.update_idletasks()
