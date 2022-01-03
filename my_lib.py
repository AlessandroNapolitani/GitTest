
    #conventions non yet implemented
    #_______________________________

    # ClassName
	#     method_name
	# ExceptionName
    #instance_var_name


CALL_STRING = "call" + " "
FUNC_STRING = "function" + " "

func_name = ""

def set_func_name(value):

    global func_name 

    func_name = value

def print_call():

    global func_name 

    print(CALL_STRING + func_name)

def print_func():

    global func_name 

    print(FUNC_STRING + func_name)

def test_Function():

    print_func()

    out_str = "Test: Ok"

    print(out_str)
