import numpy as np
import random
import sys
import time
power = {
    0: {0:1, 1:3, 2:6, 3:7, 4:3, 5:6},
    1: {0:8, 1:5, 2:10, 3:10, 4:10, 5:4},
    2: {0:5, 1:4, 2:8, 3:9, 4:1, 5:7},
    3: {0:5, 1:5, 2:5, 3:3, 4:8, 5:9},
    4: {0:9, 1:5, 2:5, 3:4, 4:3, 5:1},
    5: {0:3, 1:9, 2:9, 3:10, 4:4, 5:1}
}

machine = {
    0: {0:2, 1:0, 2:1, 3:3, 4:5, 5:4},
    1: {0:1, 1:2, 2:4, 3:5, 4:0, 5:3},
    2: {0:2, 1:3, 2:5, 3:0, 4:1, 5:4},
    3: {0:1, 1:0, 2:2, 3:3, 4:4, 5:5},
    4: {0:2, 1:4, 2:4, 3:5, 4:0, 5:3},
    5: {0:1, 1:5, 2:5, 3:0, 4:4, 5:2}
}

used_machine ={}
debug=False

def prepare_used_machine_dict(j, i, m, tuple):
    if m in used_machine:
        used_machine[m].append(tuple)
    else:
        used_machine[m] = [tuple]

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
        prepare_used_machine_dict(j, i, m, tuple)
    # print(result_data)
    # import pprint
    # pprint.pprint(c)
    return sum(list(result_data.values()))

def generateRandomSequence():
        indexes = np.array([i for i in range(0,6)])
        # print(indexes)
        random.shuffle(indexes)
        print("Initial Solution",indexes)
        return indexes.tolist()

def swapTwoJobs(seq,pos1,pos2):
    seq[pos1], seq[pos2] = seq[pos2], seq[pos1]
    return seq

def simulated_annealing(old_seq,Ti = 10000,Tf = 1 ,alpha = 0.90):
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
    
    while T >= Tf  :
        new_seq = old_seq.copy()
        # Insertion method
        # job = new_seq.pop(randint(0,n-1))
        # new_seq.insert(randint(0,n-1),job) # Swap and insertion for new sequence 
        
        #Swap Method
        u,v=random.randint(0, n-1), random.randint(0, n-1)
        job=u
        new_seq=swapTwoJobs(new_seq,u,v)
        # print(new_seq)

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

    e = default_timer.__call__()
    if debug:
        print("Best Sequence",bestSequence)
        print("Best MakeSpan", bestSolution)
    #Result Sequence
    # seq=bestSequence
    # old_makeSpan=bestSolution
    print("Best Sequence",bestSequence)
    print("Best MakeSpan", bestSolution)
    print("Time duration", e-s)


old_seq = [3,4,2,4,2,3,0,1,2,4,3,2,0,5,1,5,4,5,3,0,1,2,3,4]
new_seq = [3,4,2,4,2,3,0,1,2,4,3,2,0,4,1,5,5,5,3,0,1,2,3,4] 
simulated_annealing(old_seq)

# generateRandomSequence()
# generateRandomSequence()
# print(generateRandomSequence())
# print(solution(old_seq))
# solution(424230124320515453012343)
# solution(242301243205154530123434)
# solution(423012432051545301234342)
# print()
# pprint.pprint(used_machine)



    


