PYTHON = python3
SOURCE = shiritori.py
CACHE = __pycache__/
RM = rm -rf

all : run clean

run:
	@$(PYTHON) $(SOURCE)

clean:
	@$(RM) $(CACHE)