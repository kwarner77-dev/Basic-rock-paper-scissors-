#Validating data 

def toInt(s):

#processing

    isanumber = True

    if s == '':

        isanumber = False

    for ch in s:

        if ch  not in '0123456789':
            
            isanumber = False

            break

    return isanumber

#input

def toReal(s):


    n_decimals = 0

#processing

    isanumber = True

    if s == '':

        isanumber = False

    for ch in s:

        if ch  not in ' 0123456789.':

            isanumber = False
            break

    for ch in s:

        if ch == '.':
            n_decimals += 1

        if n_decimals > 1:

            isanumber = False
            break
        
    return isanumber


if __name__ == '__main__':

    #given some test cases and expected results

    test_data = ['13.4334', '1.234a', '1.23.4', '', '123', 'a123']

    expected_result_for_int = [False, False, False, False, True, False]

    expected_result_for_real = [True, False, False, False, True, False]

    #For each test case s

    for i in range(len(test_data)):

        s = test_data[i]

        #see what toInt returns with s as input
        
        result = toInt(s)

        if result != expected_result_for_int[i]:
            print('Test data {} has a bug in toInt'.format([i]))
                    
        # and see if result matches expected result


        # check if s can be converted to a real
            
        result = toReal(s)

        if result != expected_result_for_real[i]:
            print('Test data {} has a bug in toReal'.format([i]))

        # and see if result matches expected result





