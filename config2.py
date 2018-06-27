import os
class load(object):
    def __init__(self, file="./data"):
        self.file = file
        if os.path.exists(file) is False:
            os.system("touch "+file)
            with open(file, "w") as version:
                version.write("version:1.0")
    def add(self, key, value):
        with open(self.file, "a") as add:
            add.write("{}:{}\n".format(key, value))
    def set(self, key, value):
        dict, newdata = [], ""
        data_read = open(self.file)
        data_read = data_read.read().splitlines()
        for j in data_read:
            dict.append(j.split(":")[0])
        if key not in dict:
            self.add(key, value)
        else:
            for j in data_read:
                if j.split(":")[0] != key:
                    newdata = newdata + "{}:{}\n".format(j.split(":")[0], j.split(":")[1])
                else:
                    newdata = newdata + "{}:{}\n".format(key, value)
            with open(self.file, "w") as set:
                set.write(newdata)
    def get(self, key):
        data = open(self.file)
        for r in data:
            if (r.split(":")[0] == key):
                output = r.split(":")[1].strip("\n")
        return output
            
