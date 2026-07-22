# Noah Tah

## 7/22/2026

## Programming Capstone

## Evan Vaverka

## Northwestern Oklahoma State Univserity

## Notes that I need to make

1. Thought processes
2. Solution itself
3. Issues that I run into
4. Timeframes I work or think about the problem
5. Resources or websites I look into to solve the problem
6. Insight into the process of working through the problem

## When I submit the code file, also copy and paste into a text file to be uploaded alongside the code file

"A company named, Fancy Names, specializes in using artists and technology to take a client's submitted name and then making artistic signage of that name, out of a range of materials.
They have a singular store where a customer can make a purchase to pick up later or an order can be placed online.
Online orders have to be paid for in advance but in store orders can be paid for at pick up.
The production of the product happens at a different location called Art Factory and then is either shipped to the client or over to the store.
Fancy names already has a successful system for taking orders and keeping client information stored for use. The problem they want you to solve comes from the report the system creates that gets sent to Art Factory.
It pulls all order names to be created, the material type, and shipping information into a single excel document that is emailed over to Art Factory. This slows production down because someone has to open the document and sort the information.
Fancy Names wants a program that when fed this file, it breaks the info up appropriately.
After being broken down it prints the info to a new excel document.
An example file has been attached.
The file contains 3 columns of information. The first column contains the names to be created by the artists. It can come in 5 possible forms.
These names need to be broken into many pieces as possible if possible.
a space between parts of the name is where it would be broken apart. Evan Vaverka would become Evan in one column and Vaverka in a seperate column.

- Evan Vaverka
- Evan Patrick Vaverka
- Evan
- E. Vaverka
- Evan V.

The second column contains the material the name will be created with and the third column contains whether it is return to store "Store" or "Shipped" from Art Factory.
     - I am assuming that return to store means being shipped to "Store" which will be implied with the "Store" label.
While this information does not need to be manipulated it is important to have in the new document so Art Factory can sue it for production and shipping, instead of having to look at 2 seperate documents
Fancy Names would like the document sorted by one of the columns of information so that there is some order to the document when it is looked at.

## Most useful resources for using Python

- pandas

     1. reads excel files

     2. manipulates columns, sorting
     3. writes back to Excel file

## Documentation and resources

     - https://pandas.pydata.org/docs/user_guide/io.html#excel-files
     - https://pandas.pydata.org/docs/user_guide/text.html 
     - https://docs.python.org/3/library/pathlib.html#pathlib.Path
     - https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html
     - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

## Log of things done

## 6/1/2026

- Started writing things down in Project Notes.

- Decided that I would use Python for simplicity.

## 6/11/2026

- Created a virtual environment on my WSL-Ubuntu so that I can install pandas without affecting my global python configuration

- This was something that I am not really used to because I mostly did C flavored stuff and javascript, so was a bit confusing.

```bash
sudo apt install python3.14-venv # This was to install the virtual environment package
python3 -m venv venv # create the virtual environment
source venv/bin/activate # activate the virtual environment
pip install <package-name> # this is the syntax for installing things into the virtual environment
# or conversely
pip install -r requirements.txt # this will install all dependencies listed in requirements.txt
deactivate # deactivate the virtual environment when done
```

- pip installed pandas now to use it

07-16-2026

- Had to install the packages on my laptop so that I can work on the project on that machine

## 7/17/2026

- Now lists all files in the data directory for the user to select

```python
DATA_DIR = Path(__file__).resolve().parent / "data"


def list_data_files():
    files = sorted([path for path in DATA_DIR.iterdir() if path.is_file()])
    if not files:
        raise FileNotFoundError(f"No files were found in {DATA_DIR}")
    return files
```

- I decided to add the feature of listing the directories as an exercise because I wanted it to be a more interactive program and that just made sense to me

## Code breakdown of listing all files in specified directory

```python
DATA_DIR = Path(__file__).resolve().parent / "data"
files = sorted([path for path in DATA_DIR.iterdir() if path.is_file()])
```

- `Path(__file**__).resolve().parent / "data"**`

- `Path(__file__)`
        - `__file__` is a special built in variable that python uses to set the path of the current directory, pointing to the script being executed
        - `Path()`
            - Path comes from `pathlib`. We wrap the current working directory in a path object that makes it convenient to work with paths across platforms

- `.resolve()`
        - resolve converts the path into an absolute path if it wasn’t already, guaranteeing more consistent results

- `.parent`
        - takes the path that is pointing at the script, and goes up a level to the directory containing the script

- `sorted()`
          - Takes an iterable , and returns a list with the items in a sorted order- for Path objects it sorts the alphabetically by their string representation

- `DATA_DIR.iterdir()`
          - Returns an iterator over all the entries in the directory, but does not delve into subfolders.
          - Apparently, an iterator is an object that sort of lazy loads the items from the directory. It knows how to fetch the items, but does not store them in memory at the time of inception.

- `path.is_file()`
          - returns `True` if it points to a regular file, and `False` if it is a directory, a symlink, or does not exist

## 7/18/2026

- In the first column we need to clean the names that are contained in it
- Some of the names are smushed together so we have iterate over each character in the names, and we should detect for a capital letter that is contained in the middle of a string before a space. That should let us know that the last name has began before a space has been placed, and a space should be inserted before the capital letter for correction.

```python
  cleaned_name = re.sub(r"(?<=[a-z])([A-Z])", r" \1", name)
```

- This is the important regex that took care of a lot of the heavy lfiting in the first column

- This searches for an uppercase letter that comes after a lowercase letter, then it puts a space behind it.

- The problem is that there are edge cases like in some names like McMahan which will separate unintentionally.

- The solution I found is that you have a list of common prefixes and then when regex finds these it will exit out of the replacement.

```python

cleaned_name = re.sub(r"(?<=[a-z])([A-Z])", r" \1", name)

for prefix in PREFIXES:
     cleaned_name = re.sub(rf"({re.escape(prefix)})\s+([A-Z])", r"\1\2", cleaned_name)
```

- `re.sub()`
          - find parts of the string that match a pattern and replace them with something else
          - This is inserting a space before capital letters.
- `(?<=[a-z])`
          - checks the character before the current posistion
          - character before this must be a lowercase letter
- `([A-Z])`
          - Matches an uppercase letter
          - Captures it for reuse

## 7/20/2026

- Today realized i misunderstood the specificiations of the assignment, and instead of separating the columns of information I was cleaning the data. That is fine though because I can keep that code as a preprocessing step for a better solution.

## 7/21/2026

- Split names into 3 parts, FIRST, MIDDLE, LAST

- If the name does not have one of the parts, N/A will be added in that column.

- Since every name has a first name and a last name, if there are only 2 names in the original column, we will assume it is a first and a last name, and if there are three we will assume the second item is the middle name.

## 7/22/2026 - Final

- This function does a ton of the heavy lifting

```python
def split_names_column(df):
    if df.empty or df.shape[1] == 0:
        return df

    result_df = df.copy()
    first_column = result_df.columns[0]
    cleaned_names = result_df[first_column].apply(fix_names_column)
    split_names = cleaned_names.apply(split_name)

    first_names = []
    middle_names = []
    last_names = []

    for parts in split_names:
        if not parts:
            first_names.append("N/A")
            middle_names.append("N/A")
            last_names.append("N/A")
        elif len(parts) == 1:
            first_names.append(parts[0])
            middle_names.append("N/A")
            last_names.append("N/A")
        elif len(parts) == 2:
            first_names.append(parts[0])
            middle_names.append("N/A")
            last_names.append(parts[1])
        else:
            first_names.append(parts[0])
            middle_names.append(" ".join(parts[1:-1]))
            last_names.append(parts[-1])

    name_columns = pd.DataFrame({
        "First": first_names,
        "Middle": middle_names,
        "Last": last_names,
    })

    remaining_columns = result_df.drop(columns=[first_column])
    return pd.concat([name_columns, remaining_columns], axis=1)
```

- `first_column = result_df.columns[0]`

          - We grab the first column of the DataFrame which at this point in the program, they have been cleaned with our previous regex magic

- `split_names = cleaned_names.apply(split_name)`

          - Here we are applying a function we created to split the names at the spaces and return them

- `for parts in split_names:`

          - This part has some interesting logic built into the if statements, it assumes that if the name only has two parts, it is a first and last name, and only if it has 3 parts will it add the middle name.

- For this assignment I am happy with the program, if I was to expand it in the future I would handle more sorting capabilities or maybe different output formats. This would also be interesting to hook up to a web page and handle the interface with that instead of the command line.
