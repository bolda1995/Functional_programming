class Clock:
    t = 0
    def __init__(self, h= 0, m= 0, s = 0):
        self.h = h
        self.m = m
        self.s = s
        self.t = (h * 3600) + (m * 60) + s

    def __next__(self):
        h1 = str((self.t // 3600) % 24)
        m1 = str((self.t % 3600) // 60)
        s1 = str(self.t % 60)
        if len(h1) == 1:
            h1 = "0" + h1
        if len(m1) == 1:
            m1 = "0" + m1
        if len(s1) == 1:
            s1 = "0"+ s1
        self.t += 1
        return h1+":"+m1+":"+s1

    def __iter__(self):
        h = 0
        m = 0
        s = 0
        return self

def main():
    i = 5
    for time in Clock(10):
        print(time)
        i -= 1
        if i <= 0:
            break

if __name__ == "__main__":
    main()