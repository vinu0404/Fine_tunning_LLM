import nbformat

input_file = "Fine_tune_Llama_2.ipynb"
output_file = "Fine_tune_Llama_2_fixed.ipynb"

# Read the notebook safely with UTF-8 encoding
with open(input_file, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove widget metadata if it exists
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]
    print("Removed 'widgets' metadata from notebook.")

with open(output_file, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Cleaned notebook saved as: {output_file}")
