import pygame
from my_lib import * 

def main(goodbye_str):

    global func_name

    print_func()

    set_func_name("test_Function()")

    print_call()

    test_Function()

    print(goodbye_str)

# Just a comment
# we ci sono
# we pure io

set_func_name("main()")

print_call()

main("bye bye, the program is terminated")
