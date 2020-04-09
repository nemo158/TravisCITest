import numpy as np
import multiple as mul

first=np.random.randint(1,100,size=(3,3))
second=np.random.randint(1,100,size=(3,3))
back=mul.multiply_print(first,second)
if (back==np.multiply(first,second)).all():
    print("这俩一样的，验证OK")
else:
    print("不咋地~")