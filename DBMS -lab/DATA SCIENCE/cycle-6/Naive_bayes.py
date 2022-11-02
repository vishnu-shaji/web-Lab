{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "942d7658",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 1 0 2 0 2 0 1 1 1 1 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0\n",
      " 1 1 1 2 0 2 0 0 1 2 2 1 2 1 2 1 1 2 1 1 2 1 2 1 0 2 1 1 1 1 2 0 0 2 1 0 0\n",
      " 1]\n",
      "predicted output for [[5,5,4,4]]: [2]\n",
      "Naive bayes score               : 0.9466666666666667\n"
     ]
    }
   ],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "\n",
    "X,y=load_iris(return_X_y=True)\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=0)\n",
    "gnb=GaussianNB()\n",
    "y_pred=gnb.fit(X_train,y_train).predict(X_test)\n",
    "print(y_pred)\n",
    "x_new=[[5,5,4,4]]\n",
    "y_new=gnb.fit(X_train,y_train).predict(x_new)\n",
    "print(\"predicted output for [[5,5,4,4]]:\",y_new)\n",
    "print(\"Naive bayes score               :\",gnb.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddd8c474",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
