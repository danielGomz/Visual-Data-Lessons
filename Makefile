#################################################################################
# PROJECT
#################################################################################

PROJECT_NAME = visual-data-lessons

#################################################################################
# ENVIRONMENT
#################################################################################

.PHONY: install
install:
	@echo "📦✨ Installing project dependencies..."
	@echo "🔄 Syncing with uv..."
	@uv sync --all-groups
	@echo "✅ Environment ready to go 🚀"

#################################################################################
# CODE QUALITY
#################################################################################

.PHONY: lint
lint:
	@echo "🕵️‍♂️ Running Ruff lint check..."
	@uv run ruff check .
	@echo "📋 Lint process finished."

.PHONY: format
format:
	@echo "🎨✨ Formatting code with ruff..."
	@uv run ruff format .
	@echo "✅ Format complete. Code looking sharp 😎"

#################################################################################
# DEVELOPMENT
#################################################################################

## Production quality (1080p) - Landscape
.PHONY: render
render:
	@echo "🌄🎬 Rendering in Landscape mode (16:9)..."
	@echo "🔧 Quality: 1080p (-pqh)"
	@uv run manim $(FILE) $(SCENE) -pqh
	@echo "✅ Landscape render complete 🚀"

## Production quality (1080p) - Portrait
.PHONY: portrait
portrait:
	@echo "📱✨ Rendering in Portrait mode (9:16)..."
	@echo "🔧 Quality: 1080p (-pqh)"
	@uv run manim $(FILE) $(SCENE) -pqh -- --portrait
	@echo "✅ Portrait render complete 🚀"

#################################################################################
# CLEAN
#################################################################################

.PHONY: clean
clean:
	@echo "🧹 Cleaning Python cache..."
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +

	@echo "🧹 Removing build artifacts..."
	@rm -rf *.egg-info
	@rm -rf src/*.egg-info

	@echo "🧹 Removing Manim media..."
	@rm -rf media

	@echo "✅ Clean complete."
