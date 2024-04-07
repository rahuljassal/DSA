arrival_arr = [120,50,550,200,700,850]
depart_arr = [600,550,700,500,900,1000]
def min_station(start_arr,end_arr,n):
    start_arr.sort()
    end_arr.sort()
    platform = 1
    maxx = 1
    i = 1
    j = 0
    while(i<n and j<n):
        if start_arr[i]<=end_arr[j]:
            platform+=1
            i+=1
        elif start_arr[i]>end_arr[j]:
            platform-=1
            j+=1
        if platform>maxx:
            maxx = platform
    print(maxx)
    return maxx
def loop_soln(arr,dep,n):
    plat = 1
    result = 1
    for i in range(n):
        plat = 1
        for j in range(n):
           
            if i !=j :
                if arr[i]>=arr[j] and dep[j]>=arr[i]:
                    plat+=1
        result = max(plat,result)
    print(result)
    
    return result


min_station(arrival_arr,depart_arr,len(arrival_arr))
loop_soln(arrival_arr,depart_arr,len(arrival_arr))
