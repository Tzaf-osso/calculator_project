from calculator_exception import *

test_str = ""
VALID_CHARACTERS = ['+', '-', '*', '%', '/', '!', '~', '^', '(', ')']


def main():
    pass


class CheckString:
    def __init__(self):
        pass

    @staticmethod
    def delete_spaces(input_string):
        """
        This function delete the spaces
        example: 4 +4/8 *     (22+9)  =====>   4+4/8*(22+9)
        :param input_string:
        :return:
        """
        clean_string = input_string.replace(" ", "")  # delete spaces
        return clean_string

    @staticmethod
    def is_char_is_valid(math_string):
        """
        check if all the characters are normal
        normal chars = { digit,+,-,/,*,^,~,!,%,(,) }
        :param math_string:
        :return:
        """
        status = True
        for i in math_string:
            if i in ['+', '-', '*', '%', '/', '!', '~', '^', '(', ')', ' '] or i.isdigit():
                pass
            else:
                status = False
                break
        return status

    @staticmethod
    def check_follows_numbers(str_exp):
        """
        check if there is 2 numbers that follow without math expression
        for example:
        6+7*9 2+44/54 --------> wrong
        6+7*9+2+44/54 --------> good
        """
        tmp_str = " ".join((str_exp.split()))

        status = "good"
        for i in range(len(tmp_str)):
            if tmp_str[i] == ' ':
                if tmp_str[i - 1].isdigit() and tmp_str[i + 1].isdigit():
                    status = "wrong"

        return status

    @staticmethod
    def check_input_string():
        pass

    @staticmethod
    def check_balanced_barcks(self):
        # open_Bracket = []
        # close_Bracket = []
        pass

    @staticmethod
    def make_string_only_bracket(math_string):
        for i in math_string:
            if i in ['+', '-', '*', '%', '/', '^', '!', '~'] or i.isdigit():
                math_string = math_string.replace(i, "")
            else:
                pass

        list_math_string = list(math_string)
        return list_math_string

    @staticmethod
    def check_bracket_valid_places(list_math_string):
        """
        The function check if if all the bracket are open and close
        :param list_math_string:
        :return:
        """
        status = "good"
        bracket_counter = 0
        for i in list_math_string:
            if i == '(':
                bracket_counter += 1
            else:
                bracket_counter -= 1

            if bracket_counter < 0:
                status = "wrong"
                break
        if status != "minus":
            if bracket_counter > 0:
                status = "wrong"

        return status

    def check_bracket(self, math_string):
        self.check_balanced_barcks(math_string)
        #        self.check_barcks_places(math_string)
        self.check_bracket_valid_places(math_string)

    def check_string(self, input_string):
        status = True

        "check if all the chars are valid"
        status = self.is_char_is_valid(input_string)
        # check follow numbers
        status = self.check_follows_numbers(input_string)
        # clean the math string from spaces
        clean_string = self.delete_spaces(input_string)


class ParseExpression:
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

    if __name__ == "__main__":
        main()
