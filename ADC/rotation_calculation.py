
def rotation_calc(input_1):
    #Suggestions generated by ChatGPT
    #Calculate de difference between two inputs for each element.
    result = tuple(b - a for a,b in zip(input_1[0],input_1[1]))
    return result


if __name__ == "__main__":
    input_1 = [(30,60,90),(0,10,15)]
    
    print(rotation_calc(input_1))
    
