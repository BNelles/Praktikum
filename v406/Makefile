all: build/v406.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
build/plot1.pdf:plot1.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot1.py
build/plot2.pdf:plot2.py ../matplotlibrc ../header-matplotlib.tex | build





	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot2.py
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc








# hier weitere Abhängigkeiten für build/v406.pdf deklarieren:
build/v406.pdf: build/plot.pdf build/plot1.pdf	build/plot2.pdf

build/v406.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v406.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
