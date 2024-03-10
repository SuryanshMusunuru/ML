import numpy as np 
import matplotlib.pyplot as plt
# y_cap = m x + b 
# mse = cost = (y - y_cap)**2 / n
# n = number of points 
# d/dm(mse) = - (2/n) * (x*((y - y_cap))) 
# d/db(mse) = - (2/n) * ((y - y_cap))
def gradient_descent(x,y):
    m = b = 0  
    n = len(x)
    learning_rate=0.01
    iterations = 10000
    md=0 
    bd=0 
    cost=[]
    mchange=[]
    for i in range(iterations):
        y_cap = m * x + b
        mse = (1/n)*sum([val**2 for val in (y-y_cap)]) #(y - m * x + b )**2 / n
        md = -(2/n)*sum(x*(y-y_cap))# - (2/n) * (x*((y - m * x + b )))
        bd = -(2/n)*sum(y-y_cap)# - (2/n) * ((y - (m * x + b )))
        m_curr = m - learning_rate * md# m - learning_rate * - (2/n) * (x*((y - m * x + b )))
        b_curr = b - learning_rate * bd #b - learning_rate * - (2/n) * ((y - (m * x + b )))
        m=m_curr
        b=b_curr
        cost.append(mse)
        mchange.append(m)
        if i%1000==0:
            print("i: {}, cost: {} , m: {}, b: {}".format(i,mse,m_curr,b_curr)) 
    return m,b, cost, mchange

def plot_regression_line(x,y,m,b):#Function to show the line of best fit along with data points 
    plt.scatter(x,y, color='green', marker='o', label='Data points')
    plt.plot(x, m*x +b, color='brown' ,label='Regression line' )
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Linear regression using Gradient Descent')
    plt.show()
    
def plot_gradient_descent(cost,mchange):#Function to display how the cost change with respect to m
    plt.plot(mchange,cost, color='purple') 
    plt.xlabel('M=Slope')
    plt.ylabel('Cost(MSE)') 
    plt.title('Gradient descent by reducing the cost')
    plt.show()  

def plot_cost_over_i(cost):#Function to display how the cost change with respect to iterations
    plt.plot(range(len(mchange)),cost, color='maroon') 
    plt.xlabel('Iterations')
    plt.ylabel('Cost(MSE)') 
    plt.title('Gradient descent by reducing the cost')
    plt.show()  

x = np.array([1,2,3])
y = np.array([1,2,3])

m,b, cost, mchange = gradient_descent(x,y) 

plot_regression_line(x,y,m,b)
plot_gradient_descent(cost,mchange)
plot_cost_over_i(cost)