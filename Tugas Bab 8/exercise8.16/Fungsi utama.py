#5 cara memanggil:

#1. import module_name
import my_functions
my_functions.favorite_book("Lord of the Flies")

#2. from module_name import function_name
from my_functions import favorite_book
favorite_book("Lord of the Flies")

#3. from module_name import function_name as fn
from my_functions import favorite_book as fb
fb("Lord of the Flies")

#4. import module_name as mn
import my_functions as mf
mf.favorite_book("Lord of the Flies")

#5. from module_name import *
from my_functions import *
favorite_book("Lord of the Flies")