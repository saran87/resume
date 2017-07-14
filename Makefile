all: output/resume.pdf output/resume.txt

files=output/resume.pdf resume.html output/resume.tex resume.yaml output/resume.txt

# TODO: use rsync
.PHONY: publish
publish: output/resume.pdf
	scp $(files) forge@sknadar.me:/home/forge/default/public/
	scp $(files) forge@sknadar.me:/home/forge/default/public/
	scp $(files) forge@sknadar.me:/home/forge/default/public/

output/resume.pdf: output/resume.tex res.cls
	/usr/local/texlive/2013/bin/universal-darwin/pdflatex -interaction=batchmode -output-directory output $<

output/resume.tex: templates/resume.tex.tmpl resume.yaml genresumes.py
	python genresumes.py tex

output/resume.txt: templates/resume.txt.tmpl resume.yaml genresumes.py
	python genresumes.py txt

.PHONY: clean
clean:
	rm -rf output
	rm -f *.pyc
