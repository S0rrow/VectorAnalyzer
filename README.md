# Vector Analyzer
- This is a Python project for analyzing the Change Information Vectors used as pool in [SimilarPatchIdentifier](https://github.com/ISEL-HGU/SimilarPatchIdentifier)

## Components
### main.py
- it shows metadata of the dataset. it specifically target `gumtree_vector.csv` file.
    - `main.py` shows max, min, average, median, and standard deviation for length of each vectors within the dataset.
- to launch the program, run `python main.py`

### extractor.py
- given hash id of commit and file, it return the diff of the source codes from github.
- it specifically target `input.txt` file.
    - format = hash1, hash2, file1, file2, github_url, jira_key
    - the result is extracted as `diff.txt` file.
- to launch the program, run `python extractor.py`
