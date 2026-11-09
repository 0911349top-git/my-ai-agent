import numpy as np

ball = np.array([60, 40, 80, 90, 75, 69, 88, 100, 92, 100])

print(ball)
print(ball.shape)
print(ball.dtype)
print(np.mean(ball))
print(np.min(ball))
print(np.max(ball))
print(np.sum(ball))
print(ball[ball >= 60])
print(ball[ball < 60])
print(ball[:3])
print(ball[-1:-4:-1])

ball[1] = 79
b = ball + 5
print(np.mean(b))
