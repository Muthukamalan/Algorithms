.PHONY: run
run:
	@python -m cmd.playground.main


.PHONY: clean
clean:
	@find . -type d -name "__pycache__" -o -name ".ruff_cache" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete