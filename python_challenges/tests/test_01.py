from src.one_swap import swap
import sys, io

def test_swap():
    var1 = 7
    var2 = 2

    # Capture standard output to check the printed values
    captured_output = io.StringIO()
    sys.stdout = captured_output

    swap(var1, var2)

    # Reset redirect.
    sys.stdout = sys.__stdout__

    # Get the printed values
    printed_values = captured_output.getvalue().splitlines()

    # Assert that the function printed the correct values
    assert printed_values == [str(var1) + " " + str(var2), str(var2) + " " \
        + str(var1)]

# Additional tests can be added based on different input scenarios
