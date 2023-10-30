{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "541c4f5a",
   "metadata": {},
   "source": [
    "# Mobile Price Analysis\n",
    "\n",
    "### Table of Contents:\n",
    "1. Introduction\n",
    "2. Data\n",
    "3. Exploratory Data Analysis (EDA)\n",
    "4. Feature Engineering\n",
    "5. Training and Evaluating Models\n",
    "    1. Dimensional Reduction (PCA)\n",
    "6. Conclusion\n",
    "\n",
    "## 1. Introduction\n",
    "\n",
    "This project is based on the Mobile prices dataset taken from Kaggle, this dataset contains several factors among which we find the brand, size, weight, image quality, RAM, battery, etc. that interfere in the sales price of a Mobile.  With this data set, I want to estimate a price range that indicates how high the price is in relation to the mentioned features. For these we will apply the logistic regression and KNeighbors Classifier models.\n",
    "\n",
    "## 2. Data \n",
    "\n",
    "This dataset contains all the information related to different characteristics that interfere with the prices of a Mobile, such as:\n",
    "\n",
    "- **battery_power:** Total energy a battery can store in one time measured in mAh\n",
    "- **blue:** Has bluetooth or not\n",
    "- **clock_speed:** speed at which microprocessor executes instructions\n",
    "- **dual_sim:** Has dual sim support or not\n",
    "- **fc:** Front Camera mega pixels\n",
    "- **four_g:** Has 4G or not\n",
    "- **int_memory:** Internal Memory in Gigabytes\n",
    "- **m_dep:** Mobile Depth in cm\n",
    "- **mobile_wt:** Weight of mobile phone\n",
    "- **n_cores:** Number of cores of processor\n",
    "- **pc:** Primary Camera mega pixels\n",
    "- **px_height:** Pixel Resolution Height\n",
    "- **px_width:** Pixel Resolution Width\n",
    "- **ram:** Random Access Memory in Mega Bytes\n",
    "- **sc_h:** Screen Height of mobile in cm\n",
    "- **sc_w:** Screen Width of mobile in cm\n",
    "- **talk_time:** longest time that a single battery charge will last when you are\n",
    "- **three_g:** Has 3G or not\n",
    "- **touch_screen:** Has touch screen or not\n",
    "- **wifi:** Has wifi or not\n",
    "- **price_range:** This is the target variable with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ddf5b0d",
   "metadata": {},
   "source": [
    "**First I am going to import all the libraries that I will use in the project and open the dataset:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "06858c17",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.metrics import classification_report\n",
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.decomposition import PCA\n",
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f2c659b",
   "metadata": {},
   "source": [
    "# 3. Exploratory Data Analysis (EDA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "d35a612a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>842</td>\n",
       "      <td>0</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>0.6</td>\n",
       "      <td>188</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>20</td>\n",
       "      <td>756</td>\n",
       "      <td>2549</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1021</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>53</td>\n",
       "      <td>0.7</td>\n",
       "      <td>136</td>\n",
       "      <td>3</td>\n",
       "      <td>...</td>\n",
       "      <td>905</td>\n",
       "      <td>1988</td>\n",
       "      <td>2631</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>563</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>41</td>\n",
       "      <td>0.9</td>\n",
       "      <td>145</td>\n",
       "      <td>5</td>\n",
       "      <td>...</td>\n",
       "      <td>1263</td>\n",
       "      <td>1716</td>\n",
       "      <td>2603</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>615</td>\n",
       "      <td>1</td>\n",
       "      <td>2.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>0.8</td>\n",
       "      <td>131</td>\n",
       "      <td>6</td>\n",
       "      <td>...</td>\n",
       "      <td>1216</td>\n",
       "      <td>1786</td>\n",
       "      <td>2769</td>\n",
       "      <td>16</td>\n",
       "      <td>8</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1821</td>\n",
       "      <td>1</td>\n",
       "      <td>1.2</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>44</td>\n",
       "      <td>0.6</td>\n",
       "      <td>141</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>1208</td>\n",
       "      <td>1212</td>\n",
       "      <td>1411</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  m_dep  \\\n",
       "0            842     0          2.2         0   1       0           7    0.6   \n",
       "1           1021     1          0.5         1   0       1          53    0.7   \n",
       "2            563     1          0.5         1   2       1          41    0.9   \n",
       "3            615     1          2.5         0   0       0          10    0.8   \n",
       "4           1821     1          1.2         0  13       1          44    0.6   \n",
       "\n",
       "   mobile_wt  n_cores  ...  px_height  px_width   ram  sc_h  sc_w  talk_time  \\\n",
       "0        188        2  ...         20       756  2549     9     7         19   \n",
       "1        136        3  ...        905      1988  2631    17     3          7   \n",
       "2        145        5  ...       1263      1716  2603    11     2          9   \n",
       "3        131        6  ...       1216      1786  2769    16     8         11   \n",
       "4        141        2  ...       1208      1212  1411     8     2         15   \n",
       "\n",
       "   three_g  touch_screen  wifi  price_range  \n",
       "0        0             0     1            1  \n",
       "1        1             1     0            2  \n",
       "2        1             1     0            2  \n",
       "3        1             0     0            2  \n",
       "4        1             1     0            1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=pd.read_csv('mobile_prices.csv')\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "55843cd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The dataset has 2000 instances (rows) and 21 features (columns).\n"
     ]
    }
   ],
   "source": [
    "data.shape\n",
    "print('The dataset has {} instances (rows) and {} features (columns).'.format(data.shape[0],data.shape[1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22b6f343",
   "metadata": {},
   "source": [
    "**With the following code I want to identify if the dataset has null values. In addition, I want to identify the data types that the dataset has:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "ac7333d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2000 entries, 0 to 1999\n",
      "Data columns (total 21 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   battery_power  2000 non-null   int64  \n",
      " 1   blue           2000 non-null   int64  \n",
      " 2   clock_speed    2000 non-null   float64\n",
      " 3   dual_sim       2000 non-null   int64  \n",
      " 4   fc             2000 non-null   int64  \n",
      " 5   four_g         2000 non-null   int64  \n",
      " 6   int_memory     2000 non-null   int64  \n",
      " 7   m_dep          2000 non-null   float64\n",
      " 8   mobile_wt      2000 non-null   int64  \n",
      " 9   n_cores        2000 non-null   int64  \n",
      " 10  pc             2000 non-null   int64  \n",
      " 11  px_height      2000 non-null   int64  \n",
      " 12  px_width       2000 non-null   int64  \n",
      " 13  ram            2000 non-null   int64  \n",
      " 14  sc_h           2000 non-null   int64  \n",
      " 15  sc_w           2000 non-null   int64  \n",
      " 16  talk_time      2000 non-null   int64  \n",
      " 17  three_g        2000 non-null   int64  \n",
      " 18  touch_screen   2000 non-null   int64  \n",
      " 19  wifi           2000 non-null   int64  \n",
      " 20  price_range    2000 non-null   int64  \n",
      "dtypes: float64(2), int64(19)\n",
      "memory usage: 328.2 KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3aeef73f",
   "metadata": {},
   "source": [
    "**The dataset has no null values, so I don't need to do the imputation. Also, the dataset has 19 integer data and 2 float data. Since we do not have categorical data, it is not necessary to encode our variables.**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d52c7025",
   "metadata": {},
   "source": [
    "**With the following code I want to see the main statistical data of the dataset:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "6b04dda6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.0000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>2000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1238.518500</td>\n",
       "      <td>0.4950</td>\n",
       "      <td>1.522250</td>\n",
       "      <td>0.509500</td>\n",
       "      <td>4.309500</td>\n",
       "      <td>0.521500</td>\n",
       "      <td>32.046500</td>\n",
       "      <td>0.501750</td>\n",
       "      <td>140.249000</td>\n",
       "      <td>4.520500</td>\n",
       "      <td>...</td>\n",
       "      <td>645.108000</td>\n",
       "      <td>1251.515500</td>\n",
       "      <td>2124.213000</td>\n",
       "      <td>12.306500</td>\n",
       "      <td>5.767000</td>\n",
       "      <td>11.011000</td>\n",
       "      <td>0.761500</td>\n",
       "      <td>0.503000</td>\n",
       "      <td>0.507000</td>\n",
       "      <td>1.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>439.418206</td>\n",
       "      <td>0.5001</td>\n",
       "      <td>0.816004</td>\n",
       "      <td>0.500035</td>\n",
       "      <td>4.341444</td>\n",
       "      <td>0.499662</td>\n",
       "      <td>18.145715</td>\n",
       "      <td>0.288416</td>\n",
       "      <td>35.399655</td>\n",
       "      <td>2.287837</td>\n",
       "      <td>...</td>\n",
       "      <td>443.780811</td>\n",
       "      <td>432.199447</td>\n",
       "      <td>1084.732044</td>\n",
       "      <td>4.213245</td>\n",
       "      <td>4.356398</td>\n",
       "      <td>5.463955</td>\n",
       "      <td>0.426273</td>\n",
       "      <td>0.500116</td>\n",
       "      <td>0.500076</td>\n",
       "      <td>1.118314</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>501.000000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.100000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>256.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>851.750000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>0.700000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>0.200000</td>\n",
       "      <td>109.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>282.750000</td>\n",
       "      <td>874.750000</td>\n",
       "      <td>1207.500000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1226.000000</td>\n",
       "      <td>0.0000</td>\n",
       "      <td>1.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>564.000000</td>\n",
       "      <td>1247.000000</td>\n",
       "      <td>2146.500000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1615.250000</td>\n",
       "      <td>1.0000</td>\n",
       "      <td>2.200000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>170.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>947.250000</td>\n",
       "      <td>1633.000000</td>\n",
       "      <td>3064.500000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.250000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1998.000000</td>\n",
       "      <td>1.0000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>64.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>1960.000000</td>\n",
       "      <td>1998.000000</td>\n",
       "      <td>3998.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       battery_power       blue  clock_speed     dual_sim           fc  \\\n",
       "count    2000.000000  2000.0000  2000.000000  2000.000000  2000.000000   \n",
       "mean     1238.518500     0.4950     1.522250     0.509500     4.309500   \n",
       "std       439.418206     0.5001     0.816004     0.500035     4.341444   \n",
       "min       501.000000     0.0000     0.500000     0.000000     0.000000   \n",
       "25%       851.750000     0.0000     0.700000     0.000000     1.000000   \n",
       "50%      1226.000000     0.0000     1.500000     1.000000     3.000000   \n",
       "75%      1615.250000     1.0000     2.200000     1.000000     7.000000   \n",
       "max      1998.000000     1.0000     3.000000     1.000000    19.000000   \n",
       "\n",
       "            four_g   int_memory        m_dep    mobile_wt      n_cores  ...  \\\n",
       "count  2000.000000  2000.000000  2000.000000  2000.000000  2000.000000  ...   \n",
       "mean      0.521500    32.046500     0.501750   140.249000     4.520500  ...   \n",
       "std       0.499662    18.145715     0.288416    35.399655     2.287837  ...   \n",
       "min       0.000000     2.000000     0.100000    80.000000     1.000000  ...   \n",
       "25%       0.000000    16.000000     0.200000   109.000000     3.000000  ...   \n",
       "50%       1.000000    32.000000     0.500000   141.000000     4.000000  ...   \n",
       "75%       1.000000    48.000000     0.800000   170.000000     7.000000  ...   \n",
       "max       1.000000    64.000000     1.000000   200.000000     8.000000  ...   \n",
       "\n",
       "         px_height     px_width          ram         sc_h         sc_w  \\\n",
       "count  2000.000000  2000.000000  2000.000000  2000.000000  2000.000000   \n",
       "mean    645.108000  1251.515500  2124.213000    12.306500     5.767000   \n",
       "std     443.780811   432.199447  1084.732044     4.213245     4.356398   \n",
       "min       0.000000   500.000000   256.000000     5.000000     0.000000   \n",
       "25%     282.750000   874.750000  1207.500000     9.000000     2.000000   \n",
       "50%     564.000000  1247.000000  2146.500000    12.000000     5.000000   \n",
       "75%     947.250000  1633.000000  3064.500000    16.000000     9.000000   \n",
       "max    1960.000000  1998.000000  3998.000000    19.000000    18.000000   \n",
       "\n",
       "         talk_time      three_g  touch_screen         wifi  price_range  \n",
       "count  2000.000000  2000.000000   2000.000000  2000.000000  2000.000000  \n",
       "mean     11.011000     0.761500      0.503000     0.507000     1.500000  \n",
       "std       5.463955     0.426273      0.500116     0.500076     1.118314  \n",
       "min       2.000000     0.000000      0.000000     0.000000     0.000000  \n",
       "25%       6.000000     1.000000      0.000000     0.000000     0.750000  \n",
       "50%      11.000000     1.000000      1.000000     1.000000     1.500000  \n",
       "75%      16.000000     1.000000      1.000000     1.000000     2.250000  \n",
       "max      20.000000     1.000000      1.000000     1.000000     3.000000  \n",
       "\n",
       "[8 rows x 21 columns]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb940380",
   "metadata": {},
   "source": [
    "**With the following code I want which data contain integer values and which have floating data values:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "35871cf6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>pc</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>842</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>188</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>20</td>\n",
       "      <td>756</td>\n",
       "      <td>2549</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1021</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>53</td>\n",
       "      <td>136</td>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "      <td>905</td>\n",
       "      <td>1988</td>\n",
       "      <td>2631</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>563</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>41</td>\n",
       "      <td>145</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>1263</td>\n",
       "      <td>1716</td>\n",
       "      <td>2603</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>615</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>131</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>1216</td>\n",
       "      <td>1786</td>\n",
       "      <td>2769</td>\n",
       "      <td>16</td>\n",
       "      <td>8</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1821</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>44</td>\n",
       "      <td>141</td>\n",
       "      <td>2</td>\n",
       "      <td>14</td>\n",
       "      <td>1208</td>\n",
       "      <td>1212</td>\n",
       "      <td>1411</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   battery_power  blue  dual_sim  fc  four_g  int_memory  mobile_wt  n_cores  \\\n",
       "0            842     0         0   1       0           7        188        2   \n",
       "1           1021     1         1   0       1          53        136        3   \n",
       "2            563     1         1   2       1          41        145        5   \n",
       "3            615     1         0   0       0          10        131        6   \n",
       "4           1821     1         0  13       1          44        141        2   \n",
       "\n",
       "   pc  px_height  px_width   ram  sc_h  sc_w  talk_time  three_g  \\\n",
       "0   2         20       756  2549     9     7         19        0   \n",
       "1   6        905      1988  2631    17     3          7        1   \n",
       "2   6       1263      1716  2603    11     2          9        1   \n",
       "3   9       1216      1786  2769    16     8         11        1   \n",
       "4  14       1208      1212  1411     8     2         15        1   \n",
       "\n",
       "   touch_screen  wifi  price_range  \n",
       "0             0     1            1  \n",
       "1             1     0            2  \n",
       "2             1     0            2  \n",
       "3             0     0            2  \n",
       "4             1     0            1  "
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_categorical=data.select_dtypes(include='int64')\n",
    "data_categorical.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "50cf88b0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>m_dep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.2</td>\n",
       "      <td>0.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.5</td>\n",
       "      <td>0.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.5</td>\n",
       "      <td>0.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2.5</td>\n",
       "      <td>0.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.2</td>\n",
       "      <td>0.6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   clock_speed  m_dep\n",
       "0          2.2    0.6\n",
       "1          0.5    0.7\n",
       "2          0.5    0.9\n",
       "3          2.5    0.8\n",
       "4          1.2    0.6"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_categorical=data.select_dtypes(include='float64')\n",
    "data_categorical.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69727054",
   "metadata": {},
   "source": [
    "**The following graph shows the participation by price range:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "caf7d8b7",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = data[\"price_range\"].value_counts().index\n",
    "sizes = data[\"price_range\"].value_counts()\n",
    "colors = sns.color_palette('pastel')[0:10]\n",
    "plt.figure(figsize = (5,5))\n",
    "plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.1f%%',colors=colors,shadow=True, startangle=90)\n",
    "plt.title('Participation by price range',color = 'green',fontsize = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d1017ae",
   "metadata": {},
   "source": [
    "**With the following graph we can see the participation by price range and by mobile features:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "d9997526",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style type=\"text/css\">\n",
       "#T_56f28_row0_col0, #T_56f28_row4_col0 {\n",
       "  background-color: #d95847;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row0_col1, #T_56f28_row1_col1 {\n",
       "  background-color: #dddcdc;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row0_col2 {\n",
       "  background-color: #a5c3fe;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row0_col3 {\n",
       "  background-color: #4a63d3;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row0_col4 {\n",
       "  background-color: #5977e3;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row0_col5, #T_56f28_row3_col5, #T_56f28_row5_col5 {\n",
       "  background-color: #efcebd;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row1_col0, #T_56f28_row5_col0 {\n",
       "  background-color: #5d7ce6;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row1_col2 {\n",
       "  background-color: #f7b396;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row1_col3 {\n",
       "  background-color: #c73635;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row1_col4 {\n",
       "  background-color: #d65244;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row1_col5, #T_56f28_row2_col5, #T_56f28_row4_col5 {\n",
       "  background-color: #c5d6f2;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row2_col0 {\n",
       "  background-color: #f18d6f;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row2_col1 {\n",
       "  background-color: #aac7fd;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row2_col2 {\n",
       "  background-color: #90b2fe;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row2_col3 {\n",
       "  background-color: #445acc;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row2_col4 {\n",
       "  background-color: #6485ec;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row3_col0 {\n",
       "  background-color: #82a6fb;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row3_col1 {\n",
       "  background-color: #f7b89c;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row3_col2 {\n",
       "  background-color: #f59d7e;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row3_col3 {\n",
       "  background-color: #c0282f;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row3_col4 {\n",
       "  background-color: #e0654f;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row4_col1 {\n",
       "  background-color: #e5d8d1;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row4_col2 {\n",
       "  background-color: #ebd3c6;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row4_col3, #T_56f28_row5_col4, #T_56f28_row7_col0, #T_56f28_row7_col1, #T_56f28_row7_col2, #T_56f28_row7_col5 {\n",
       "  background-color: #3b4cc0;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row4_col4, #T_56f28_row5_col3, #T_56f28_row6_col0, #T_56f28_row6_col1, #T_56f28_row6_col2, #T_56f28_row6_col5 {\n",
       "  background-color: #b40426;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row5_col1 {\n",
       "  background-color: #d4dbe6;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row5_col2 {\n",
       "  background-color: #ccd9ed;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row6_col3 {\n",
       "  background-color: #b50927;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row6_col4 {\n",
       "  background-color: #cad8ef;\n",
       "  color: #000000;\n",
       "}\n",
       "#T_56f28_row7_col3 {\n",
       "  background-color: #3c4ec2;\n",
       "  color: #f1f1f1;\n",
       "}\n",
       "#T_56f28_row7_col4 {\n",
       "  background-color: #edd2c3;\n",
       "  color: #000000;\n",
       "}\n",
       "</style>\n",
       "<table id=\"T_56f28\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th class=\"blank\" >&nbsp;</th>\n",
       "      <th class=\"blank level0\" >&nbsp;</th>\n",
       "      <th id=\"T_56f28_level0_col0\" class=\"col_heading level0 col0\" >blue</th>\n",
       "      <th id=\"T_56f28_level0_col1\" class=\"col_heading level0 col1\" >dual_sim</th>\n",
       "      <th id=\"T_56f28_level0_col2\" class=\"col_heading level0 col2\" >four_g</th>\n",
       "      <th id=\"T_56f28_level0_col3\" class=\"col_heading level0 col3\" >Three_g</th>\n",
       "      <th id=\"T_56f28_level0_col4\" class=\"col_heading level0 col4\" >touch_screen</th>\n",
       "      <th id=\"T_56f28_level0_col5\" class=\"col_heading level0 col5\" >wifi</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th class=\"index_name level0\" >price_range</th>\n",
       "      <th class=\"index_name level1\" >&nbsp;</th>\n",
       "      <th class=\"blank col0\" >&nbsp;</th>\n",
       "      <th class=\"blank col1\" >&nbsp;</th>\n",
       "      <th class=\"blank col2\" >&nbsp;</th>\n",
       "      <th class=\"blank col3\" >&nbsp;</th>\n",
       "      <th class=\"blank col4\" >&nbsp;</th>\n",
       "      <th class=\"blank col5\" >&nbsp;</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level0_row0\" class=\"row_heading level0 row0\" rowspan=\"2\">0</th>\n",
       "      <th id=\"T_56f28_level1_row0\" class=\"row_heading level1 row0\" >0</th>\n",
       "      <td id=\"T_56f28_row0_col0\" class=\"data row0 col0\" >257</td>\n",
       "      <td id=\"T_56f28_row0_col1\" class=\"data row0 col1\" >250</td>\n",
       "      <td id=\"T_56f28_row0_col2\" class=\"data row0 col2\" >241</td>\n",
       "      <td id=\"T_56f28_row0_col3\" class=\"data row0 col3\" >127</td>\n",
       "      <td id=\"T_56f28_row0_col4\" class=\"data row0 col4\" >238</td>\n",
       "      <td id=\"T_56f28_row0_col5\" class=\"data row0 col5\" >252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level1_row1\" class=\"row_heading level1 row1\" >1</th>\n",
       "      <td id=\"T_56f28_row1_col0\" class=\"data row1 col0\" >243</td>\n",
       "      <td id=\"T_56f28_row1_col1\" class=\"data row1 col1\" >250</td>\n",
       "      <td id=\"T_56f28_row1_col2\" class=\"data row1 col2\" >259</td>\n",
       "      <td id=\"T_56f28_row1_col3\" class=\"data row1 col3\" >373</td>\n",
       "      <td id=\"T_56f28_row1_col4\" class=\"data row1 col4\" >262</td>\n",
       "      <td id=\"T_56f28_row1_col5\" class=\"data row1 col5\" >248</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level0_row2\" class=\"row_heading level0 row2\" rowspan=\"2\">1</th>\n",
       "      <th id=\"T_56f28_level1_row2\" class=\"row_heading level1 row2\" >0</th>\n",
       "      <td id=\"T_56f28_row2_col0\" class=\"data row2 col0\" >255</td>\n",
       "      <td id=\"T_56f28_row2_col1\" class=\"data row2 col1\" >245</td>\n",
       "      <td id=\"T_56f28_row2_col2\" class=\"data row2 col2\" >238</td>\n",
       "      <td id=\"T_56f28_row2_col3\" class=\"data row2 col3\" >122</td>\n",
       "      <td id=\"T_56f28_row2_col4\" class=\"data row2 col4\" >239</td>\n",
       "      <td id=\"T_56f28_row2_col5\" class=\"data row2 col5\" >248</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level1_row3\" class=\"row_heading level1 row3\" >1</th>\n",
       "      <td id=\"T_56f28_row3_col0\" class=\"data row3 col0\" >245</td>\n",
       "      <td id=\"T_56f28_row3_col1\" class=\"data row3 col1\" >255</td>\n",
       "      <td id=\"T_56f28_row3_col2\" class=\"data row3 col2\" >262</td>\n",
       "      <td id=\"T_56f28_row3_col3\" class=\"data row3 col3\" >378</td>\n",
       "      <td id=\"T_56f28_row3_col4\" class=\"data row3 col4\" >261</td>\n",
       "      <td id=\"T_56f28_row3_col5\" class=\"data row3 col5\" >252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level0_row4\" class=\"row_heading level0 row4\" rowspan=\"2\">2</th>\n",
       "      <th id=\"T_56f28_level1_row4\" class=\"row_heading level1 row4\" >0</th>\n",
       "      <td id=\"T_56f28_row4_col0\" class=\"data row4 col0\" >257</td>\n",
       "      <td id=\"T_56f28_row4_col1\" class=\"data row4 col1\" >251</td>\n",
       "      <td id=\"T_56f28_row4_col2\" class=\"data row4 col2\" >253</td>\n",
       "      <td id=\"T_56f28_row4_col3\" class=\"data row4 col3\" >113</td>\n",
       "      <td id=\"T_56f28_row4_col4\" class=\"data row4 col4\" >265</td>\n",
       "      <td id=\"T_56f28_row4_col5\" class=\"data row4 col5\" >248</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level1_row5\" class=\"row_heading level1 row5\" >1</th>\n",
       "      <td id=\"T_56f28_row5_col0\" class=\"data row5 col0\" >243</td>\n",
       "      <td id=\"T_56f28_row5_col1\" class=\"data row5 col1\" >249</td>\n",
       "      <td id=\"T_56f28_row5_col2\" class=\"data row5 col2\" >247</td>\n",
       "      <td id=\"T_56f28_row5_col3\" class=\"data row5 col3\" >387</td>\n",
       "      <td id=\"T_56f28_row5_col4\" class=\"data row5 col4\" >235</td>\n",
       "      <td id=\"T_56f28_row5_col5\" class=\"data row5 col5\" >252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level0_row6\" class=\"row_heading level0 row6\" rowspan=\"2\">3</th>\n",
       "      <th id=\"T_56f28_level1_row6\" class=\"row_heading level1 row6\" >1</th>\n",
       "      <td id=\"T_56f28_row6_col0\" class=\"data row6 col0\" >259</td>\n",
       "      <td id=\"T_56f28_row6_col1\" class=\"data row6 col1\" >265</td>\n",
       "      <td id=\"T_56f28_row6_col2\" class=\"data row6 col2\" >275</td>\n",
       "      <td id=\"T_56f28_row6_col3\" class=\"data row6 col3\" >385</td>\n",
       "      <td id=\"T_56f28_row6_col4\" class=\"data row6 col4\" >248</td>\n",
       "      <td id=\"T_56f28_row6_col5\" class=\"data row6 col5\" >262</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th id=\"T_56f28_level1_row7\" class=\"row_heading level1 row7\" >0</th>\n",
       "      <td id=\"T_56f28_row7_col0\" class=\"data row7 col0\" >241</td>\n",
       "      <td id=\"T_56f28_row7_col1\" class=\"data row7 col1\" >235</td>\n",
       "      <td id=\"T_56f28_row7_col2\" class=\"data row7 col2\" >225</td>\n",
       "      <td id=\"T_56f28_row7_col3\" class=\"data row7 col3\" >115</td>\n",
       "      <td id=\"T_56f28_row7_col4\" class=\"data row7 col4\" >252</td>\n",
       "      <td id=\"T_56f28_row7_col5\" class=\"data row7 col5\" >238</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x2afad0e0790>"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(data = [data.groupby('price_range')['blue'].value_counts(), \n",
    "                     data.groupby('price_range')['dual_sim'].value_counts(),\n",
    "                     data.groupby('price_range')['four_g'].value_counts(),\n",
    "                     data.groupby('price_range')['three_g'].value_counts(),\n",
    "                     data.groupby('price_range')['touch_screen'].value_counts(),\n",
    "                     data.groupby('price_range')['wifi'].value_counts()],  \n",
    "\n",
    "             index=[\"blue\", \"dual_sim\",\"four_g\",\"Three_g\",\"touch_screen\",\"wifi\"]).T.style.background_gradient(cmap='coolwarm')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68ec1207",
   "metadata": {},
   "source": [
    "**The following graph shows the distribution for each feature of the dataset:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "4f564838",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 21 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots(3, 7,figsize=(20,10))\n",
    "axe = axes.flatten()\n",
    "color_palette = sns.color_palette(\"pastel\") + sns.color_palette(\"Set2\") + sns.color_palette(\"husl\", 25)\n",
    "\n",
    "\n",
    "for i,feature in enumerate(data.columns):\n",
    "    sns.histplot(data=data, x=feature, kde=True, ax=axe[i], color=color_palette[i])    \n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47612af0",
   "metadata": {},
   "source": [
    "**The following graph shows the boxplot for each feature of the dataset:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "aad51216",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 21 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots(3, 7,figsize=(20,10))\n",
    "axe = axes.flatten()\n",
    "\n",
    "for i,feature in enumerate(data.columns):\n",
    "    sns.boxplot(data=data, x=feature, ax=axe[i], color=color_palette[i])    \n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c201f81",
   "metadata": {},
   "source": [
    "# 4. Feature Engineering"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a9e9f94",
   "metadata": {},
   "source": [
    "Once we have analyzed the information in our dataset, we proceed to prepare the data to apply the prediction models."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "e1297f1c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>0 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi, price_range]\n",
       "Index: []\n",
       "\n",
       "[0 rows x 21 columns]"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.duplicated()]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "795424d2",
   "metadata": {},
   "source": [
    "**I haven't duplicate values in the data set. Now we gonna see the relation with the target variable:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "4950cd41",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "price_range      1.000000\n",
       "ram              0.917046\n",
       "battery_power    0.200723\n",
       "px_width         0.165818\n",
       "px_height        0.148858\n",
       "int_memory       0.044435\n",
       "sc_w             0.038711\n",
       "pc               0.033599\n",
       "three_g          0.023611\n",
       "sc_h             0.022986\n",
       "fc               0.021998\n",
       "talk_time        0.021859\n",
       "blue             0.020573\n",
       "wifi             0.018785\n",
       "dual_sim         0.017444\n",
       "four_g           0.014772\n",
       "n_cores          0.004399\n",
       "m_dep            0.000853\n",
       "clock_speed     -0.006606\n",
       "mobile_wt       -0.030302\n",
       "touch_screen    -0.030411\n",
       "Name: price_range, dtype: float64"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.corr()[\"price_range\"].sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "d9f9a819",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 936x648 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(13,9))\n",
    "sns.heatmap(data.corr(), vmax=0.8, linewidth=0.1, cmap='vlag')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "259750ec",
   "metadata": {},
   "source": [
    "**Price appears to be highly correlated with RAM. In addition, clock_speed, mobile_wt and touch_screen appear to be negatively correlated, indicating that there is a relationship between them, such that as the value of one variable increases, the value of the other decreases.**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0001bbed",
   "metadata": {},
   "source": [
    "# 5. Training and Evaluating Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "dcee8fa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1500, 20) (1500,) (500, 20) (500,)\n"
     ]
    }
   ],
   "source": [
    "X = data.drop('price_range',axis=1)\n",
    "y = data['price_range']\n",
    "\n",
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)\n",
    "print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80298399",
   "metadata": {},
   "source": [
    "**Train and Fit Models**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "bdef7cc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    }
   ],
   "source": [
    "Model1 = LogisticRegression()\n",
    "Model1.fit(X_train, y_train)\n",
    "predicts1 = Model1.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "0b3ac2ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression\n",
      "\n",
      "Accuracy test:  61.6\n",
      "\n",
      "classification report\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.79      0.72      0.75       132\n",
      "           1       0.49      0.50      0.49       118\n",
      "           2       0.50      0.49      0.50       120\n",
      "           3       0.67      0.73      0.70       130\n",
      "\n",
      "    accuracy                           0.62       500\n",
      "   macro avg       0.61      0.61      0.61       500\n",
      "weighted avg       0.62      0.62      0.62       500\n",
      "\n",
      "Confusion Matrix\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 15.0, 'Predicted label')"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(\"Logistic Regression\")\n",
    "Model1_acc = accuracy_score(y_test, predicts1)*100\n",
    "\n",
    "print(\"\\nAccuracy test: \", round(Model1_acc,2))\n",
    "\n",
    "print(\"\\nclassification report\\n\")\n",
    "report1 = classification_report(y_test, predicts1)\n",
    "print(report1)\n",
    "\n",
    "print(\"Confusion Matrix\")\n",
    "confusionmatrix1 = confusion_matrix(y_test, predicts1)\n",
    "p = sns.heatmap(pd.DataFrame(confusionmatrix1), annot=True,fmt='g')\n",
    "plt.title('Confusion matrix')\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "299087e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "Model2 = KNeighborsClassifier()\n",
    "Model2.fit(X_train, y_train)\n",
    "predicts2 = Model2.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "a8c09ee4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNeighbors Classifier_ Metrics\n",
      "\n",
      "Accuracy test:  93.2\n",
      "\n",
      "classification report\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.95      0.95      0.95       132\n",
      "           1       0.89      0.93      0.91       118\n",
      "           2       0.92      0.89      0.91       120\n",
      "           3       0.96      0.95      0.95       130\n",
      "\n",
      "    accuracy                           0.93       500\n",
      "   macro avg       0.93      0.93      0.93       500\n",
      "weighted avg       0.93      0.93      0.93       500\n",
      "\n",
      "Confusion Matrix\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 15.0, 'Predicted label')"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(\"KNeighbors Classifier_ Metrics\")\n",
    "Model2_acc = accuracy_score(y_test, predicts2)*100\n",
    "\n",
    "print(\"\\nAccuracy test: \", round(Model2_acc,2))\n",
    "\n",
    "print(\"\\nclassification report\\n\")\n",
    "report2 = classification_report(y_test, predicts2)\n",
    "print(report2)\n",
    "\n",
    "print(\"Confusion Matrix\")\n",
    "confusionmatrix2 = confusion_matrix(y_test, predicts2)\n",
    "p = sns.heatmap(pd.DataFrame(confusionmatrix2), annot=True,fmt='g')\n",
    "plt.title('Confusion matrix')\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e531eca",
   "metadata": {},
   "source": [
    "**Dimensional Reduction** (Principal Component Analysis: PCA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "a04cd6e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The Importance of each column is explained by %:  [0.67043953 0.16517904]\n",
      "\n",
      "Final DataFrame\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Component1</th>\n",
       "      <th>Component2</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>430.596294</td>\n",
       "      <td>-795.788745</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>504.985048</td>\n",
       "      <td>696.622162</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>473.330120</td>\n",
       "      <td>763.941758</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>639.822549</td>\n",
       "      <td>779.690737</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-718.985233</td>\n",
       "      <td>382.304896</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Component1  Component2  price_range\n",
       "0  430.596294 -795.788745            1\n",
       "1  504.985048  696.622162            2\n",
       "2  473.330120  763.941758            2\n",
       "3  639.822549  779.690737            2\n",
       "4 -718.985233  382.304896            1"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pca = PCA(n_components=2)\n",
    "principalComponents = pca.fit_transform(data)\n",
    "principalDf = pd.DataFrame(data = principalComponents, columns=['Component1','Component2'])\n",
    "print('\\nThe Importance of each column is explained by %: ',pca.explained_variance_ratio_)\n",
    "finaldata=principalDf.join(data['price_range'])\n",
    "print('\\nFinal DataFrame')\n",
    "finaldata.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "72c5c702",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = finaldata.drop('price_range',axis=1)\n",
    "y = finaldata['price_range']\n",
    "\n",
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "cd157bfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "Model1_pca = LogisticRegression()\n",
    "Model1_pca.fit(X_train, y_train)\n",
    "predicts1_pca = Model1_pca.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "bb7b91e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression_PCA\n",
      "\n",
      "Accuracy test:  80.6\n",
      "\n",
      "classification report\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.88      0.89      0.88       132\n",
      "           1       0.75      0.74      0.74       118\n",
      "           2       0.72      0.74      0.73       120\n",
      "           3       0.87      0.85      0.86       130\n",
      "\n",
      "    accuracy                           0.81       500\n",
      "   macro avg       0.80      0.80      0.80       500\n",
      "weighted avg       0.81      0.81      0.81       500\n",
      "\n",
      "\n",
      "Confusion Matrix\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 15.0, 'Predicted label')"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(\"Logistic Regression_PCA\")\n",
    "Model1_pca_acc = accuracy_score(y_test, predicts1_pca)*100\n",
    "\n",
    "print(\"\\nAccuracy test: \", round(Model1_pca_acc,2))\n",
    "\n",
    "print(\"\\nclassification report\\n\")\n",
    "report3 = classification_report(y_test, predicts1_pca)\n",
    "print(report3)\n",
    "\n",
    "print(\"\\nConfusion Matrix\")\n",
    "confusionmatrix3 = confusion_matrix(y_test, predicts1_pca)\n",
    "p = sns.heatmap(pd.DataFrame(confusionmatrix3), annot=True,fmt='g')\n",
    "plt.title('Confusion matrix')\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "89970c9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Model2_pca = KNeighborsClassifier()\n",
    "Model2_pca.fit(X_train, y_train)\n",
    "predicts2_pca = Model2_pca.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "ae8d9c49",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNN_PCA\n",
      "\n",
      "Accuracy test:  80.0\n",
      "\n",
      "classification report\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.90      0.86      0.88       132\n",
      "           1       0.71      0.75      0.73       118\n",
      "           2       0.71      0.71      0.71       120\n",
      "           3       0.86      0.87      0.87       130\n",
      "\n",
      "    accuracy                           0.80       500\n",
      "   macro avg       0.80      0.80      0.80       500\n",
      "weighted avg       0.80      0.80      0.80       500\n",
      "\n",
      "\n",
      "Confusion Matrix\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 15.0, 'Predicted label')"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(\"KNN_PCA\\n\")\n",
    "Model2_pca_acc = accuracy_score(y_test, predicts2_pca)*100\n",
    "print(\"Accuracy test: \", round(Model2_pca_acc,2))\n",
    "\n",
    "print(\"\\nclassification report\\n\")\n",
    "report4 = classification_report(y_test, predicts2_pca)\n",
    "print(report4)\n",
    "\n",
    "print(\"\\nConfusion Matrix\")\n",
    "confusionmatrix4 = confusion_matrix(y_test, predicts2_pca)\n",
    "p = sns.heatmap(pd.DataFrame(confusionmatrix4), annot=True,fmt='g')\n",
    "plt.title('Confusion matrix')\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2390a8c6",
   "metadata": {},
   "source": [
    "# 6. Conclusion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "ad5f614e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>Accuracy</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Logistic Regression</td>\n",
       "      <td>61.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Logistic Regression_PCA</td>\n",
       "      <td>80.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>KNeighbors Classifier</td>\n",
       "      <td>93.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>KNeighbors Classifier_PCA</td>\n",
       "      <td>80.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Model  Accuracy\n",
       "0        Logistic Regression      61.6\n",
       "1    Logistic Regression_PCA      80.6\n",
       "2      KNeighbors Classifier      93.2\n",
       "3  KNeighbors Classifier_PCA      80.0"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "conclusion = pd.DataFrame({\n",
    "    'Model': ['Logistic Regression','Logistic Regression_PCA', 'KNeighbors Classifier', 'KNeighbors Classifier_PCA'],\n",
    "    'Accuracy': [Model1_acc,Model1_pca_acc,Model2_acc,Model2_pca_acc,]})\n",
    "\n",
    "conclusion.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9eaf430",
   "metadata": {},
   "source": [
    "After a comprehensive analysis of the Mobile Prices dataset, we've gained valuable insights into the factors influencing the pricing of mobile phones. The answer to the question of why some phones cost more than others can be attributed to several key findings:\n",
    "\n",
    "**~RAM Matters:** One of the most significant factors contributing to higher mobile phone prices is RAM. Phones with more RAM tend to be priced higher, likely because of their superior performance and ability to handle more tasks simultaneously.\n",
    "\n",
    "**~Quality Over Quantity:** The quality of features like camera resolution, battery capacity, and screen size plays a crucial role in pricing. Higher-end components often lead to higher prices.\n",
    "\n",
    "**~Touch Screen and Connectivity:** Phones with touch screens and advanced connectivity options, such as Wi-Fi and 4G support, tend to command higher prices due to their enhanced user experience and connectivity capabilities.\n",
    "\n",
    "**~Competition and Brand:** The reputation of a brand and the competitive landscape in the mobile phone market can also impact pricing. Established brands may charge a premium for their products.\n",
    "\n",
    "**~Performance:** Faster processors and more cores can increase a phone's price, as they deliver better performance for demanding tasks.\n",
    "\n",
    "**~Dimensional Reduction (PCA):** The application of Principal Component Analysis (PCA) revealed that some features were more critical than others in determining mobile phone prices. This technique allowed us to understand which attributes had the most significant impact on pricing.\n",
    "\n",
    "In conclusion, while price differences can be attributed to a combination of factors, including specifications, brand reputation, and market dynamics, RAM and the quality of hardware components stand out as key drivers for variations in mobile phone prices. This analysis provides valuable insights into the \"why\" behind the pricing of mobile phones, enabling consumers and industry professionals to make more informed decisions in the ever-evolving mobile market."
   ]
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
