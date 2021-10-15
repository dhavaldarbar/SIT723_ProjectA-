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
    0: {0:92,  1:49, 2:93, 3:48, 4:1,  5:52, 6:57,  7:16,  8:6,  9:6,   10:19,  11:96, 12:27,  13:76, 14:60},
     1: {0:4,   1:96, 2:52, 3:87, 4:94, 5:83, 6:9,   7:85,  8:47, 9:63,  10:31,  11:26, 12:46,  13:49, 14:48},
     2: {0:34,  1:34, 2:37, 3:82, 4:25, 5:43, 6:11,  7:71,  8:55, 9:34,  10:77,  11:20, 12:89,  13:23, 14:32},
     3: {0:49,  1:12, 2:52, 3:76, 4:64, 5:51, 6:84,  7:42,  8:5,  9:45,  10:20,  11:93, 12:48,  13:75, 14:100},
     4: {0:35,  1:1,  2:15, 3:49, 4:78, 5:80, 6:99,  7:88,  8:24, 9:20,  10:100, 11:28, 12:71,  13:1,  14:7},
     5: {0:69,  1:24, 2:21, 3:3,  4:28, 5:8,  6:42,  7:33,  8:40, 9:50,  10:8,   11:5,  12:13,  13:42, 14:73},
     6: {0:83,  1:15, 2:62, 3:27, 4:5,  5:65, 6:100, 7:65,  8:82, 9:89,  10:81,  11:92, 12:38,  13:47, 14:96},
     7: {0:98,  1:24, 2:75, 3:57, 4:93, 5:74, 6:10,  7:44,  8:59, 9:51,  10:82,  11:65, 12:8,   13:12, 14:24},
     8: {0:55,  1:44, 2:47, 3:75, 4:81, 5:30, 6:42,  7:100, 8:81, 9:29,  10:31,  11:47, 12:34,  13:77, 14:92},
     9: {0:18,  1:42, 2:37, 3:1,  4:67, 5:20, 6:91,  7:21,  8:57, 9:100, 10:100, 11:59, 12:77,  13:21, 14:98},
    10: {0:42,  1:16, 2:19, 3:70, 4:7,  5:74, 6:7,   7:50,  8:74, 9:46,  10:88,  11:71, 12:42,  13:34, 14:60},
    11: {0:12,  1:45, 2:7,  3:15, 4:22, 5:31, 6:70,  7:88,  8:46, 9:44,  10:45,  11:87, 12:5,   13:99, 14:70},
    12: {0:51,  1:39, 2:50, 3:39, 4:23, 5:28, 6:49,  7:5,   8:17, 9:40,  10:30,  11:62, 12:65,  13:84, 14:12},
    13: {0:92,  1:67, 2:85, 3:88, 4:18, 5:13, 6:70,  7:69,  8:20, 9:52,  10:42,  11:82, 12:19,  13:21, 14:5},
    14: {0:34,  1:60, 2:52, 3:70, 4:51, 5:2,  6:43,  7:75,  8:45, 9:53,  10:96,  11:1,  12:44,  13:66, 14:19},
    15: {0:31,  1:44, 2:84, 3:16, 4:10, 5:4,  6:48,  7:67,  8:11, 9:21,  10:78,  11:42, 12:44,  13:37, 14:35},
    16: {0:20,  1:40, 2:37, 3:68, 4:42, 5:11, 6:6,   7:44,  8:43, 9:17,  10:3,   11:77, 12:100, 13:82, 14:5},
    17: {0:14,  1:5,  2:40, 3:70, 4:63, 5:59, 6:42,  7:74,  8:32, 9:50,  10:21,  11:29, 12:83,  13:64, 14:45},
    18: {0:70,  1:28, 2:79, 3:25, 4:98, 5:24, 6:54,  7:65,  8:93, 9:74,  10:22,  11:73, 12:75,  13:69, 14:9},
    19: {0:100, 1:46, 2:69, 3:41, 4:3,  5:18, 6:41,  7:94,  8:97, 9:30,  10:96,  11:7,  12:86,  13:83, 14:90}
    
}

machine = {
     0: {0:3, 1:1, 2:2, 3:6, 4:0, 5:4, 6:5, 7:8,  8:12, 9:13, 10:11, 11:9,  12:7,  13:14, 14:10},
     1: {0:5, 1:3, 2:6, 3:1, 4:2, 5:4, 6:0, 7:11, 8:10, 9:8,  10:9,  11:13, 12:12, 13:7,  14:14},
     2: {0:1, 1:6, 2:4, 3:2, 4:0, 5:5, 6:3, 7:9,  8:14, 9:7,  10:11, 11:12, 12:8,  13:10, 14:13},
     3: {0:3, 1:5, 2:6, 3:2, 4:0, 5:1, 6:4, 7:10, 8:12, 9:7,  10:8,  11:11, 12:14, 13:13, 14:9},
     4: {0:2, 1:1, 2:3, 3:6, 4:5, 5:4, 6:0, 7:9,  8:7,  9:11, 10:10, 11:8,  12:14, 13:13, 14:12},
     5: {0:3, 1:6, 2:5, 3:4, 4:1, 5:2, 6:0, 7:10, 8:11, 9:9,  10:8,  11:13, 12:12, 13:7,  14:14},
     6: {0:0, 1:4, 2:2, 3:6, 4:5, 5:1, 6:3, 7:14, 8:10, 9:7,  10:13, 11:9,  12:8,  13:11, 14:12},
     7: {0:6, 1:4, 2:2, 3:0, 4:1, 5:3, 6:5, 7:7,  8:13, 9:11, 10:12, 11:14, 12:10, 13:8,  14:9},
     8: {0:4, 1:0, 2:3, 3:5, 4:2, 5:6, 6:1, 7:10, 8:8,  9:7,  10:13, 11:9,  12:11, 13:12, 14:14},
    9: {0:2, 1:5, 2:0, 3:4, 4:3, 5:6, 6:1, 7:8,  8:14, 9:12, 10:10, 11:11, 12:13, 13:9,  14:7},
    10: {0:3, 1:1, 2:4, 3:6, 4:2, 5:0, 6:5, 7:12, 8:9,  9:8,  10:14, 11:13, 12:10, 13:7,  14:11},
    11: {0:6, 1:4, 2:2, 3:0, 4:1, 5:3, 6:5, 7:13, 8:9,  9:8,  10:14, 11:12, 12:11, 13:7,  14:10},
    12: {0:4, 1:5, 2:0, 3:2, 4:3, 5:6, 6:1, 7:13, 8:12, 9:14, 10:10, 11:11, 12:8,  13:7,  14:9},
    13: {0:6, 1:0, 2:5, 3:1, 4:3, 5:4, 6:2, 7:7,  8:14, 9:13, 10:8,  11:11, 12:10, 13:12, 14:9},
    14: {0:4, 1:0, 2:1, 3:5, 4:2, 5:6, 6:3, 7:10, 8:11, 9:8,  10:12, 11:13, 12:14, 13:7,  14:9},
    15: {0:6, 1:1, 2:0, 3:3, 4:4, 5:2, 6:5, 7:13, 8:14, 9:12, 10:8,  11:7,  12:11, 13:9,  14:10},
    16: {0:1, 1:4, 2:3, 3:2, 4:6, 5:0, 6:5, 7:10, 8:11, 9:12, 10:14, 11:7,  12:13, 13:9,  14:8},
    17: {0:5, 1:0, 2:3, 3:1, 4:4, 5:2, 6:6, 7:9,  8:13, 9:7,  10:10, 11:14, 12:12, 13:11, 14:8},
    18: {0:6, 1:0, 2:3, 3:4, 4:5, 5:2, 6:1, 7:12, 8:13, 9:10, 10:7,  11:9,  12:11, 13:8,  14:14},
    19: {0:5, 1:2, 2:4, 3:3, 4:1, 5:6, 6:0, 7:8,  8:11, 9:12, 10:14, 11:7,  12:9,  13:13, 14:10}

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

def simulated_annealing(old_seq,Ti = 10000,Tf = 1 ,alpha = 0.80):
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

new_seq = [16,17,0,19,10,7,4,1,16,7,4,15,5,16,14,
           7,0,2,19,5,7,1,4,16,7,18,15,5,2,19,
           16,3,7,4,18,15,5,16,10,18,19,7,2,3,18,
           12,15,17,19,7,18,4,6,7,12,18,19,1,15,3,
           7,12,18,4,5,14,19,12,14,18,17,18,10,7,12,
           2,17,15,13,1,7,6,4,10,7,13,3,6,2,0,
           7,4,13,10,0,6,1,7,13,8,5,6,8,3,13,
           12,14,0,4,10,6,8,13,16,2,5,10,15,19,13,
           3,14,6,8,4,13,1,8,6,13,17,13,18,5,17,
           9,11,0,8,1,11,6,8,10,11,0,4,9,3,11,
           8,15,6,5,11,15,8,18,10,12,19,0,15,2,11,
           9,18,14,6,8,19,10,11,4,12,14,16,8,19,9,
           16,11,1,12,10,16,15,8,11,6,16,8,18,12,5,
           8,11,13,0,10,12,9,0,3,8,11,6,10,4,17,
           9,1,14,6,0,19,17,14,2,5,6,17,0,16,4,
           11,9,13,10,14,11,3,2,5, 16,18,9,11, 17,4,
           1,1,5,9,10,3,15,13,16,17,2,3,18,12,15,5,
           9,11,15,0,17,12,13,2,1,3,14,12,14,5,9,
           15,17,2,1,19,0,12,3,13,0,9,19,2,17,14,
           16,3,1,14,9,17,3,14,2,19,9,2,1,9] 
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



    

