from Tests.crud_test import test_add_object, test_get_by_id, test_delete_object, test_modify_object
from Tests.domain_test import test_object
from Tests.functions_test import test_sum, test_ascending_order, test_max_price, test_concat_str, test_move_object


def run_all():
    test_object()
    test_add_object()
    test_get_by_id()
    test_delete_object()
    test_modify_object()
    test_move_object()
    test_concat_str()
    test_max_price()
    test_ascending_order()
    test_sum()