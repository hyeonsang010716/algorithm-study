import os
import importlib.util
from typing import List, Dict


def import_func_from_file(file_path: str):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "solution")


def search_file_path(number: int) -> str:
    filename = f"p{number}.py"
    curr_path = os.path.dirname(os.path.abspath(__file__))

    for root, _, files in os.walk(curr_path):
        for file in files:
            if file.endswith(filename):
                file_path = f"{root}/{filename}"
                return file_path
    return None


def get_answer(number: int, input_list: List[str]) -> Dict[str, List]:
    result_list = []
    file_path = search_file_path(number)
    if file_path:
        solution = import_func_from_file(file_path)
        for i in input_list:
            result_list.append(str(solution(i)))
        return {"answer": result_list}


if __name__ == "__main__":
    input_list1 = ['12\n1 2 3\n1 3 2\n2 4 5\n3 5 11\n3 6 9\n4 7 1\n4 8 7\n5 9 15\n5 10 4\n6 11 6\n6 12 10']
    input_list2 = ['5\n1 2 3']
    print(get_answer(1967, input_list1))
    print(get_answer(25344, input_list2))