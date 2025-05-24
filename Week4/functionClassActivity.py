{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c66ac7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "class fileReader:\n",
    "    def _init_(self,filepath):\n",
    "        self.filepath = filepath\n",
    "        \n",
    "    def readTXT(self,delimeter=','):\n",
    "        df = pd.read_csv(self.filepath, delimiter)\n",
    "\n",
    "    def readCSV(self):\n",
    "        df = pd.read_csv(self.filepath)\n",
    "\n",
    "    \n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
