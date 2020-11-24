from os import listdir, getcwd, stat, rename
from os.path import isfile, join, dirname
from time import localtime, strftime
onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
print(getcwd())
for f in onlyfiles:
    if f.startswith("Screenshot") and f.endswith(".png"):
        file_created = strftime("%d_%m_%Y__%H_%M_%S",
                            localtime(stat(f).st_ctime))
        rename(f,join(getcwd(), "Screenshot_"+file_created+".png"))
        print(f"{f} sucessfuly renamed")
                                