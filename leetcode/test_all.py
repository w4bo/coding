import unittest
import os
from importlib import import_module
import time
import pandas as pd

class Test(unittest.TestCase):
    def test(self):
        res = []
        for folder in [f.path for f in os.scandir(".") if f.is_dir() and "venv" not in f.path]: # iterate over all the sub-folders (i.e., coding problems)
            folder = folder.replace("\\", "").replace("/", "").replace(".", "")
            print(folder)
            module = import_module(folder + ".test") # import the unit_test function
            print(module)
            unit_test = module.unit_test
            print(unit_test)
            for filename in os.listdir(folder): # iterate over all solutions of each coding problem
                if filename.endswith(".py") and filename != "test.py": 
                    module = import_module(folder + "." + filename.replace(".py", "")) # import the function to be tested
                    test_function = module.test_function
                    trials = 10 
                    start = time.time()
                    for i in range(trials): # execute the function `trials` times to get the average result
                        unit_test(self, test_function)
                    res.append([folder, filename, (time.time() - start) / trials]) # store the result
        df = pd.DataFrame(res, columns=["problem", "solution", "time"])
        df.to_csv("results.csv", index=False)
        print(df)

if __name__ == "__main__":
    unittest.main()
