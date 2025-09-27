# Deep Learning Coding Problems


**Problem-1 : Sigmoid Activation Function Understanding**
> Write a Python function that computes the output of the sigmoid activation function given an input value z. The function should return the output rounded to four decimal places.
>> Example : Input z = 0 and Output : 0.5 \
> Reasoning: The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)). For z = 0, exp(-0) = 1, hence the output is 1 / (1 + 1) = 0.5.

```python
import math

def sigmoid(z : float) -> float:
	# Your code here
	return result

```

**Problem-2 : Softmax Activation Function Implementation**
> Write a Python function that computes the softmax activation for a given list of scores. The function should return the softmax values as a list, each rounded to four decimal places.
>> Example : Input : scores = [1, 2, 3] and Output : [0.0900, 0.2447, 0.6652] \
>> Reasoning: The softmax function converts a list of values into a probability distribution. The probabilities are proportional to the exponential of each element divided by the sum of the exponentials of all elements in the list.

```python
import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	return probabilities
```
**Problem-3 : Implement SwiGLU activation function**
> Implement a Python function that applies the SwiGLU activation function to a NumPy array. Assume the input array has already been passed through a linear projection and has shape (batch_size, 2d). Round each output to four decimal places and return the result as a NumPy array of the shape (batch_size, d).
>> Example : Input : `np.array([[1, -1, 1000, -1000]])` and Output : `[[1000., 0.]]`. \
>> Reasoning: The input is of shape (1, 4), so it is split into x1 = [1, -1] and x2 = [1000, -1000]. The sigmoid of 1000 is approximately 1, and the sigmoid of -1000 is approximately 0 due to saturation. Thus, Swish(1000) ≈ 1000 x 1 = 1000 and Swish(-1000) ≈ -1000 x 0 = 0. Then, SwiGLU = x1 * Swish(x2) = [1 x 1000, -1 x 0] = [1000, 0].


**Problem-4 : **