from context import testcase_data, country
from input import parse_coutry_input

# tcd.add_coutry(country("Netherlands", 0, 2, 2, 4))
# tcd.add_coutry(country("Belgium", 0, 0, 2, 2))

# tcd.add_coutry(country("Luxembourg", 0, 0, 1, 1))

# tcd.add_coutry(country("France", 0, 3, 4, 6))
# tcd.add_coutry(country("Spain", 2, 0, 6, 3))
# tcd.add_coutry(country("Portugal", 0, 0, 2, 2))
    
def ineration(i) -> bool:
    num = int(input())
    if num == 0:
        return False
        
    tcd = testcase_data(i)
    for _ in range(num):
        country = parse_coutry_input()
        if country is not None:
            tcd.add_coutry(country)
        else:
            raise Exception("Country is None")
        
    tcd.generate_world()
    while not tcd.check_completion():
        tcd.iteration()
    
    
    tcd.print_contries()
    return True


if __name__ == "__main__":
    try:
        i = 0
        while ineration(i):
            i += 1
    except Exception as e:
        print(e)