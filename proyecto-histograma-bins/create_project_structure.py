import os

# Define the base path for your project
base_path = "/Users/alexandersandoval/Documents/GitHub/TableauProjects/proyecto-histograma-bins"

# Define the folder structure
folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "scripts",
    "notebooks",
    "outputs/graphs",
    "outputs/reports",
    "config"
]

# Define the files to create
files = {
    "requirements.txt": "",
    "README.md": "# Proyecto Histograma Bins - Tableau",
    "config/config.yaml": "# Aquí guarda la API key y configuraciones"
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files
for file_name, file_content in files.items():
    with open(os.path.join(base_path, file_name), 'w') as file:
        file.write(file_content)

print("Estructura de proyecto creada exitosamente.")
