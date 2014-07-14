def parallel_dot(dview, A, B):
    dview.scatter('A', A)
    dview['B'] = B
    dview.execute('C = numpy.dot(A, B)')
    return dview.gather('C')

A = np.random.random((10, 3))
B = np.random.random((3, 5))

result1 = parallel_dot(dview, M1, M2)
result2 = np.dot(M1, M2)

print(np.allclose(result1, result2))
