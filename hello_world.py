# Hello world test file for autopep8 testing

def hello_world(test_number):

    message = "Hello, World! I want to see if pep8 is working."
    length = len(message)
    print("The length of the message is: ", length)

    return test_number


if __name__ == "__main__":

    result = hello_world(15)
    print('test_numer is:', result)
