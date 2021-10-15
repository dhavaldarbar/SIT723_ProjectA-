import numpy as np
import random
import sys
import time

#  Fisher and Thompson 20x5 instance, alternate name (mt20)
#  20 5
#  0 29 1 9 2 49 3 62 4 44
#  0 43 1 75 3 69 2 46 4 72
#  1 91 0 39 2 90 4 12 3 45
#  1 81 0 71 4 9 2 85 3 22
#  2 14 1 22 0 26 3 21 4 72
#  2 84 1 52 4 48 0 47 3 6
#  1 46 0 61 2 32 3 32 4 30
#  2 31 1 46 0 32 3 19 4 36
#  0 76 3 76 2 85 1 40 4 26
#  1 85 2 61 0 64 3 47 4 90
#  1 78 3 36 0 11 4 56 2 21
#  2 90 0 11 1 28 3 46 4 30
#  0 85 2 74 1 10 3 89 4 33
#  2 95 0 99 1 52 3 98 4 43
#  0 6 1 61 4 69 2 49 3 53
#  1 2 0 95 3 72 4 65 2 25
#  0 37 2 13 1 21 3 89 4 55
#  0 86 1 74 4 88 2 48 3 79
#  1 69 2 51 0 11 3 89 4 74
#  0 13 1 7 2 76 3 52 4 45
power = {
    0: {0:29, 1:9, 2:49, 3:62, 4:44},
    1: {0:43, 1:75, 2:69, 3:46, 4:72},
    2: {0:91, 1:39, 2:90, 3:12, 4:45},
    3: {0:81, 1:71, 2:9, 3:85, 4:22},
    4: {0:14, 1:22, 2:26, 3:21, 4:72},
    5: {0:84, 1:52, 2:48, 3:47, 4:6},
    6: {0:46, 1:61, 2:32, 3:32, 4:30},
    7: {0:31, 1:46, 2:32, 3:19, 4:36},
    8: {0:76, 1:76, 2:85, 3:40, 4:26},
    9: {0:85, 1:61, 2:64, 3:47, 4:90},
    10: {0:78, 1:36, 2:11, 3:56, 4:21},
    11: {0:90, 1:11, 2:28, 3:46, 4:30},
    12: {0:85, 1:74, 2:10, 3:89, 4:33},
    13: {0:95, 1:99, 2:52, 3:98, 4:43},
    14: {0:6, 1:61, 2:69, 3:49, 4:53},
    15: {0:2, 1:95, 2:72, 3:65, 4:25},
    16: {0:37, 1:13, 2:21, 3:89, 4:55},
    17: {0:86, 1:74, 2:88, 3:48, 4:79},
    18: {0:69, 1:51, 2:11, 3:89, 4:74},
    19: {0:13, 1:7, 2:76, 3:52, 4:45}
    
}

machine = {
    0: {0:0, 1:1, 2:2, 3:3, 4:4},
    1: {0:0, 1:1, 2:3, 3:2, 4:4},
    2: {0:1, 1:0, 2:2, 3:4, 4:3},
    3: {0:1, 1:0, 2:4, 3:2, 4:3},
    4: {0:2, 1:1, 2:0, 3:3, 4:4},
    5: {0:2, 1:1, 2:4, 3:0, 4:3},
    6: {0:1, 1:0, 2:2, 3:3, 4:4},
    7: {0:2, 1:1, 2:0, 3:3, 4:4},
    8: {0:0, 1:3, 2:2, 3:1, 4:4},
    9: {0:1, 1:2, 2:0, 3:3, 4:4},
    10: {0:1, 1:3, 2:0, 3:4, 4:2},
    11: {0:2, 1:0, 2:1, 3:3, 4:4},
    12: {0:0, 1:2, 2:1, 3:3, 4:4},
    13: {0:2, 1:0, 2:1, 3:3, 4:4},
    14: {0:0, 1:1, 2:4, 3:2, 4:3},
    15: {0:1, 1:0, 2:3, 3:4, 4:2},
    16: {0:0, 1:2, 2:1, 3:3, 4:4},
    17: {0:0, 1:1, 2:4, 3:2, 4:3},
    18: {0:1, 1:2, 2:0, 3:3, 4:4},
    19: {0:0, 1:1, 2:2, 3:3, 4:4}
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

    #print("result_data   ",result_data)
    # import pprint
    # pprint.pprint(c)
    # print("max ", max(list(result_data.values())))
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

def simulated_annealing(old_seq,Ti = 10000,Tf = 1 ,alpha = 0.60):
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

new_seq = [12,11,16,8,6,4,5,7,10,8,9,0,14,1,15,9,10,4,17,13,6,2,16,14,15,8,17,9,3,0,14,5,18,15,10,7,1,19,13,6,2,18,4,16,0,11,17,19,7,5,1,14,18,6,12,4,19,9,13,2,11,16,8,19,7,4,15,11,16,17,12,0,19,14,17,5,3,18,10,13,1,18,15,2,10,6,7,3,0,9,8,5,11,1,2,3,12,3,12,13] 
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






    

