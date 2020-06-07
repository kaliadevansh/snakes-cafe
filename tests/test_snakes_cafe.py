import pytest

from snakes_cafe import __version__
from snakes_cafe.snakes_cafe import is_quit
from snakes_cafe.snakes_cafe import store_order


def test_version():
    assert __version__ == '0.1.0'


def test_is_quit_quits():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        is_quit("quit").will_exit_somewhere_down_the_stack()
    assert pytest_wrapped_e.type == SystemExit


def test_is_quit_does_not_quit():
    assert is_quit("Wings") == None


def test_store_order_existing_item():
    order_dictionary = {"Magic": 1}
    store_order(order_dictionary, "Magic")
    order_dictionary["Magic"] == 2


def test_store_order_new_item():
    order_dictionary = {"Apple": 1}
    store_order(order_dictionary, "Magic")
    order_dictionary["Magic"] == 1


def test_store_order_empty_list():
    order_dictionary = {}
    store_order(order_dictionary, "Magic")
    order_dictionary["Magic"] == 1
