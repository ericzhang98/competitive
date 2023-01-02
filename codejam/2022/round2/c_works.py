def back(arr,ind,taken,s_taken):
    global ans
    if ind==n:
        ans=[]
        for i in range(n):
            ans.append((arr[i]+1,s_taken[i]+1))
        return True
    for i in range(n):
        if i not in taken:
            for j in childToSweet[i]:
                if j in s_taken:
                    continue
                if not j:
                    return False
                if back(arr+[i],ind+1,taken.union({i}),s_taken+[j]):
                    return True
                break
    return False
 
 
 
t=int(input())
for _ in range(t):
    print("Case #{}:".format(_+1),end=" ")
    n=int(input())
    children=[]
    for i in range(n):
        x,y=map(int,input().split())
        children.append((x,y))
    sweets=[]
    for i in range(n+1):
        x, y = map(int, input().split())
        sweets.append((x, y))
    childToSweet=[[i for i in range(n+1)] for j in range(n)]
    for i in range(n):
        childToSweet[i].sort(key=lambda x:((children[i][0]-sweets[x][0])**2+(children[i][1]-sweets[x][1])**2,-x))
    ans=None
    back([],0,set(),[])
    if not ans:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        for i,j in ans:
            print(str(i)+" "+str(j))