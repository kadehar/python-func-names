import pytest

from print_function import print_info_about as info


def open_browser(url="https://google.com"):
    pass


def go_to_companyname_homepage(login="1223", password="abcd"):
    pass


def find_registration_button_on_login_page():
    pass


@pytest.mark.parametrize(
    "func",
    [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]
)
def test_print_info(func):
    info(func)
