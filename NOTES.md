### `os` module

This is Python's standard interface to the operating system. It can be used to list files, create/remove directories, join paths. It also has path utilities via `os.path`.

#### Core `os` functions

1. `os.listdir(path)` -> list names of directory (e.g., `print(os.listdir('.')) # shows files in current folder`)
2. `os.makedirs(path, exist_ok=True)` -> create directories recursively
3. `os.remove(path)` -> delete a file
4. `os.rmdir(path)` -> remove an empty directory
5. `os.rename(src, dst)` -> rename/move a file or directory

#### Path handling (via `os.path`)

1. `os.path.exists(path)` -> checks if a path exists
   os.path.
2. `os.path.join(a, b, ...)` -> safely combine path parts
3. `os.path.isfile(path)` -> check if path is a file
4. `os.path.isdir(path)` -> check if path is a directory
5. `os.path.basename(path)` -> filename part only
6. `os.path.dirname(path)` -> directory part only
7. `os.path.abspath(path)` -> absolute path version (e.g. `print(os.path.abspath("x)) # prints the full path to 'x'`)

#### Process / environment

1. `os.getcwd()` -> current working directory (e.g., `print(os.getcwd())`)
2. `os.chdir(path)` -> change working directory.
3. `os.environ` -> directory of environment variables.

### String methods

There are a number of built-in string methods that are part of Python's `str` type. `str` is the class (blueprint) and instances of `str` can access these methods.

#### Checks

1. `.startswith(prefix)` -> does the string start with a prefix?
2. `.endswith(suffix)` -> does the string end with a suffix?
3. `.isdigit()` -> only digits?
4. `.isalpha()` -> only letters?
5. `.isalnum()` -> letters or digits?
6. `isspace()` -> only whitespace?
7. `islower()` / `.isupper() -> all lower/upper case?

#### Transformations

1. `.lower()` / `.upper()` -> change case
2. `.strip()` -> remove whitespace from both ends
3. `.lstrip()` / `.rstrip` -> left/right strip
4. `.replace(old, new)` -> replace substrings

#### Splitting & joining

1. `.split()` -> split string into list by whitespace or a given separator
2. `.splitlines()` -> split by line breaks
3. `.join(list_of_strings)` -> join into one string with a separator

#### Finding

1. `.find(sub)` -> index of first occurence (or -1)
2. `.rfind(sub)` -> index of last occurence (or -1)
3. `.count(sub)` -> number of times substring appears

### String module

This one contains predefined constants and helpers for working with texts, such as:

- `string.ascii_letters` -> "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
- `string.ascii_lowercase` -> "abcdefghijklmnopqrstuvwxyz"
- `string.ascii_uppercase` -> "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
- `string.digits` -> "0123456789"
- `string.hexdigits` -> "0123456789abcdefABCDEF"
- `string.octdigits` -> "01234567"
- `string.punctuation` -> all common punctuation characters
- `string.whitespace` -> space, tab, newline, etc.
- `string.capwords(s)` -> Capitalizes each word in a string
