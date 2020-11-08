# A cool example of the us of recursion to solve any Hanoi problem
# note: n == number of disks, f == 'from'p position, h == 'helper' position, t == '
target' position


def move(f,t):
        print("Move disk from {} to {}!".format(f,t))

def moveVia(f,v,t):
        move(f,v)
        move(v,t)

def hanoi(n,f,h,t):
        if n==0:
                pass
        else:
                hanoi(n-1,f,t,h)
                move(f,t)
                hanoi(n-1,h,f,t)

hanoi(6,"A","B","C")
