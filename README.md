## MACHINE LEARNING

#### Linear Regression Section

Linear Regression predicts a continuous value using a straight line model. The equation is:
y = mX + b
m controls the slope. b shifts the line up or down.

The goal is to reduce prediction error. 

Error is the difference between the actual value and the predicted value:

error = y - y_hat (different between predicted(line) and actual value point)

#####  Mean Squared Error

measures how far predictions are from actual values. 
It squares each error to remove negative values, penalize large mistakes, and support smooth optimization.

##### Gradient Descent vs Closed Form
Gradient Descent updates model parameters step by step and works well on large datasets. Closed form computes the exact solution directly and fits small datasets better but does not scale well.
