def sum(x, y):
    return x + y
def diff(x, y):
    return x - y

def log_details(fnc):
    logInfo = "Logging into the system.."
    def innerFun(*arg):
        print(logInfo)
        print(fnc(*arg))
        print("-" * 40)
    return innerFun

sum_logger = log_details(sum)

diff_logger = log_details(diff)

sum_logger(10, 20)
diff_logger(35, 25)