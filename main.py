from context import testcase_data, country
    
def ineration(i) -> bool:
    num = int(input())
    if num == 0:
        return False
        
    tcd = testcase_data(i)
    for _ in range(num):
        tcd.add_coutry(country(*input().split()))
        
    tcd.generate_world()
    while not tcd.check_completion():
        tcd.iteration()
    
    tcd.show_contries()
    return True


if __name__ == "__main__":
    try:
        i = 0
        while ineration(i):
            i += 1
    except Exception as e:
        print(e)