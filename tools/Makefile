
UB_FOLDER ?= coptic-nt/unboundbible
ABBREV_INDEX ?= build/abbrev-index.csv
ABBREV_SOURCE_TSV ?= kjv/kjv.tsv

ALL_BUILDS = $(wildcard build/*)
ALL_UB_FOLDERS = $(wildcard $(UB_FOLDER)/*)

all: $(ALL_UB_FOLDERS:$(UB_FOLDER)/%=convert-%)

build:
	mkdir -p build

$(ABBREV_INDEX): build $(ABBREV_SOURCE_TSV)
	./build_abbreviation_index.py $(ABBREV_SOURCE_TSV) -o $(ABBREV_INDEX)

clean: $(ALL_BUILDS:build/%=clean-%)

clean-%:
	rm -f build/$*

convert-%: $(ABBREV_INDEX)
	./to_tsv.py $(UB_FOLDER)/$* build --abbreviation-index=$(ABBREV_INDEX)

.PHONY: all  convert-%
