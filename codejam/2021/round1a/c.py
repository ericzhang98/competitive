import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect
import fractions

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

@functools.lru_cache(None)
def nCk(n, k):
    if k == 0: return 1
    return n * nCk(n-1, k-1) // k

def flip(c):
    return "TF"[c == 'T']

def solution(answers, correct):
    N, Q = len(answers), len(answers[0])
    # copy to make 3 answers
    for _ in range(3-N):
        answers.append(answers[-1])
        correct.append(correct[-1])
    answers = list(map(list, answers))

    A = answers
    S = correct

    an = sum(a == b == c for a, b, c in zip(*A))
    bn = sum(b == c != a for a, b, c in zip(*A))
    cn = sum(c == a != b for a, b, c in zip(*A))
    dn = sum(a == b != c for a, b, c in zip(*A))
    total = acount = bcount = ccount = dcount = 0
    for ar in range(an+1):
        # (1) ar + (bn-br) +    cr   +    dr   = S[0]
        # (2) ar +    br   + (cn-cr) +    dr   = S[1]
        # (3) ar +    br   +    cr   + (dn-dr) = S[2]
        br = (S[1]+S[2]-cn-dn)//2-ar  # [(2)+(3)]/2, since at least one br exists and (S[1]+S[2]-cn-dn)//2 is constant, so (S[1]+S[2]-cn-dn)%2 is always 0
        cr = (S[2]+S[0]-bn-dn)//2-ar  # [(3)+(1)]/2, since at least one cr exists and (S[2]+S[0]-bn-dn)//2 is constant, so (S[2]+S[0]-bn-dn)%2 is always 0
        dr = (S[0]+S[1]-bn-cn)//2-ar  # [(1)+(2)]/2, since at least one dr exists and (S[0]+S[1]-bn-cn)//2 is constant, so (S[0]+S[1]-bn-cn)%2 is always 0
        if not (0 <= br <= bn and 0 <= cr <= cn and 0 <= dr <= dn):
            continue  # ar is invalid
        ways = nCk(an,ar) * nCk(bn,br) * nCk(cn,cr) * nCk(dn,dr)
        total += ways
        acount += ways*ar
        bcount += ways*br
        ccount += ways*cr
        dcount += ways*dr
    result = []
    for a, b, c in zip(*A):
        if a == b == c:
            result.append(a if acount >= total*an-acount else "TF"[a == 'T'])
        elif b == c != a:
            result.append(b if bcount >= total*bn-bcount else a)
        elif c == a != b:
            result.append(c if ccount >= total*cn-ccount else b)
        elif a == b != c:
            result.append(a if dcount >= total*dn-dcount else c)
    count = max(acount, total*an-acount) + max(bcount, total*bn-bcount) + max(ccount, total*cn-ccount) + max(dcount, total*dn-dcount)
    g = math.gcd(count, total)
    return "%s %s/%s" % ("".join(result), count//g, total//g)

    """
    # flip so that person 1 always answers T
    flips = set()
    for i in range(Q):
        if answers[0][i] == 'F':
            flips.add(i)
    for i in range(Q):
        if i in flips:
            answers[0][i] = flip(answers[0][i])
            answers[1][i] = flip(answers[1][i])
            answers[2][i] = flip(answers[2][i])


    # count types
    an = sum((answers[1][i], answers[2][i]) == ('T', 'T') for i in range(Q))
    bn = sum((answers[1][i], answers[2][i]) == ('T', 'F') for i in range(Q))
    cn = sum((answers[1][i], answers[2][i]) == ('F', 'T') for i in range(Q))
    dn = sum((answers[1][i], answers[2][i]) == ('F', 'F') for i in range(Q))

    total_answer_keys = 0
    total_a = 0
    total_b = 0
    total_c = 0
    total_d = 0

    """
    """
    # consider number of times person 1 got each particular type of question correct
    for ak in range(an+1):
        for bk in range(bn+1):
            for ck in range(cn+1):
                dk = correct[0] - ak - bk - ck
                if dk < 0 or dk > dn:
                    continue
                # number of times person 2 is correct == ak + bk
                if ak + bk != correct[1]:
                    continue
                # number of times person 3 is correct == ak + ck
                if ak + ck != correct[2]:
                    continue
                eprint("asdf")
                # selection of correct answers for each type is consistent
                # count number of possible answer keys
                answer_keys = nCk(an, ak) * nCk(bn, bk) * nCk(cn, ck) * nCk(dn, dk)
                total_answer_keys += answer_keys
                # "agree with person 1 is correct" probability contribution to each question type * number of possible answer keys
                # to maintain exact results, divide by an,bn,cn,dn later
                total_a += ak * answer_keys
                total_b += bk * answer_keys
                total_c += ck * answer_keys
                total_d += dk * answer_keys
    """
    """
    for ak in range(an+1):
        bk = (correct[0]+correct[1]-dn-cn)//2-ak
        ck = (correct[2]+correct[0]-bn-dn)//2-ak
        dk = (correct[1]+correct[2]-cn-bn)//2-ak
        if not (0 <= bk <= bn and 0 <= ck <= cn and 0 <= dk <= dn):
            continue  # ak is invalid
        # selection of correct answers for each type is consistent
        # count number of possible answer keys
        answer_keys = nCk(an, ak) * nCk(bn, bk) * nCk(cn, ck) * nCk(dn, dk)
        total_answer_keys += answer_keys
        # "agree with person 1 is correct" probability contribution to each question type * number of possible answer keys
        # to maintain exact results, divide by an,bn,cn,dn later
        total_a += ak * answer_keys
        total_b += bk * answer_keys
        total_c += ck * answer_keys
        total_d += dk * answer_keys

    eprint(total_a, total_b, total_c, total_d)

    # "agree with person 1 is correct" probabilities
    prob_a = fractions.Fraction(total_a, (an * total_answer_keys)) if an * total_answer_keys > 0 else fractions.Fraction(1,2)
    prob_b = fractions.Fraction(total_b, (bn * total_answer_keys)) if bn * total_answer_keys > 0 else fractions.Fraction(1,2)
    prob_c = fractions.Fraction(total_c, (cn * total_answer_keys)) if cn * total_answer_keys > 0 else fractions.Fraction(1,2)
    prob_d = fractions.Fraction(total_d, (dn * total_answer_keys)) if dn * total_answer_keys > 0 else fractions.Fraction(1,2)

    eprint(prob_a, prob_b, prob_c, prob_d)

    strategy = {
        ('T', 'T'): prob_a >= 0.5,
        ('T', 'F'): prob_b >= 0.5,
        ('F', 'T'): prob_c >= 0.5,
        ('F', 'F'): prob_d >= 0.5,
    }
    strategy_ev = [max(prob_a, 1-prob_a), max(prob_b, 1-prob_b), max(prob_c, 1-prob_c), max(prob_d, 1-prob_d)]

    total_ev = an * strategy_ev[0] + bn * strategy_ev[1] + cn * strategy_ev[2] + dn * strategy_ev[3]

    res = []
    for i in range(Q):
        question_type = (answers[1][i], answers[2][i])
        choice = "FT"[strategy[question_type]]
        if i in flips:
            choice = flip(choice)
        res.append(choice)
    res = "".join(res)

    return f"{res} {total_ev.numerator}/{total_ev.denominator}"
    """

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N, Q = map(int, input().split())
    answers = []
    correct = []
    for _ in range(N):
        s = input().split()
        answers.append(s[0])
        correct.append(int(s[1]))
    res = solution(answers, correct)
    print("Case #{}: {}".format(case_num, res))
