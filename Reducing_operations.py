class ReducingOperations:
    def __init__(self):
        pass

    @staticmethod
    def reduce_minus(math_list):
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

    @staticmethod
    def reduce_plus(math_list):
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

    @staticmethod
    def reduce_plus_minus(math_list):
        """
        This method replace sequence of ' + '.
        for example:
        5+8-9*2/3+++++8+322^2+++55 => 5+8-9*2/3+8+322^2
        :param math_list:
        :return:
        """
        math_list = list(math_list)
        count_plus_flag = False
        counter = 0
        counter_i = 0

        for i in math_list:
            if i == '+':
                if math_list[counter + 1] == '-':
                    math_list[counter] = '-'
                    math_list.pop(counter + 1)
            elif i == '-':
                if math_list[counter + 1] == '+':
                    math_list[counter] = '-'
                    math_list.pop(counter + 1)
            counter += 1

        return math_list

    def reduce(self, math_list):
        math_list = self.reduce_minus(math_list)
        math_list = self.reduce_plus(math_list)
        return self.reduce_plus_minus(math_list)
