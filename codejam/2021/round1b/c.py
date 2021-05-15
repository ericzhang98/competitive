import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read():
    val = int(input())
    if val == -1:
        raise Exception("bad")
    return val

def solution(N,B):
    total = N*B

    cur_state = [0,0,0,0]
    cur_indices = [[], [], [], 1]

    for _ in range(total):
        val = read()
        nxt_state = None
        nxt_indices = None
        best_ev = -1
        done, num_top, num_second_top, nxt_height = cur_state
        idx_to_write = None

        # cand place in top spot
        if num_top > 0:
            ev_cand = val * 10**14 + dp(done+1,num_top-1,num_second_top,nxt_height)
            if ev_cand >= best_ev:
                best_ev = ev_cand
                nxt_state = [done+1,num_top-1,num_second_top,nxt_height]
                nxt_indices = copy.deepcopy(cur_indices)
                idx_to_write = nxt_indices[1][0]
                nxt_indices[0].append(nxt_indices[1].pop(0))

        # cand place in second top spot
        if num_second_top > 0:
            ev_cand = val  * 10**13 + dp(done,num_top+1,num_second_top-1,nxt_height)
            if ev_cand >= best_ev:
                best_ev = ev_cand
                nxt_state = [done,num_top+1,num_second_top-1,nxt_height]
                nxt_indices = copy.deepcopy(cur_indices)
                idx_to_write = nxt_indices[2][0]
                nxt_indices[1].append(nxt_indices[2].pop(0))

        # cand place in next block
        if done + num_top + num_second_top < N:
            if nxt_height == 12:
                ev_cand = val * 10**nxt_height + dp(done,num_top,num_second_top+1,0)
                if ev_cand >= best_ev:
                    best_ev = ev_cand
                    nxt_state = [done,num_top,num_second_top+1,0]
                    nxt_indices = copy.deepcopy(cur_indices)
                    idx_to_write = nxt_indices[3]
                    nxt_indices[2].append(nxt_indices[3])
                    nxt_indices[3] += 1
            else:
                ev_cand = val * 10**nxt_height + dp(done,num_top,num_second_top,nxt_height+1)
                if ev_cand >= best_ev:
                    best_ev = ev_cand
                    nxt_state = [done,num_top,num_second_top,nxt_height+1]
                    nxt_indices = copy.deepcopy(cur_indices)
                    idx_to_write = nxt_indices[3]

        assert(nxt_state is not None)
        assert(nxt_indices is not None)
        cur_state = nxt_state
        cur_indices = nxt_indices
        print(idx_to_write)

    assert(cur_state == [N,0,0,0])
    assert(cur_indices == [list(range(1,N+1)),[],[],N+1])
    return

    """
    current_spaces = [B] * N

    @functools.lru_cache(None)
    def single_ev(space):
        if space == 0:
            return 0
        else:
            return sum(4.5 * 10**p for p in range(B-space, B))

    def total_ev(spaces):
        ev = 0
        for space in spaces:
            ev += single_ev(space)
        return ev

    amt = 0
    for exchange in range(total):
        val = read()
        best_ev = -1
        best_i = -1
        for i in range(N):
            if current_spaces[i] > 0:
                current_spaces[i] -= 1
                cand_ev = val * 10**(B-current_spaces[i]-1) + total_ev(current_spaces)
                #eprint(f"val: {val} cand_ev: {cand_ev}")
                current_spaces[i] += 1
                if cand_ev > best_ev:
                    best_i = i
                    best_ev = cand_ev
        #eprint(f"exchange: {exchange} current_spaces: {current_spaces} best i: {best_i}")
        print(best_i+1)
        current_spaces[best_i] -= 1
        amt += val * 10**(B-current_spaces[best_i]-1) 
    eprint(total_ev([B] * N))
    return amt
    """

# dp on [done][num top spots][num second top spots][height of next tower]
# done + num top spots + num second top spots <= N

@functools.lru_cache(None)
def dp(done, num_top, num_second_top, nxt_height):
    #print(done,num_top,num_second_top,nxt_height)
    N = 20
    B = 15
    if done == N:
        #print(done, num_top, num_second_top, nxt_height)
        assert(num_top == 0 and num_second_top == 0 and nxt_height == 0)
        return 0

    ev = 0
    for nxt_num in range(0,10):
        ev_cand = []
        # cand place in top spot
        if num_top > 0:
            ev_cand.append(nxt_num * 10**14 + dp(done+1,num_top-1,num_second_top,nxt_height))
        # cand place in second top spot
        if num_second_top > 0:
            ev_cand.append(nxt_num * 10**13 + dp(done,num_top+1,num_second_top-1,nxt_height))
        # cand place in next block
        if done + num_top + num_second_top < N:
            if nxt_height == 12:
                ev_cand.append(nxt_num * 10**nxt_height + dp(done,num_top,num_second_top+1,0))
            else:
                ev_cand.append(nxt_num * 10**nxt_height + dp(done,num_top,num_second_top,nxt_height+1))
        ev += max(ev_cand)

    return ev / 10

#dp(0,0,0,0)

T,N,B,P = map(int, input().split())
for case_num in range(1, T + 1):
    solution(N,B)
