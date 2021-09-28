import numpy as np
def C(u :float, P: list):
    Q = np.array(P)
    for j in range(1, len(Q), 1):
        print("Iteração ", j)
        for k in range(len(Q)-j):
            Q[k] = (1.-u)*Q[k]+u*Q[k+1]
            print("Q[", k, "] = ", Q[k])
        print("-------------\n")
def main():
    u = 0.6
    P= [[-1,0], [-0.5,0.5],[0.5,-0.5], [1,0]]
    C(u, P)
    
if __name__ == "__main__":
    main()