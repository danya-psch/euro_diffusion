import sys
import copy

class country:
    def __init__(self, name, xl, yl, xh, yh):
        self.name = name
        self.xl = int(xl) - 1
        self.yl = int(yl) - 1
        self.xh = int(xh)
        self.yh = int(yh)
        self.complete = 0
        self.scoordinates = []
        
    def add_sity(self, sity):
        self.scoordinates.append(sity_coordinates(sity.x, sity.y))
    
    def print(self):
        print(f"{self.name}: {self.complete}")
    

DEF_COINS_NUM = 1000000
DEF_COINS_DIV = 1000
class sity:
    def __init__(self, x, y, country_names: list, country_name=None):
        self.country_name = country_name
        self.coins = {}
        for cn in country_names:
            self.coins[cn] = DEF_COINS_NUM if cn == country_name else 0
        
        self.complete = 0    
        self.x = x
        self.y = y
    
    def is_euro_sity(self):
        return self.country_name is not None

class sity_coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class testcase_data:
    def __init__(self, num):
        self.num = num
        self.countries = []
        self.xl = sys.maxsize
        self.yl = sys.maxsize
        self.xh = 0
        self.yh = 0
        self.world = None
        self.iteration_count = 0
        self.complete = 0
        
    def add_coutry(self, c: country) -> bool:
        res = False
        append_allowed = True
        for cil in self.countries:
            if (cil.name == c.name) or \
               (cil.xl < c.xl <= cil.xh and \
                cil.yl < c.yl <= cil.yh) or \
               (cil.xl < c.xh <= cil.xh and \
                cil.yl < c.yh <= cil.yh):
                append_allowed = False
                break
                
        if append_allowed:
            if c.xl < self.xl:
                self.xl = c.xl
            if c.yl < self.yl:
                self.yl = c.yl
            if c.xh > self.xh:
                self.xh = c.xh
            if c.yh > self.yh:
                self.yh = c.yh
            self.countries.append(c)
            res = True
        return res

    def generate_world(self):
        country_names = [c.name for c in self.countries]
        self.world = [[sity(i, j, country_names) for i in range(self.yl, self.yh)] for j in range(self.xl, self.xh)]
        for c in self.countries:
            for i in range(c.xl, c.xh):
                for j in range(c.yl, c.yh):
                    s = sity(i, j, country_names, c.name)
                    self.world[i][j] = s
                    c.add_sity(s)
  
    def check_completion(self) -> bool:
        res = True
        if self.world is not None:
            tc_complete = True
            for c in self.countries:
                country_complete = True
                for sc in c.scoordinates:
                    s = self.world[sc.x][sc.y]
                    sity_complete = True
                    for _, val in s.coins.items():
                        if not val:
                            sity_complete = False
                            break
                        
                    if sity_complete:
                        s.complete = 1
                    if not s.complete and country_complete:
                        country_complete = False
                if country_complete:
                    if not c.complete:
                        c.complete = self.iteration_count
                elif tc_complete:
                    tc_complete = False
            if tc_complete:
                self.complete = self.iteration_count
            res = tc_complete
        return res

    def sity_iteration(self, s: sity, temp_world):
        x_more_then_xl = s.x > self.xl
        x_less_then_xh = s.x < self.xh - 1
        y_more_then_yl = s.y > self.yl
        y_less_then_yh = s.y < self.yh - 1
        for coin, value in s.coins.items():
            diff = int(value / DEF_COINS_DIV)
            if x_more_then_xl and self.world[s.x - 1][s.y].is_euro_sity():
                temp_world[s.x - 1][s.y].coins[coin] += diff
                temp_world[s.x][s.y].coins[coin] -= diff
            if x_less_then_xh and self.world[s.x + 1][s.y].is_euro_sity():
                temp_world[s.x + 1][s.y].coins[coin] += diff
                temp_world[s.x][s.y].coins[coin] -= diff
            if y_more_then_yl and self.world[s.x][s.y - 1].is_euro_sity():
                temp_world[s.x][s.y - 1].coins[coin] += diff
                temp_world[s.x][s.y].coins[coin] -= diff
            if y_less_then_yh and self.world[s.x][s.y + 1].is_euro_sity():
                temp_world[s.x][s.y + 1].coins[coin] += diff
                temp_world[s.x][s.y].coins[coin] -= diff
              
    def iteration(self):
        if self.world is not None:
            temp_world = copy.deepcopy(self.world)
            for c in self.countries:
                for sc in c.scoordinates:
                    self.sity_iteration(self.world[sc.x][sc.y], temp_world)
            self.world = temp_world
            self.iteration_count += 1
    
    def print_contries(self):
        print(f"Case number {self.num}")
        sorted_countries = sorted(sorted(self.countries, key=lambda x: x.name), key=lambda x: x.complete)
        for c in sorted_countries:
            c.print()
                            
                    
                        
                    
            
        