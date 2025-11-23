import subprocess
import sys

def test_addsub():
    # Run the addsub.py program with arguments 10 and 5
    result = subprocess.run(
        [sys.executable, "addsub.py", "10", "5"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    # Expected outputs
    assert "Addition: 15.0" in output
    assert "Subtraction: 5.0" in output