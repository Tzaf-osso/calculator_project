test_str = ""


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
        :param math_string:
        :return:
        """
        status = True
        for i in math_string:
            if i in ['+', '-', '*', '%', '/', '!', '~', '(', ')'] or i.isdigit():
                pass
            else:
                status = False
                break
        return status

    @staticmethod
    def check_input_string():
        status = ""

    @staticmethod
    def check_balanced_barcks(self):
        # open_Bracket = []
        # close_Bracket = []
        pass

    @staticmethod
    def make_string_only_bracket(math_string):
        for i in math_string:
            if i in ['+', '-', '*', '%', '/', '!', '~'] or i.isdigit():
                math_string = math_string.replace(i, "")
            else:
                pass

        list_math_string = list(math_string)
        return list_math_string

    @staticmethod
    def check_bracket_valid_places(list_math_string):
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

    def tests(self, input_string):
        clean_string = self.delete_spaces(input_string)
        self.is_char_is_valid(clean_string)
