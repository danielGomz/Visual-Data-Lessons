#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = visual-data-lessons
PYTHON_VERSION = 3.8
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install --upgrade pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using ruff and black (use `make format` to do formatting)
.PHONY: lint
lint:
	ruff check .
	isort --check --diff scenes
	black --check --config pyproject.toml scenes

## Format source code with black
.PHONY: format
format:
	isort scenes
	black --config pyproject.toml scenes

## Set up Python environment
.PHONY: create_environment
create_environment:
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	@echo ">>> Conda environment created. Activate with:\nconda activate $(PROJECT_NAME)"

## Render a specific scene file
.PHONY: render
render:
	@echo "Rendering scene file: $(FILE)"
	$(PYTHON_INTERPRETER) -m manim $(FILE) --renderer=opengl -pqh

## Render all scenes in a specific folder (e.g., project1 or common)
.PHONY: render-all
render-all:
	@echo "Rendering all scenes in folder: $(FOLDER)"
	find scenes/$(FOLDER) -name "*.py" | xargs -I {} $(PYTHON_INTERPRETER) -m manim {} -pqh


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
