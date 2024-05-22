x_values = [0.1,0.5,0.7]
weights = [0.3,0.2,0.9]
threshold = 0.5

def perceptron(x_values, weights, threshold):   
    weighted_sum = 0
    for x,w in zip(x_values, weights):
        weighted_sum += x*w
        print("Weighted sum: ", weighted_sum)

    if weighted_sum > threshold:
        return 1
    else:
        return 0

output = perceptron(x_values, weights, threshold)
print("Output: ", output)