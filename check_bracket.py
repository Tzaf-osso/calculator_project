class CheckBrackets:
    """
      A class used to check if there are brackets in the expression
      if there are brackets we check if there are balanced/
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
    def is_brackets_in_expression(math_expr):
        """
        This method check if the expression include brackets
        :param math_expr:
        :return: status
        """
        open_bracket = '('
        close_bracket = ')'
        math_expr = list(math_expr)
        status = False
        if open_bracket in math_expr or close_bracket in math_expr:
            status = True
        return status

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

    def check_brackets(self, math_string):
        status = self.is_brackets_in_expression(math_string)

        status = self.check_balanced_brackets(math_string)
        # self.check_barcks_places(math_string)
        self.check_bracket_valid_places(math_string)
