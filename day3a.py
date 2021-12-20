def ingest() -> list[int]: 
    output = []
    digits = -1
    while True:
        number = input()
        if not number:
            break
        if digits < 0:
            digits = len(number)
        output.append(int(number, 2))
    return output, digits

def main(input_array:list[int], digits:int):
    gamma_str = ''
    epsilon_str = ''
    length = len(input_array)
    for i in reversed(range(digits)):
        mask = 1 << i
        count = sum(mask & number == 0 for number in input_array)
        gamma_str += '0' if count > length/2 else '1'
        epsilon_str += '1' if count > length/2 else '0'
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)
    print(gamma)
    print(epsilon)
    
        

if __name__ == "__main__":
    input_values, digits = ingest()
    main(input_values, digits)