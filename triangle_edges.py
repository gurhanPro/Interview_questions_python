""" An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers,
returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

"""

def solution(a):
    a.sort()
    le = len(a)
    for i in range(0,le-2):
        p,q,r = i,i+1,i+2
        if a[p]+a[q]>a[r]:
            return 1
        
    return 0
