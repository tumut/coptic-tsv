
UB_FOLDER ?= coptic-nt/unboundbible
ABBREV_INDEX ?= bin/abbrev-index.csv
ABBREV_SOURCE_TSV ?= kjv/kjv.tsv

ALL_UB_FOLDERS = $(wildcard $(UB_FOLDER)/*)

.DEFAULT_GOAL = build

bin:
	mkdir -p bin

$(ABBREV_INDEX): bin $(ABBREV_SOURCE_TSV)
	./build_abbreviation_index.py $(ABBREV_SOURCE_TSV) -o $(ABBREV_INDEX)

.PHONY: build
build: $(ALL_UB_FOLDERS:$(UB_FOLDER)/%=build-%)

.PHONY: build-%
build-%: $(ABBREV_INDEX)
	./to_tsv.py $(UB_FOLDER)/$* bin --abbreviation-index=$(ABBREV_INDEX)

.PHONY: clean
clean:
	rm -f bin/*

.PHONY: clean-%
clean-%: bin/%.tsv
	rm -f bin/$*.tsv
