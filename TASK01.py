{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "54833f8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your first name\n",
      "vaibhav\n",
      "enter your last_name\n",
      "singh\n",
      "singh vaibhav\n"
     ]
    }
   ],
   "source": [
    "# write a program that accepts the users first and last name and prints them in reverse order with a space between them\n",
    "first_name,last_name=input(\"enter your first name\\n\"),input(\"enter your last_name\\n\")\n",
    "print(last_name+\" \"+first_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b02ce867",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value of your 'n' 5\n",
      "your result is:-155\n"
     ]
    }
   ],
   "source": [
    "# write a python program that accepts an integer (n)and computes the value of n+nn+nnn  \n",
    "number=int(input(\"enter the value of your 'n' \"))\n",
    "output=number+(number**2)+(number**3)\n",
    "print(\"your result is:-\"+str(output))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2529e58d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name**Is**James\n"
     ]
    }
   ],
   "source": [
    "# display three string \"name\",\"is,\"james\" as \"name**is**james\"\n",
    "first,second,third=\"Name\",\"Is\",\"James\"\n",
    "string=[first,second,third]\n",
    "result_string=\"**\".join(string)\n",
    "print(result_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "46de616a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the value of given number is: 4.66\n"
     ]
    }
   ],
   "source": [
    "#display float number with two decimal places using print()\n",
    "given_number=4.6550\n",
    "print(\"the value of given number is: {:.2f}\".format(given_number))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0aaecebe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter three strings separated by commas: vaibhav,kumar,singh\n",
      "first = vaibhav\n",
      "second = kumar\n",
      "third = singh\n"
     ]
    }
   ],
   "source": [
    "#accept any three string from one input call\n",
    "input_string = input(\"Enter three strings separated by commas: \")\n",
    "str1, str2, str3 = input_string.split(\",\")\n",
    "\n",
    "print(\"first =\", str1)\n",
    "print(\"second =\", str2)\n",
    "print(\"third =\", str3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10b6bab5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}