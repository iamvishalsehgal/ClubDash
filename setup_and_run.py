import os
import sys
import subprocess
import platform

def install_virtualenv():
    try:
        import virtualenv
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'virtualenv'])

def create_virtualenv():
    subprocess.check_call([sys.executable, '-m', 'virtualenv', 'venv'])

def activate_virtualenv():
    if platform.system() == 'Windows':
        activate_script = os.path.join('venv', 'Scripts', 'activate_this.py')
    else:
        activate_script = os.path.join('venv', 'bin', 'activate_this.py')
    
    with open(activate_script) as file_:
        exec(file_.read(), dict(__file__=activate_script))

def install_requirements():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        print("Attempting to resolve dependency conflicts...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--use-deprecated=legacy-resolver', '-r', 'requirements.txt'])

def install_jupyter():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jupyter'])

def run_jupyter():
    try:
        if platform.system() == 'Windows':
            jupyter_executable = os.path.join('venv', 'Scripts', 'jupyter.exe')
        else:
            jupyter_executable = os.path.join('venv', 'bin', 'jupyter')
        
        subprocess.check_call([jupyter_executable, 'notebook', 'dash.ipynb'])
    except subprocess.CalledProcessError as e:
        print(f"Error running Jupyter Notebook: {e}")
        print("Make sure Jupyter is installed and available in the virtual environment.")

def main():
    install_virtualenv()
    create_virtualenv()
    activate_virtualenv()
    install_requirements()
    install_jupyter()
    run_jupyter()

if __name__ == '__main__':
    main()
