from calculator_exception import *
import check_exp
import re

test_str = ""
VALID_CHARACTERS = ['+', '-', '*', '%', '/', '!', '~', '^', '(', ')']

class ConvertString:
    """
          A class used to convert the string to list

          ...

          Methods
          -------
          convert_to_list() - function convert the math string to list

          create_list_from_string() - convert the string to list

          clean_unwanted_char() - clean the list from unwanted signs
            """
    def __init__(self):
        pass

    @staticmethod
    def create_list_from_string(string_exp):
        """
        This method create a list from the string math expression
        for example :
                    "4+5/21+3*542" =>>>>  ['4','5','/','21,'+','3','*','542'
        :param string_exp:
        :return:
        """
        return re.split('(\D)', string_exp)

    @staticmethod
    def clean_unwanted_char(string_exp):
        # remove all '' if there are this sign ~ !
        for i in string_exp:
            if i == '':
                string_exp.remove('')
        return string_exp

    def convert_to_list(self, string_exp):
        math_list = self.create_list_from_string(string_exp)
        return self.clean_unwanted_char(math_list)


class ParseExpression:
    """
       A class used to parse the expression

       ...

       Attributes
       ----------

       """

    def remove_character_minus_sequence(self,math_list):
        """
        This method replace sequence of ' - '.
        for example:
                    5+8---9*2/3------8+322^2 => 5+8-9*2/3+8+322^2
        :param math_list:
        :return:
        """
        math_list = list(math_list)
        counterplus = 0
        counterminus = 0
        count_plus_flag = False
        counter = 0
        counter_i = 0

        for i in math_list:
            if i == '-':
                count_plus_flag = True
                counter = counter_i
                counterminus += 1
                while count_plus_flag:
                    if math_list[counter + 1] == '-':
                        counterplus += 1
                        math_list.pop(counter + 1)
                        counterminus += 1
                    else:
                        if counterminus % 2 == 0:
                            math_list[counter_i] = '+'
                        count_plus_flag = False
                        counterminus = 0
                counterplus = 0

            counter_i += 1

        return math_list

    def remove_character_plus_sequence(self,math_list):
        """
        This method replace sequence of ' + '.
        for example:
                    5+8-9*2/3+++++8+322^2+++55 => 5+8-9*2/3+8+322^2
        :param math_list:
        :return:
        """
        math_list = list(math_list)
        counterplus = 0
        count_plus_flag = False
        counter = 0
        counter_i = 0

        for i in math_list:
            if i == '+':
                count_plus_flag = True
                counter = counter_i
                while count_plus_flag:
                    if math_list[counter + 1] == '+':
                        counterplus = + 1
                        math_list.pop(counter + 1)
                    else:
                        count_plus_flag = False

            counter_i += 1

        return math_list

    def remove_character_minus_plus_sequence(self,math_list):
        pass


class Calculate:
    """
       A class used to parse the expression

       ...

       Attributes
       ----------
       says_str : str
           a formatted string to print out what the animal says
       name : str
           the name of the animal
       sound : str
           the sound that the animal makes
       num_legs : int
           the number of legs the animal has (default 4)

       Methods
       -------
       delete_symbol(sound=None)
           for example there is 5+8+-9  |   3/+6
           so the method do => 5+8-9    |   3/6

        create list from the expression
       """

    def __init__(self):
        pass

    def calculate_level7(self, math_list):
        """
        This method calculate the expression from operation of level 7
        The operation is => ~
        :param math_list: list of the expression
        :return:
        """
        counter = 0
        for sign in math_list:
            if sign == "~":
                if math_list[counter + 1].isdigit():
                    math_str = "~" + math_list[counter + 1]
                    answer = eval(math_str)
                    math_list[counter + 1] = str(answer)
                    math_list.remove("~")
                elif math_list[counter + 1] == "+":
                    math_str = "~" + math_list[counter + 2]
                    answer = eval(math_str)
                    math_list[counter + 2] = str(answer)
                    math_list.remove("~")
                    math_list.remove("+")
                else:
                    math_str = "~" + "-" + math_list[counter + 2]
                    answer = eval(math_str)
                    math_list[counter + 2] = str(answer)
                    math_list.remove("~")
                    math_list.remove("-")

    def calculate_level6(self, math_string):
        """
        This method calculate the expression from operation of level 6
        The operation is => !
        :param math_string:
        :return:
        """
        pass

    def calculate_level3(self, math_string):
        """
        This method calculate the expression from operation of level 3
        The operation is => ^
        :param math_string:
        :return:
        """
        pass

    def calculate_level2(self, math_string):
        """
        This method calculate the expression from operation of level 2
        The operation is => * , / , %
        :param math_string:
        :return:
        """
        pass

    def calculate_level1(self, math_string):
        """
        This method calculate the expression from operation of level 1
        The operation is => + , -
        :param math_string:
        :return:
        """
        pass


def get_expression_from_user():
    print("Hello")
    return input("Please write your expression\n")


def main():
    check_expression = check_exp.CheckString()
    c = ConvertString()
    p = ParseExpression()
    "get the math expression from the user"
    math_str = get_expression_from_user()
    "check the expression and return clean string"
    clean_str = check_expression.check_string(math_str)
    "Convert the string to list"
    list_math_exp = c.convert_to_list(clean_str)
    pass


if __name__ == "__main__":
    main()
