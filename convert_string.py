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