import numpy as np
import random
import sys
import time

#  Lawrence 10x10 instance (Table 6, instance 5); also called (seta5) or (A5)
#  10 10
#  6 9 1 81 4 55 2 40 8 32 3 37 0 6 5 19 9 81 7 40
#  7 21 2 70 9 65 4 64 1 46 5 65 8 25 0 77 3 55 6 15
#  2 85 5 37 0 40 3 24 1 44 6 83 4 89 8 31 7 84 9 29
#  4 80 6 77 7 56 0 8 2 30 5 59 3 38 1 80 9 41 8 97
#  0 91 6 40 4 88 1 17 2 71 3 50 9 59 8 80 5 56 7 7
#  2 8 6 9 3 58 5 77 1 29 8 96 0 45 9 10 4 54 7 36
#  4 70 3 92 1 98 5 87 6 99 7 27 8 86 9 96 0 28 2 73
#  1 95 7 92 3 85 4 52 6 81 9 32 8 39 0 59 2 41 5 56
#  3 60 8 45 0 88 2 12 1 7 5 22 4 93 9 49 7 69 6 27
#  0 21 2 61 3 68 5 26 6 82 9 71 8 44 4 99 7 33 1 84
#  +++++++++++++++++++++++++++++
power = {
    0: {0:9,  1:81, 2:55, 3:40, 4:32, 5:37 , 6:6,  7:19, 8:81, 9:40},
    1: {0:21, 1:70, 2:65, 3:64, 4:46, 5:65 , 6:25, 7:77, 8:55, 9:15},
    2: {0:85, 1:37, 2:40, 3:24, 4:44, 5:83 , 6:89, 7:31, 8:84, 9:29},
    3: {0:80, 1:77, 2:56, 3:8,  4:30, 5:59 , 6:38, 7:80, 8:41, 9:97},
    4: {0:91, 1:40, 2:88, 3:17, 4:71, 5:50 , 6:59, 7:80, 8:56, 9:7},
    5: {0:8,  1:9,  2:58, 3:77, 4:29, 5:96 , 6:45, 7:10, 8:54, 9:36},
    6: {0:70, 1:92, 2:98, 3:87, 4:99, 5:27 , 6:86, 7:96, 8:28, 9:73},
    7: {0:95, 1:92, 2:85, 3:52, 4:81, 5:32 , 6:39, 7:59, 8:41, 9:56},
    8: {0:60, 1:45, 2:88, 3:12, 4:7,  5:22 , 6:93, 7:49, 8:69, 9:27},
    9: {0:21, 1:61, 2:68, 3:26, 4:82, 5:71 , 6:44, 7:99, 8:33, 9:84},
    
}

machine = {
    0: {0:6, 1:1, 2:4, 3:2, 4:8, 5:3 , 6:0, 7:5, 8:9, 9:7},
    1: {0:7, 1:2, 2:9, 3:4, 4:1, 5:5 , 6:8, 7:0, 8:3, 9:6},
    2: {0:2, 1:5, 2:0, 3:3, 4:1, 5:6 , 6:4, 7:8, 8:7, 9:9},
    3: {0:4, 1:6, 2:7, 3:0, 4:2, 5:5 , 6:3, 7:1, 8:9, 9:8},
    4: {0:0, 1:6, 2:4, 3:1, 4:2, 5:3 , 6:9, 7:8, 8:5, 9:7},
    5: {0:2, 1:6, 2:3, 3:5, 4:1, 5:8 , 6:0, 7:9, 8:4, 9:7},
    6: {0:4, 1:3, 2:1, 3:5, 4:6, 5:7 , 6:8, 7:9, 8:0, 9:2},
    7: {0:1, 1:7, 2:3, 3:4, 4:6, 5:9 , 6:8, 7:0, 8:2, 9:5},
    8: {0:3, 1:8, 2:0, 3:2, 4:1, 5:5 , 6:4, 7:9, 8:7, 9:6},
    9: {0:0, 1:2, 2:3, 3:5, 4:6, 5:9 , 6:8, 7:4, 8:7, 9:1},
}

# used_machine ={}
debug=False

# def prepare_used_machine_dict(j, i, m, tuple):


# input1 = 215013424301243205154530


def solution(li):
    job_data = {}
    result_data = {}
    used_machine = {}
    # li = [int(x) for x in str(input1)]
    for j in li:
        if j  in job_data:
            job_data[j] = job_data[j] + 1
        else:
            job_data[j] = 0
        i = job_data[j]
        m = machine[j][i]
        tuple = (j,i)
        if i > 0:
            if m in used_machine:
                my_list = used_machine[m]
                new_tuple = (j,i-1)
                ans = max(result_data[my_list[len(my_list)-1]], result_data[new_tuple]) + power[j][i]
                result_data[tuple] = ans
            else:
                new_tuple = (j,i-1)
                ans = result_data[new_tuple] + power[j][i]
                result_data[tuple] = ans
        else:
            if m in used_machine:
                my_list = used_machine[m]
                # print(result_data)
                ans = result_data[my_list[len(my_list)-1]] + power[j][i]
                result_data[tuple] = ans
            else:
                ans = power[j][i]
                result_data[tuple] = ans
        if m in used_machine:
            used_machine[m].append(tuple)
        else:
            used_machine[m] = [tuple]

    #print("Initial Solution  ",result_data)
    # import pprint
    # pprint.pprint(c)
    #print("max ", max(list(result_data.values())))
    return max(list(result_data.values()))

def generateRandomSequence():
        indexes = np.array([i for i in range(0,6)])
        # print(indexes)
        random.shuffle(indexes)
        print("Initial Solution",indexes)
        return indexes.tolist()

def swapTwoJobs(seq,pos1,pos2):
    seq[pos1], seq[pos2] = seq[pos2], seq[pos1]
    return seq

def simulated_annealing(old_seq,Ti = 10000,Tf = 1 ,alpha = 0.70):
    #Number of jobs given
    n = len(old_seq)
    default_timer = time.time

    s = default_timer.__call__()
    # neh=NEH()
    # #Initialize the primary seq
    # # old_seq,schedules,old_makeSpan, _ = self.palmer_heuristic()
    # # old_seq, schedules, old_makeSpan, _ = n.nehAlgo(self.data, self.nb_machines, self.nb_jobs)
    # old_seq,  old_makeSpan = neh.nehAlgo(
    #     self.data, self.nb_machines, self.nb_jobs)
    # print('Initial Sequence of NEH =>', old_seq)
    # print('Initial Sequence of NEH makespan =>', old_makeSpan)
    # old_seq=self.generateRandomSequence()
    # old_makeSpan = commonFunction.makespan(old_seq, self.data, self.nb_machines)[
    #         self.nb_machines - 1][len(old_seq)]

    # old_seq = [3,4,2,4,2,3,0,1,2,4,3,2,0,5,1,5,4,5,3,0,1,2,3,4]
    old_makeSpan = solution(old_seq)
    if debug:
        print('Initial Sequence =>', old_seq)
        print('Initial Sequence makespan =>', old_makeSpan)
    bestSolution = old_makeSpan
    bestSequence = old_seq
    new_seq = []       
    delta_mk1 = 0
    #Initialize the temperature
    if debug:
        print("Initial Temperature =>",Ti)
        print("Final Temperature =>",Tf)
        print("Alpha",alpha)
    T = Ti
    Tf = Tf
    alpha = alpha
    # of iterations
    temp_cycle = 0
    count =0 
    count2 = 0
    
    while T >= Tf  :
        count = count+1
        for i1 in range(30):    
            count2 +=1
        new_seq = old_seq.copy()
        # Insertion method
        # job = new_seq.pop(randint(0,n-1))
        # new_seq.insert(randint(0,n-1),job) # Swap and insertion for new sequence 
        
        #Swap Method
        u,v=random.randint(0, n-1), random.randint(0, n-1)
        job=u
        new_seq=swapTwoJobs(new_seq,u,v)
        # print("new_seq ",new_seq)

        # Call solution
        new_make_span = solution(new_seq)
        
        # new_make_span = commonFunction.makespan(new_seq, self.data, self.nb_machines)[
        #     self.nb_machines - 1][len(new_seq)]
        # new_make_span = self._get_makespan(new_seq,self.data)
        if debug:
            print('Job :',job)
            print('New Sequence :', new_seq)
            print('New Sequence make span:', new_make_span)
        delta_mk1 = new_make_span - old_makeSpan
        # print("Delta ",delta_mk1)
        # if delta_mk1 <= 0:
        #     old_seq = new_seq
        #     old_makeSpan = new_make_span
        r=(old_seq == new_seq)
        if debug:
            print('Check Sequence Change',r)
        if r == False:
            if new_make_span < old_makeSpan:
                if debug:
                    print("MakeSpan Swap Sequence", "new_make_span =>",new_make_span," old_makeSpan=>",old_makeSpan)
                old_seq = new_seq
                old_makeSpan = new_make_span
                
            else :
                delta_mk1 = new_make_span - old_makeSpan
                Aprob = np.exp((-1*(delta_mk1)/T))
                p = np.random.uniform(0.1,0.9)
                if debug:
                    print("Proability",p)
                    print("Delta Change ", delta_mk1)
                    print("Aprob => ", Aprob)
                    print(p <= Aprob)
                if p < Aprob:
                    old_seq = new_seq
                    old_makeSpan = new_make_span
                    if debug:
                        print("Proability Swap Sequence")
                else :
                    #The solution is discarded
                    if debug:
                        print("Discard Iteration")
                        print('Old Sequence :',old_seq)
                    pass
        T = T * alpha 
        if debug:
            print("New Temperature=>",T)
        temp_cycle += 1
        if bestSolution > old_makeSpan:
            
            bestSolution = old_makeSpan
            bestSequence = old_seq
            if debug:
                print("Best Solution Swap")
                print('New Swap Sequence :', bestSequence)
                print('New Sequence make span:', bestSolution)
                print("Iteration Count:", count)
    

    e = default_timer.__call__()
    if debug:
        print("Best Sequence",bestSequence)
        print("Best MakeSpan", bestSolution)
        print("Iteration Count:", count)
    
    #Result Sequence
    # seq=bestSequence
    # old_makeSpan=bestSolution
    print(bestSolution-old_makeSpan)
    d = float((bestSolution-old_makeSpan)/old_makeSpan)
    return bestSequence, bestSolution, e-s, d


# old_seq = [3,4,2,4,2,3,0,1,2,4,3,2,0,5,1,5,4,5,3,0,1,2,3,4] ,0,4,3,2,1,3,0,4,2,3,2,1,0,3,1,0,2,4,3,0,1,2,3,0,4,2,3,1,4,1

new_seq = [8,3,7,5,1,6,8,5,3,7,6,1,8,0,3,6,7,1,8,4,2,0,6,7,8,5,7,4,9,2,3,7,6,8,2,4,2,5,6,2,9,8,3,2,7,5,9,6,2,8,3,5,6,7,9,4,1,2,0,4,6,9,3,1,7,2,8,0,9,4,6,8,2,5,3,9,1,4,0,3,5,0,9,1,4,0,3,4,0,9,1,5,0,4,1,0,1,5,7,9] 

n = len(new_seq)
for j in range(5):
    new_seq, best_value, best_time, delta = simulated_annealing(new_seq)
    print("Best Sequence",new_seq)
    print("Best MakeSpan", best_value)
    print("Time duration", best_time)
    print("Delta     ", delta)
    
    
    for i in range(10):
        u,v=random.randint(0, n-1), random.randint(0, n-1)
        new_seq=swapTwoJobs(new_seq,u,v)
        #print("New Random Seq ", new_seq)
        
    


# generateRandomSequence()
# generateRandomSequence()
# print(generateRandomSequence())
# print(solution(old_seq))
# solution(old_seq)
# solution(new_seq)
# solution(424230124320515453012343)
# solution(242301243205154530123434)
# solution(423012432051545301234342)
# print()
# pprint.pprint(used_machine)



    

