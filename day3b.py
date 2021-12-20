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
    o2_list = input_array
    co2_list = input_array
    for i in reversed(range(digits)):
        if len(o2_list) == 1:
            break
        mask = 1 << i
        zeros = [number for number in o2_list if mask & number == 0]
        ones = [number for number in o2_list if mask & number == mask]
        o2_list = zeros if len(ones) < len(zeros) else ones
    for i in reversed(range(digits)):
        if len(co2_list) == 1:
            break
        mask = 1 << i
        zeros = [number for number in co2_list if mask & number == 0]
        ones = [number for number in co2_list if mask & number == mask]
        co2_list = ones if len(ones) < len(zeros) else zeros
    print(o2_list[0])
    print(co2_list[0])
    
        

if __name__ == "__main__":
    input_values, digits = ingest()
    main(input_values, digits)