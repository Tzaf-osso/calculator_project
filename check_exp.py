class CheckString:
    def __init__(self):
        pass

    @staticmethod
    def is_char_is_valid(math_string):
        """
        check if all the characters are normal
        normal chars = { digit,+,-,/,*,^,~,!,%,(,) }
        :param math_string:
        :return: status
        """
        status = True
        for i in math_string:
            if i in ['+', '-', '*', '.', '%', '/', '!', '~', '^', '(', ')', ' '] or i.isdigit():
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
    def check_balanced_brackets(math_expr):
        """
        This method check if thr brackets are balanced
        for example if there is open bracket without close bracket
        the brackets called unbalanced
        :param math_expr:
        :return:
        """
        status = ""
        open_bark = []
        close_bark = []
        index = 0
        for char in math_expr:
            if char == '(':
                open_bark.append(index)
            elif char == ')':
                close_bark.append(index)
            index += 1
        if len(open_bark) == len(close_bark):
            status = "Balanced"
        else:
            status = "unbalanced"
        return status, open_bark, close_bark
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
        return clean_string
