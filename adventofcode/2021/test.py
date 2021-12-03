# import glob
# import os

# files = [x for x in glob.glob('./**/*.py', recursive=True) if "test.py" not in x]
# for f in files:
#     print(f)
#     f = f.replace("\\", "/").split("/")
#     d = '/'.join(f[:-1])
#     f = f[-1]
#     os.chdir(d)
#     exec(open(f).read())