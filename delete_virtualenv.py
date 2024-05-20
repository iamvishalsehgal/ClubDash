import os
import shutil

def delete_virtualenv():
    if os.path.exists('venv'):
        shutil.rmtree('venv')
        print("Virtual environment 'venv' deleted successfully.")
    else:
        print("Virtual environment 'venv' does not exist.")

if __name__ == '__main__':
    delete_virtualenv()
