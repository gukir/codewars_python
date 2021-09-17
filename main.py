import itertools


def solve_puzzle(clues):
    # Предполагается решать задачу рекурсивно
    # Рекурсивная функция будет возвращать застроенное поле или False
    fld = Field()

    def solve_puzzle_inner(field: Field, s_pos: int):
        nonlocal clues
        if s_pos > 15:
            return True
        if not field.check_rep():
            return False
        base_line = field.get_line(s_pos)
        possib = []
        for line in itertools.permutations(range(1, 5), 4):
            if check_cond(line, clues[s_pos]) and check_cross(line, base_line):
                possib.append(line)
        if not possib:
            return False
        else:
            for line in possib:
                changed_line = field.get_line(s_pos)
                field.build_line(line, s_pos)
                if solve_puzzle_inner(field, s_pos+1):
                    return True
                else:
                    field.build_line(changed_line, s_pos)
                    continue
        return False
    if solve_puzzle_inner(fld, 0):
        print(fld)
        return fld.data
    else:
        return False


class Field(object):
    """Field with skyscrapers"""

    def __init__(self):
        self.data = ((0, )*4, )*4

    def __str__(self):
        res = ''
        for arr in self.data:
            res += f"{arr}\n"
        return res

    def build_line(self, line, num):
        if 0 <= num <= 3:
            tmp_data = list(zip(*self.data))
            tmp_data[num % 4] = tuple(line)
            self.data = tuple(zip(*tmp_data))
        elif 4 <= num <= 7:
            tmp_data = list(self.data)
            tmp_data[num % 4] = tuple(reversed(line))
            self.data = tuple(tmp_data)
        elif 8 <= num <= 11:
            tmp_data = list(zip(*self.data))
            tmp_data[-(num % 4 + 1)] = tuple(reversed(line))
            self.data = tuple(zip(*tmp_data))
        elif 12 <= num <= 15:
            tmp_data = list(self.data)
            tmp_data[-(num % 4 + 1)] = tuple(line)
            self.data = tuple(tmp_data)
        else:
            print("Wrong number of line!")

    def get_line(self, num):
        if 0 <= num <= 3:
            tmp_data = list(zip(*self.data))
            return tmp_data[num % 4]
        elif 4 <= num <= 7:
            line = list(self.data[num % 4])
            return tuple(reversed(line))
        elif 8 <= num <= 11:
            tmp_data = list(zip(*self.data))
            return tuple(reversed(list(tmp_data[-(num % 4 + 1)])))
        elif 12 <= num <= 15:
            return self.data[-(num % 4 + 1)]
        else:
            print("Wrong number of line!")
            return 0

    def check_rep(self):
        for n_line in range(16):
            line = self.get_line(n_line)
            for height in range(1,5):
                if line.count(height) > 1:
                    return False
        return True


def check_cross(bld_arr, base_arr):
    for n_bld in range(len(bld_arr)):
        if bld_arr[n_bld] != base_arr[n_bld] and base_arr[n_bld] != 0:
            return False
    return True


def check_cond(array, count):
    base = 0
    vis_num = 0
    if not count:
        return True
    for elem in array:
        if elem > base:
            base = elem
            vis_num += 1
    return vis_num == count


s = solve_puzzle((2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3))

s = [1,2,3,4,5,5,6,2,3,1,3,1]
e = s.count(3)
print(3 == 3)
