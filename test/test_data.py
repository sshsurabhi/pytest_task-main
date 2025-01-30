import os

from src.section_data import DataStructureDemo, format_string


def test_add_item():
    """
    SPECIFICATION: add_item shall create a backup of 'items', which is then
    available under 'items_backup'

    ASSUMPTION: implementation is wrong and the backup is not created correctly
    TASK: patch the implementation
    HINT: special behavior of python dict/list
    """
    demo = DataStructureDemo()
    demo.add_item(1)
    assert len(demo.items) > len(demo.items_backup)


def test_set_item():
    """
    SPECIFICATION: 'set_item' shall set the given key-value-pair to 'data'.

    ASSUMPTION: test is correct
    TASK: patch the implementation
    """
    demo = DataStructureDemo()
    demo.set_item("example", 22)
    assert demo.data["example"] == 22

# TODO: make this parametrized?
def test_transform_items():
    """
    SPECIFICATION: 'transform_items' shall return a subsection of
    the upper characters of 'items'

    ASSUMPTION: test is wrong
    TASK: patch the test
    """
    demo = DataStructureDemo(items=["a", "b", "c", "d"])
    result = demo.transform_items(start_index=2)
    assert result == ["C", "D"]

def test_string_formatting():
    """
    SPECIFICATION: 'format_string' returns an identical string,
    once formatted using %-formatting, once using f-string-formatting

    ASSUMPTION: assume the test is correct
    TASK: patch the implementation
    """
    old_style, new_style = format_string("John", 30)
    assert old_style == "Name: John, Age: 30"
    assert new_style == "Name: John, Age: 30"

def test_get_evaluation():
    """
    SPECIFICATION: 'get_evaluation' shall return
    - 'Large' for values > 100
    - 'Negative' for values <= 0
    - 'Normal' for values inbetween

    ASSUMPTION: assume the test is correct
    TASK: patch the implementation
    """
    demo = DataStructureDemo()
    assert demo.get_evaluation(150) == "Large"
    assert demo.get_evaluation(0) == "Negative"
    assert demo.get_evaluation(50) == "Normal"

def test_get_evaluation_2():
    """
    ASSUMPTION:
    - implementation is correct
    - test is poorly defined

    TASK: explain why the test is failing
    HINT: special behavior of python class attributes
    """
    demo_1 = DataStructureDemo()
    demo_2 = DataStructureDemo()

    assert demo_1.get_evaluation(102) == "Large"
    assert demo_2.get_evaluation(102) == "Large"

    demo_1.BOUNDARY_HIGH = 103
    assert demo_1.get_evaluation(102) == "Normal"
    assert demo_2.get_evaluation(102) == "Large"

    DataStructureDemo.BOUNDARY_HIGH = 103
    assert demo_1.get_evaluation(102) == "Normal"
    assert demo_2.get_evaluation(102) == "Normal"

def test_file_operations(tmp_path):
    """
    SPECIFICATION: 'write_data' and 'read_data' shall lead
    to unmodified data

    ASSUMPTION: assume the test is correct
    TASK:  patch the implementation
    """
    demo = DataStructureDemo()
    filepath = tmp_path / "test.json"
    testdata = {"testkey": "testvalue"}
    demo.data.update(testdata)
    demo.write_data(filepath)
    demo.read_data(filepath)
    assert demo.data == testdata
