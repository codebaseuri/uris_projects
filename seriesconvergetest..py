
#made by uri kestenbaum
#1/n seires converge proof
# this program proves that the sum qeometric when a1 is 1 series of 1/n ,n=>2 converges to 1/(n-1).
#examples 1/2 + 1/4 +1/8.. converges to 1
# 1/3 +1/9+ 1/27..... converges to 0.5


converge_series=[]
for i in range(2,100):
    converge_series.append(1/i)
#print(converge_series)

for j in converge_series:
    base=j
    #print(base)
    ssum=0
    for i in range (1,1000):
        ssum+=pow(base,i)
    #print(ssum)
    print(f"{ssum} and it should converge to ->{1/(converge_series.index(j)+1)}")
    print("________________________________")