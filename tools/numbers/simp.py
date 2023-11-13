def adding(n1, n2):
    """
    returns sum of numbers from input
    """
    return n1 + n2

def substracting(n1, n2):
    """
    returns sum of numbers from input
    """
    return n1 -n2

def perform_operation(n1, n2, operation):
    if operation == 'sum':
        return adding(n1, n2)
    elif operation == 'subtract':
        return substracting(n1, n2)

if __name__ == '__main__':
    print(adding(2,3))
    print(adding(0.1, 2))
    print(substracting(0,5))
    print(substracting(3,7.4))
