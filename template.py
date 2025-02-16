from pathlib import Path
import os 

main_folder = "cnnProject"


liat_of_paths = [
    f"{main_folder}/__init__.py",
    f"{main_folder}/components/__init__.py",
    f"{main_folder}/components/data_ingestion.py",
    f"{main_folder}/components/prepare_base_model.py",
    f"{main_folder}/components/model_trainer.py",
    f"{main_folder}/components/model_evaluation.py",
    f"{main_folder}/Pipeline/__init__.py",
    f"{main_folder}/Pipeline/Stages_of_Pipeline.py",
    f"{main_folder}/config/__init__.py",
    f"{main_folder}/config/config_entity.py",
    f"{main_folder}/utils/__init__.py",
    f"{main_folder}/utils/common.py",
    "app.py",
    "main.py",
    "params.ymal",
    "requirements.txt",
    "setup.py"
]

for path in liat_of_paths:
    file_path = Path(path)
    folder = file_path.parent
    os.makedirs(folder,exist_ok=True)
    
    if not file_path.exists():
        file_path.touch(exist_ok=True)
    