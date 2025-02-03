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
	isort --check --diff visual_data_lessons
	black --check --config pyproject.toml visual_data_lessons

## Format source code with black
.PHONY: format
format:
	isort visual_data_lessons
	black --config pyproject.toml visual_data_lessons

## Set up Python environment
.PHONY: create_environment
create_environment:
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION) -y
	@echo ">>> Conda environment created. Activate with:\nconda activate $(PROJECT_NAME)"

## Render a specific scene file in horizontal format
.PHONY: render-horizontal
render-horizontal:
	@echo "Rendering scene file: $(FILE) in HORIZONTAL format"
	$(PYTHON_INTERPRETER) -m manim $(FILE) -pqh --config_file visual_data_lessons/config/config_horizontal.cfg


## Render a specific scene file in vertical format
.PHONY: render-vertical
render-vertical:
	@echo "Rendering scene file: $(FILE) in VERTICAL format"
	$(PYTHON_INTERPRETER) -m manim $(FILE) -p --config_file visual_data_lessons/config/config_vertical.cfg

## Render all visual_data_lessons in a specific folder (e.g., project1 or common)
.PHONY: render-all
render-all:
	@echo "Rendering all visual_data_lessons in folder: $(FOLDER)"
	find visual_data_lessons/$(FOLDER) -name "*.py" | xargs -I {} $(PYTHON_INTERPRETER) -m manim {} -pqh


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
