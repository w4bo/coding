import re
import unittest


def f(filename):
    with open(filename) as f:
        lines = [re.split(", y=|\\.\\.", x.strip()[15:]) for x in f.readlines()][0]  # read the lines
        min_x, max_x, min_y, max_y = int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3])

        def pass_by(v_x, v_y):
            cur_x, cur_y, h_max = 0, 0, 0
            while cur_x <= max_x and cur_y >= min_y:  # time is running
                cur_x += v_x  # update the x position
                cur_y += v_y  # update the y position
                h_max = max(h_max, cur_y)
                if min_x <= cur_x <= max_x and min_y <= cur_y <= max_y:
                    return (True, h_max)
                v_x = max(v_x - 1, 0)
                v_y -= 1
            return (False, h_max)

        x, y, h = 0, 0, 0
        direction = "b"
        while x <= max_x and y >= min_y:
            flag, h_max = pass_by(x, y)
            if flag:
                h = max(h_max, h)
            if direction == "a":
                y -= 1
                x += 1
                if y < 0:
                    y = 0
                    direction = "b"
            elif direction == "b":
                y += 1
                x -= 1
                if x < 0:
                    x = 0
                    direction = "a"

        # y_max = 0
        # v_x_opt = 0
        # v_y_opt = 0
        # for x in range(min_x, max_x + 1):
        #     for y in range(min_y, max_y + 1):
        #         for t in range(1, 1000):
        #             if y == -9 and t == 9 and x == 21:
        #                 print("Here")
        #             v1 = x / t + -1 * (t - 1)  # 0.5 *
        #             v2 = y / t - 1 * (t - 1)  # 0.5 *
        #             if v2 * v2 / 2 > y_max:
        #                 y_max = v2 * v2 / 2
        #                 v_x_opt = v1
        #                 v_y_opt = v2

        return h


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/17-test.txt'), 45)
        self.assertEqual(f('data/17-input.txt'), 2628)


if __name__ == "__main__":
    unittest.main()
