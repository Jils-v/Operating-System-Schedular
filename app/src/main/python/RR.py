def algorithm(nop,tq, a):
    number_of_process = int(nop)
    at = list()
    bt = list()
    arrival_time = list()
    burst_time = list()
    response_time = list()
    completion_time = list()
    tat = list()
    waiting_time = list()
    gantt_chart = list()
    tq = int(tq)

    for i in range(len(a)):
        if(i < number_of_process):
            at.append([i,int(a[i])])
            arrival_time.append(int(a[i]))
            bt.append([i,int(a[i])])
            burst_time.append(int(a[i]))

    cpu_time = 0
    ready_queue = list()

    for i in at:
        if(i[1] <= cpu_time):
            ready_queue.append(i)
    for i in range(len(ready_queue)):
        for j in range(len(ready_queue)-i-1):
            if(ready_queue[j][1] > ready_queue[j+1][1]):
                temp = ready_queue[j]
                ready_queue[j] = ready_queue[j+1]
                ready_queue[j+1] = temp

    while(len(at) != 0 or len(ready_queue) != 0):
        if(len(ready_queue)==0):
            cpu_time = cpu_time+1
            for i in at:
                if(i[1] <= cpu_time):
                    ready_queue.append(i)
            for i in range(len(ready_queue)):
                for j in range(len(ready_queue)-i-1):
                    if(ready_queue[j][1] > ready_queue[j+1][1]):
                        temp = ready_queue[j]
                        ready_queue[j] = ready_queue[j+1]
                        ready_queue[j+1] = temp
            continue

        while(len(ready_queue) != 0):
            process = ready_queue[0]
            ready_queue.pop(0)
            index = process[0]
            bt_of_process = bt[index][1]

            if(process in at):
                at.remove(process)

            if(bt_of_process <= tq):
                gantt_chart.append(cpu_time)
                gantt_chart.append(str(process[0]))
                cpu_time = cpu_time + bt_of_process
                gantt_chart.append(cpu_time)
                temporary = list()
                for k in at:
                    if(k[1] <= cpu_time):
                        if(k not in ready_queue):
                            temporary.append(k)
                        for i in range(len(temporary)):
                            for j in range(len(temporary)-i-1):
                                if(temporary[j][1] > temporary[j+1][1]):
                                    t = temporary[j]
                                    temporary[j] = temporary[j+1]
                                    temporary[j+1] = t
                if(len(temporary) != 0):
                    for i in temporary:
                        ready_queue.append(i)

            else:
                gantt_chart.append(cpu_time)
                gantt_chart.append(str(process[0]))
                cpu_time = cpu_time + tq
                gantt_chart.append(cpu_time)
                bt_of_process = bt_of_process - tq
                bt[process[0]][1] = bt_of_process
                temp_remaining_execution = process
                temporary = list()
                for k in at:
                    if(k[1] <= cpu_time):
                        if(k not in ready_queue):
                            temporary.append(k)
                        for i in range(len(temporary)):
                            for j in range(len(temporary)-i-1):
                                if(temporary[j][1] > temporary[j+1][1]):
                                    t = temporary[j]
                                    temporary[j] = temporary[j+1]
                                    temporary[j+1] = t
                if(len(temporary) != 0):
                    for i in temporary:
                        ready_queue.append(i)
                ready_queue.append(temp_remaining_execution)


    for i in range(number_of_process):
        for j in range(-1, -len(gantt_chart), -1):
            if(gantt_chart[j] == str(i)):
                completion_time.append(gantt_chart[j+1])
                break

    for i in range(number_of_process):
        tat.append(completion_time[i] - arrival_time[i])
        waiting_time.append(tat[i] - burst_time[i])

    for i in range(number_of_process):
        for j in range(len(gantt_chart)):
            if(gantt_chart[j] == str(i)):
                response_time.append(gantt_chart[j-1] - arrival_time[i])
                break

    ct_answer = "CT\n"
    for i in completion_time:
        ct_answer = ct_answer + str(i) + "\n"
    at_answer = "AT\n"
    for i in arrival_time:
        at_answer = at_answer + str(i) + "\n"
    bt_answer = "BT\n"
    for i in burst_time:
        bt_answer = bt_answer + str(i) + "\n"
    tat_answer = "TAT\n"
    for i in tat:
        tat_answer = tat_answer + str(i) + "\n"
    wt_answer = "WT\n"
    for i in waiting_time:
        wt_answer = wt_answer + str(i) + "\n"
    rt_answer = "RT\n"
    for i in response_time:
        rt_answer = rt_answer + str(i) + "\n"

    answer = at_answer + " " + bt_answer + " " + ct_answer +" "+ tat_answer +" "+ wt_answer +" "+ rt_answer
    # FCFS_table = pd.DataFrame({
    #     "AT" : final_at,
    #     "BT" : final_bt,
    #     "CT" : final_ct,
    #     "TAT" : final_tat,
    #     "WT" : final_wt,
    #     "RT" : final_rt
    #     })
    return answer
    # RR_table = pd.DataFrame({
    #     "AT" : arrival_time,
    #     "BT" : burst_time,
    #     "CT" : completion_time,
    #     "TAT" : tat,
    #     "WT" : waiting_time,
    #     "RT" : response_time
    #     })
    #
    # print("\n")
    # print(RR_table)
    # print("\n average waiting time : ",sum(waiting_time)/number_of_process)


