from kfp.components import create_component_from_func


@create_component_from_func
def sum_and_print_numbers(number_1: int, number_2: int) -> int:
    sum_num = number_1 + number_2
    print(sum_num)
    return sum_num


if __name__ == "__main__":
    sum_and_print_numbers.component_spec.save("sum_and_print_numbers.yaml")
