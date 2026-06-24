import math
#need to take
def log2_by_case(case_name: str, TotalCapacity: float, TotalDieDensity: float) -> float:
    match case_name.upper():
        #if we choose module type CAMM2
        case "CAMM2":
            x=TotalCapacity*8/(TotalDieDensity*4)
            sum=int(math.log2(x))
            return sum
        #if we choose module type COMPONENT
        case "COMPONENT":
            x=TotalCapacity*8/(TotalDieDensity*1)
            sum=int(math.log2(x))
            return sum
        case _:
            raise ValueError(
                f"Error"
            )

#Calculate the DDP, QDP, ODP based on the sum value
def ddp(sum: int) -> str:
    match int(sum):
        case val if val < 1:
            return "DDP"
        case 1:
            return "DDP"
        case 2:
            return "QDP"
        case 3:
            return "ODP"
        #for now 4 is ODP until we get something with HDP
        case 4:
            return "ODP"
        case _:
            return "sum is out of range (1-4)"


def main() -> None:
    sum_value = log2_by_case("COMPONENT", 4, 32)
    print(sum_value)
    print(ddp(sum_value))


if __name__ == "__main__":
    main()
