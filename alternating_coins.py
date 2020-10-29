def solution(A):
    
    if len(A) == 1 or len(A) == 0:
        return 0
    else:
        flipped_stack = [A[0]]
    
    num_heads = sum(A)
    num_tails = len(A) - num_heads
    
    stack_heads = sum(flipped_stack)
    stack_tails = len(flipped_stack) - stack_heads
    
    coins_to_flip = 0
    
    for i in range(1, len(A)):
        #print(f'i: {i}, A[i]: {A[i]}, flipped_stack: {flipped_stack}')
        if flipped_stack[-1] ^ A[i] == 0:
            if flipped_stack[-1] == 1:
                flipped_stack.append(0)
            elif flipped_stack[-1] == 0:
                flipped_stack.append(1)
        elif flipped_stack[-1] ^ A[i] == 1:
            if flipped_stack[-1] == 1:
                flipped_stack.append(0)
            elif flipped_stack[-1] == 0:
                flipped_stack.append(1)
    
    print(A)            
    print(flipped_stack)
    
    for c in range(len(A)):
        if A[c] != flipped_stack[c]:
            coins_to_flip += 1
        else:
            continue
    return coins_to_flip