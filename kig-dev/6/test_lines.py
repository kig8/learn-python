from lines import check_args, count_loc
import pytest

basic_arg = ["lines.py"]

def test_cehck_args():
    with pytest.raises(SystemExit) as ex_info:
        check_args([*basic_arg])

    assert ex_info.value.code == "Too few command-line arguments"

    with pytest.raises(SystemExit) as ex_info:
        check_args([*basic_arg, "test.py", "hello"])

    assert ex_info.value.code == "Too many command-line arguments"

    with pytest.raises(SystemExit) as ex_info:
        check_args([*basic_arg, "test"])

    assert ex_info.value.code == "Not a python file"

    with pytest.raises(SystemExit) as ex_info:
        check_args([*basic_arg, "test.py"])

    assert ex_info.value.code == "File does not exist"


def test_count_loc():
    assert count_loc("../5/fuel.py") == 26
    assert count_loc("../5/bank.py") == 14
