import subprocess
import sys
import time

def run_script(script_name):
    print(f"\nExecutando {script_name}...")
    try:
        subprocess.run([sys.executable, script_name], check=True)
        print(f"{script_name} executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {script_name}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_time = time.time()
    
    # Sequência de scripts para executar
    scripts = [
        "write.py",
        "swmm_parallel.py",
        "post.py"
    ]
    
    # Executa cada script na sequência
    for script in scripts:
        run_script(script)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTodos os scripts foram executados em {total_time:.2f} segundos")