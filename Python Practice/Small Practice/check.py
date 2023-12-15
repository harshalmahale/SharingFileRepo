final_string = ''

class TestCalculator:
    @staticmethod
    def str_change(str1):
        final_string = ''
        for i in str1:
            if i.isdigit():
                final_string += i
            else:
                final_string += '{' + i + '}'
        return final_string
    
print(final_string)