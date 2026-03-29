
# MACHINE LEARNING
_
Linear Regression(Section)_

    Concept Overview of Linear Model

The model predicts a value using a straight line:

y = wx + b

w controls the slope

b shifts the line up or down

Objective:
The goal is to minimize prediction error.
Error is the difference between actual and predicted values:

error = y - y_hat

              Mean Squared Error

MSE measures how far predictions are from actual values:

Square each error and
take the average

Why square errors:

Removes negative values

Penalizes large mistakes more than small ones

Makes optimization smooth for gradient descent

