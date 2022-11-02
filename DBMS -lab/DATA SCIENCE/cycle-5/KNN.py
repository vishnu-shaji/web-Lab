{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "387a6d5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy :  0.9777777777777777\n",
      "['setosa']\n"
     ]
    }
   ],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn import metrics\n",
    "\n",
    "iris = load_iris()\n",
    "x = iris.data\n",
    "y = iris.target\n",
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)\n",
    "c_knn = KNeighborsClassifier(n_neighbors=3)\n",
    "c_knn.fit(x_train,y_train)\n",
    "y_pred = c_knn.predict(x_test)\n",
    "print(\"Accuracy : \",metrics.accuracy_score(y_test,y_pred))\n",
    "sample = [[2,2,2,2]]\n",
    "pred = c_knn.predict(sample)\n",
    "pred_v = [iris.target_names[p] for p in pred]\n",
    "print(pred_v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13dd0635",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c5417e0",
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
