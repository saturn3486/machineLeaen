# -*- encoding:utf-8 -*-
import numpy as np
import timeit

nomal_py_sec = timeit.timeit('sum(x*x for x in range(1000))',number=10000)
naive_np_sec = timeit.timeit('sum(na*na)',setup="import numpy as np; na=np.arange(1000)",number=10000)
good_np_sec = timeit.timeit('na.dot(na)',setup="import numpy as np; na=np.arange(1000)",number=10000)

print("nomal python : %f sec"%nomal_py_sec)
print("naive pynum : %f sec"%naive_np_sec)
print("good pynum : %f sec"%good_np_sec)