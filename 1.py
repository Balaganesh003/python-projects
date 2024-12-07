def fun(arr, edges):
    a = arr  
    
    m = len(edges)
    
    adj_list = [[] for _ in range(len(a))]
    
    for edge in edges:
        tmpA, tmpB = edge
        adj_list[tmpA - 1].append(tmpB - 1)
        adj_list[tmpB - 1].append(tmpA - 1)
    
    assignment = [0] * len(a)
    
    final_ans = 0
    
    def backtrack(n):
        nonlocal final_ans
        
        for i in range(2):
            assignment[n] = i
            
            if n == len(a) - 1:
                # Check constraints when reaching the last node
                satisfied = True
                for j in range(len(a)):
                    if assignment[j] == 1:
                        for zz in adj_list[j]:
                            if assignment[zz] == 1:
                                satisfied = False
                                break
                        if not satisfied:
                            break
                
                # If constraints are satisfied, calculate sum
                if satisfied:
                    tmp = sum(a[j] for j in range(len(a)) if assignment[j] == 1)
                    final_ans = max(final_ans, tmp)
            else:
                # Recursive backtracking
                backtrack(n + 1)
            
            # Backtrack by resetting assignment
            assignment[n] = 0
    
    # Start backtracking from the first node
    backtrack(0)
    
    return final_ans

# Example of how to call the function
arr = list(map(int, input().split()))
E = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]
out_ = fun(arr, edges)
print(out_)
