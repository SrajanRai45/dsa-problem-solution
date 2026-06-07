def tOH(n:int, s:int, d:int, h:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n > 1:
        a=tOH(n-1,s,h,d)
        b=tOH(n-1,h,d,s)
        return a + b + 1:
