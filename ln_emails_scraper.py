{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Finding rents for maximum-value matching {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}:\n",
      "status:  optimal\n",
      "optimal value:  0.0\n",
      "rents: heder=43.333333333333336, martef=23.333333333333336, salon=33.33333333333332\n",
      "\n",
      "Finding rents for another matching {('salon', 'batya'), ('heder', 'aya'), ('martef', 'gila')}\n",
      "status:  infeasible\n",
      "optimal value:  inf\n",
      "rents: heder=None, martef=None, salon=None\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\"\"\"\n",
    "Using cvxpy to find \"rental harmony\" - an envy-free rent division.\n",
    "AUTHOR: Erel Segal-Halevi\n",
    "SINCE:  2019-11\n",
    "\"\"\"\n",
    "\n",
    "import cvxpy\n",
    "\n",
    "\n",
    "print(\"\\nFinding rents for maximum-value matching {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}:\")\n",
    "\n",
    "price_martef, price_heder, price_salon = cvxpy.Variable(), cvxpy.Variable(), cvxpy.Variable()\n",
    "prob = cvxpy.Problem(\n",
    "    cvxpy.Minimize(0),\n",
    "    # cvxpy.Maximize(price_martef+price_heder+price_salon),\n",
    "    constraints = [price_martef + price_heder + price_salon == 100,\n",
    "                   # price_martef >= 0, price_heder >= 0, price_salon >= 0,\n",
    "            35 - price_salon >= 40 - price_heder,\n",
    "            35 - price_salon >= 25 - price_martef,  # aya\n",
    "\n",
    "            60 - price_heder >= 35 - price_salon,\n",
    "            60 - price_heder >= 40 - price_martef,  # batya\n",
    "\n",
    "            20 - price_martef >= 40 - price_heder,\n",
    "            20 - price_martef >= 25 - price_salon,  # gila\n",
    "    ]\n",
    ")\n",
    "prob.solve()\n",
    "print(\"status: \", prob.status)\n",
    "print(\"optimal value: \", prob.value)\n",
    "print(\"rents: heder={}, martef={}, salon={}\".format(price_heder.value, price_martef.value, price_salon.value))\n",
    "\n",
    "print(\"\\nFinding rents for another matching {('salon', 'batya'), ('heder', 'aya'), ('martef', 'gila')}\")\n",
    "price_martef, price_heder, price_salon = cvxpy.Variable(), cvxpy.Variable(), cvxpy.Variable()\n",
    "prob = cvxpy.Problem(\n",
    "    cvxpy.Minimize(0),\n",
    "    constraints = [price_martef + price_heder + price_salon == 100,\n",
    "            40 - price_heder >= 35 - price_salon, 40 - price_heder >= 25 - price_martef,  # aya\n",
    "            35 - price_salon >= 60 - price_heder, 35 - price_salon >= 40 - price_martef,  # batya\n",
    "            20 - price_martef >= 40 - price_heder, 20 - price_martef >= 25 - price_salon,  # gila\n",
    "                   ]\n",
    ")\n",
    "prob.solve()\n",
    "print(\"status: \", prob.status)\n",
    "print(\"optimal value: \", prob.value)\n",
    "print(\"rents: heder={}, martef={}, salon={}\".format(price_heder.value, price_martef.value, price_salon.value))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.5rc1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
