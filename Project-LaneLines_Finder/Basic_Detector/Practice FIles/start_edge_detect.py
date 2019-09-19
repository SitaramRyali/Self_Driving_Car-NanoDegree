
def start_edge(start_arr):
    st,sp =(100,0)
    dist = len(start_arr)
    for i in range(dist):
        if (start_arr[i] == 255) and (i <150):            
            st = i
            break
    for i in range(dist):
        if start_arr[-1-i] == 255:
            sp = -1-i
            break
    sp = dist +sp
    
    return (st,sp)

        
        
    
        