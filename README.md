#####
README

Last updated: 2018-11-22
by @rdkm
#####

~ Folder contents ~

This folder contains all of the files relevant to the Richard Brome network analysis project.

The sub-folders are structured as follows:

	metrics
		\_ whole_network_metrics_by_play.csv
		\_ word_counts_by_character.csv

	network_data
		\_ character_lists
		\_ edgelists
		\_ gephi_files

	plays
		\_ plays_with_filenames.csv
		\_ texts
			\_ full_xml
			\_ split_on_character

	quick_viz
		\_ images
		\_ index.html

	scripts
		\_ BromeExtraction+WordCount.py


~ Notes ~

1.

The file word_counts.csv contains word counts for all characters across all of the plays. Due to the messiness of the TEI markup of the plays, there may be some errors. These means that character names will need to be manually inspected for overlaps and misspellings, etc.

This also means that some numbers may need to be added together to provide more accurate figures. However, the overall difference across the data_ should be negligible.

2.

The quick_viz.html works in Chrome and Firefox; I haven’t tested other browsers. I recommend Chrome.

~rdkm
