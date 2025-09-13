import subprocess

def test_run_app():
    # run app.py as a separate process
    result = subprocess.run(
        ["python", "app.py"], capture_output=True, text=True
    )
    print("Output:\n", result.stdout)

if __name__ == "__main__":
    test_run_app()
