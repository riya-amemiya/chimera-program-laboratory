import re

out = "#pragma once\n"
flag = 0
path = "./lib/include/rs.hpp"
with open(path) as f:
    for x in f:
        if re.search(r"#include", x) or flag:
            out += f"{x}"
        else:
            out += "namespace rs_to_py_lib {\n"
            flag = 1

out += "}"
with open(path, mode="w") as f:
    f.write(out)
print(out)
