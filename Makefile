# Define variables.
PYTHON = python
PACKAGE_NAME = SDU-Haier-AQD-IEEEDataPort

# Default task(test).
test:
	$(PYTHON) -m unittest discover -s tests -v

# Default task(extract_img).
extract:
	$(PYTHON) datasetupload/extract_img.py

# Environment configuration.
install:
	conda env create -f environment.yml

# Clean up the project.
clean:
	rm -rf __pycache__ *.pyc *.pyo

# Print the help information.
help:
	@echo "Available tasks:"
	@echo "  test         : Run tests"
	@echo "  run          : Run the application"
	@echo "  extract	  : Run the extract image data"
	@echo "  install      : Install dependencies"
	@echo "  clean        : Clean up project"
	@echo "  help         : Show available tasks"

# Default task
.DEFAULT_GOAL := help
