def algorithm(nop,p, a):
    number_of_process = int(nop)

    index = list()
    for i in range(number_of_process):
        index.append(i)

    at = list()
    bt = list()

    for i in range(len(a)):
        if(i < number_of_process):
            at.append(int(a[i]))
        elif(i >= number_of_process):
            bt.append(int(a[i]))

    final_at = at.copy()
    final_bt = bt.copy()

    priority = list()
    for i in range(len(p)):
        priority.append(int(p[i]))
    final_priority = priority.copy()

    ready_queue = list()
    cpu_time = 0
    ct= list()
    index_manager = list()
    temp_final_priority = final_priority.copy()

    while(len(at) != 0):
        for i in range(len(at)):
            if(at[i] <= cpu_time):
                ready_queue.append(i)
        priority_of_ready = list()
        for i in ready_queue:
            priority_of_ready.append(priority[i])
        if(len(priority_of_ready) == 0):
            cpu_time = cpu_time + 1
            continue
        lowest_priority = min(priority_of_ready)
        temp_index = priority.index(lowest_priority)
        temp_bt = bt[temp_index]
        gc = cpu_time + temp_bt
        cpu_time = gc
        at.pop(temp_index)
        bt.pop(temp_index)
        priority.pop(temp_index)
        ct.append(gc)
        ready_queue = list()

        counter = 0
        for element in final_priority:
            if(element == lowest_priority):
                counter = counter+1
        if(counter == 1):
            temp_index2 = final_priority.index(lowest_priority)
            index_manager.append(temp_index2)
        else:
            temp_index2 = temp_final_priority.index(lowest_priority)
            temp_final_priority[temp_index2] = " "
            index_manager.append(temp_index2)


    final_ct = list()
    for i in range(len(index_manager)):
        temp_index = index_manager.index(i)
        final_ct.append(ct[temp_index])

    final_tat = list()
    final_wt = list()

    for i in range(number_of_process):
        final_tat.append(round((final_ct[i] - final_at[i]),1))
        final_wt.append(round((final_tat[i] - final_bt[i]),1))


    final_rt = final_wt.copy()

    ct_answer = "CT\n"
    for i in final_ct:
        ct_answer = ct_answer + str(i) + "\n"
    at_answer = "AT\n"
    for i in final_at:
        at_answer = at_answer + str(i) + "\n"
    bt_answer = "BT\n"
    for i in final_bt:
        bt_answer = bt_answer + str(i) + "\n"
    tat_answer = "TAT\n"
    for i in final_tat:
        tat_answer = tat_answer + str(i) + "\n"
    wt_answer = "WT\n"
    for i in final_wt:
        wt_answer = wt_answer + str(i) + "\n"
    rt_answer = "RT\n"
    for i in final_rt:
        rt_answer = rt_answer + str(i) + "\n"
    pr_answer = "PRIO.\n"
    for i in final_priority:
        pr_answer = pr_answer + str(i) + "\n"

    answer = at_answer + " " + bt_answer + " " + ct_answer +" "+ tat_answer +" "+ wt_answer +" "+ rt_answer +" "+pr_answer
    # FCFS_table = pd.DataFrame({
    #     "AT" : final_at,
    #     "BT" : final_bt,
    #     "CT" : final_ct,
    #     "TAT" : final_tat,
    #     "WT" : final_wt,
    #     "RT" : final_rt
    #     })
    return answer

    # priority_scheduling_table = pd.DataFrame({
    #     "AT" : final_at,
    #     "BT" : final_bt,
    #     "CT" : final_ct,
    #     "TAT" : final_tat,
    #     "WT" : final_wt,
    #     "RT" : final_rt,
    #     "PRIORITY" : final_priority
    #     })
    # print("\n")
    # print(priority_scheduling_table)
    #
    # print("\n average waiting time is : ",sum(final_wt)/number_of_process)




