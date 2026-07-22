# Pandas documentation: https://pandas.pydata.org/docs/

import pandas

"""
Please make sure you have pandas installed. You can install it with pip from your computer or 
Atom/VS Code terminal/cmd just like you have installed other third-party packages. 
Please execute one of the commands below to do the installation depending on what version of Python you are using:

pip3.10 install pandas

or

pip3.9 install pandas

or

pip3.8 install pandas

etc.

Also, in the next lecture, we will use an enhanced Python interactive shell called IPython.

IPython is just like the standard shell you get when you run Python, but IPython provides better printing for large text. 
This ability makes IPython suitable for data analysis because the program prints data in a well-structured format. 
You can install IPython with pip:

pip3.10 install ipython

or

pip3.9 install ipython

or

pip3.8 install ipython
"""
#-----------------------------------------------------------------------------------------------------------------------------------------

# Dentro del CMD
"""
Microsoft Windows [Versión 10.0.26100.6584]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\Usuario>ipython
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.5.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use `%timeit` or `%%timeit`, and the  `-r`, `-n`, and `-o` options to easily profile your code.

In [1]: import pandas


In [3]: df1=pandas.DataFrame([[2,4,6],[10,20,30]])

In [4]: df1
Out[4]:
    0   1   2
0   2   4   6
1  10  20  30

In [7]: df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

In [8]: df1
Out[8]:
   Price  Age  Value
0      2    4      6
1     10   20     30

In [9]: df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First", "Second"])

In [10]: df1
Out[10]:
        Price  Age  Value
First       2    4      6
Second     10   20     30

In [12]: df2=pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

In [13]: df2
Out[13]:
   Name
0  John
1  Jack

In [14]: df2=pandas.DataFrame([{"Name":"John","Surname":"Johns"},{"Name":"Jack"}])

In [15]: df2
Out[15]:
   Name Surname
0  John   Johns
1  Jack     NaN

In [16]: df1.Price.mean()
Out[16]: np.float64(6.0)
"""

import cv2
