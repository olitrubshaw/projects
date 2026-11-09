import numpy as np
import matplotlib.pyplot as plt

def monte_carlo(mu, sigma, no_days):
    P = np.zeros(no_days)
    P[0] = 1250.0
    
    # Generate random numbers
    Z = np.random.normal(mu, sigma, no_days)
    
    # Convert random numbers to returns
    R = Z + 1
    
    # Use a For loop to fill in prices
    for i in range(1, no_days):
        P[i] = P[i-1] * R[i-1]
        
    #returns price path
    return P
fig, ax = plt.subplots()

# Prepare a 1000-day simulation
no_days = 1000
x = np.linspace(0, (no_days - 1), no_days)
np.random.seed(56789)

### company 1
mu = 0.00025
sigma = 0.0025
y = monte_carlo(mu, sigma, no_days)
ax.plot(x, y, 'b', linewidth=2, label='Company 1 Price Path')

### company 2
mu = 0.00040
sigma = 0.0040
y = monte_carlo(mu, sigma, no_days)
ax.plot(x, y, 'r', linewidth=2, label='Company 2 Price Path')

### company 3
mu = 0.00065
sigma = 0.0065
y = monte_carlo(mu, sigma, no_days)
ax.plot(x, y, 'g', linewidth=2, label='Company 3 Price Path')

ax.legend(loc='upper left')
ax.set_title('Simulated Price Paths')
ax.set_xlabel('Days')
ax.set_ylabel('Price')
fig.savefig("simulated price paths.jpg")