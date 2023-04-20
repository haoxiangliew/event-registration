- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org5181d1c)
  - [Installation](#org12e29e7)
    - [Prerequisites](#org4975cd0)
    - [Linux](#org5e0accc)
    - [Windows](#orgdcd43e3)
    - [MacOS](#orga23afb8)
  - [Specifications](#org6158efb)
    - [Scanner](#org2f7fd54)
    - [IDs](#orgfc84881)
    - [Application](#orgb6b12e0)



<a id="org5181d1c"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org12e29e7"></a>

## Installation


<a id="org4975cd0"></a>

### Prerequisites

-   [Python 3+](https://www.python.org/downloads/)
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)
    -   Linux: Search your repositories for python-tk / tkinter
    -   Windows: Official Distribution
    -   MacOS: Official Distribution / `brew install python-tk` (Homebrew)


<a id="org5e0accc"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgdcd43e3"></a>

### Windows

```sh
python -m venv ./venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```


<a id="orga23afb8"></a>

### MacOS

Using the shell, the Linux instructions should work perfectly


<a id="org6158efb"></a>

## Specifications


<a id="org2f7fd54"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgfc84881"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgb6b12e0"></a>

### Application

1.  Dependencies

    ```sh
    openpyxl
    pandas
    tk
    ```
    
    -   Takes in `input.xlsx`, with the first-row as categories.
        -   Should have no duplicate ID and names.
    -   Filter input for scanner and manual input automatically.
    -   `tkinter` popups can be dismissed quickly with `<RET>`.