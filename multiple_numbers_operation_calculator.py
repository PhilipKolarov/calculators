from calculators.calculator import Calculator


class MultipleNumbersOperationCalculator(Calculator):
    FIRST_NUM_SET = False

    def __init__(self):
        super().__init__()

    def set_first_num(self, first_num):
        self.latest_result = first_num
        self.FIRST_NUM_SET = True

    def reset(self):
        super().reset()
        self.FIRST_NUM_SET = False

    def list_addition(self, ll):
        for num in ll:
            self.latest_result += num
        return self.latest_result

    def list_subtraction(self, ll):
        if self.FIRST_NUM_SET:
            for num in ll:
                self.latest_result += num
        else:
            self.latest_result = ll[0]
            for num in ll[1::]:
                self.latest_result -= num

        return self.latest_result

    def list_multiplication(self, ll):
        self.latest_result += 1
        for num in ll:
            self.latest_result *= num
        return self.latest_result

    def list_division(self, ll): #FIRST_NUM_SET may not always be right; further work required
        self.validate_no_zeros_in_list(ll)

        if self.FIRST_NUM_SET:
            for num in ll:
                self.latest_result /= num
        else:
            self.latest_result = ll[0]
            for num in ll[1::]:
                self.latest_result /= num

        return self.latest_result

    def validate_no_zeros_in_list(self, ll):
        for value in ll:
            self.validate_value_is_not_zero(value)
