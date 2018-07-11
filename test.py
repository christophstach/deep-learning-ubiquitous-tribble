import numpy as np

slice = np.array([
    [1, 1],
    [1, 1]
])

kernel = np.array([
    [0.1, 0.5],
    [0.5, 0.2]
])

rgb_kernel = np.repeat(kernel[:, :, np.newaxis], 3, axis=2)
rgb_slice = np.ones((2, 2, 3))


def conv(matrix, kernel):
    # print(kernel.shape)
    # print(kernel.reshape((3, 2, 2))[0])

    result = np.dot(matrix, kernel )
    return result


print(conv(slice, kernel))
print('#################################')
#print(conv(rgb_slice, kernel))
