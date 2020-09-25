# Numba GPU Timer
A helper package to easily time Numba CUDA GPU events.

## Compatibility 
As this package uses Numba, refer to the [Numba compatibility guide](https://numba.pydata.org/numba-doc/dev/user/installing.html#compatibility).

## Installation
Using Pip: `pip3 install numba_timer`.

## Example
```
import math
import numpy as np
from numba import cuda
from numba_timer import cuda_timer

@cuda.jit
def increment_a_2D_array(an_array):
    x, y = cuda.grid(2)
    if x < an_array.shape[0] and y < an_array.shape[1]:
       an_array[x, y] += 1

an_array = np.zeros((2, 100))
threadsperblock = (16, 16)
blockspergrid_x = math.ceil(an_array.shape[0] / threadsperblock[0])
blockspergrid_y = math.ceil(an_array.shape[1] / threadsperblock[1])
blockspergrid = (blockspergrid_x, blockspergrid_y)

timer = cuda_timer.Timer()

timer.start()
increment_a_2D_array[blockspergrid, threadsperblock](an_array)
timer.stop()

print(f'Elapsed time for run 1: {timer.elapsed()} ms')

timer.start()
increment_a_2D_array[blockspergrid, threadsperblock](an_array)
timer.stop()

print(f'Elapsed time for run 2: {timer.elapsed()} ms')
```
Numba specific code is borrowed from the [Numba documentation](https://numba.pydata.org/numba-doc/latest/cuda/kernels.html).