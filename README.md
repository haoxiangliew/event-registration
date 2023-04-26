- [[event-registration](https://github.com/haoxiangliew/event-registration)](#orgc8e4200)
  - [Installation](#orgb11c843)
    - [Prerequisites](#orgf6621bd)
    - [Linux](#orgb8c03e1)
    - [Windows](#orga45d3ce)
    - [MacOS](#org07b766e)
  - [Specifications](#org0adc5ed)
    - [Scanner](#orgeb9ea08)
    - [IDs](#orgd6a42cc)
    - [Application](#orgab15916)



<a id="orgc8e4200"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="orgb11c843"></a>

## Installation


<a id="orgf6621bd"></a>

### Prerequisites

-   [Python 3+](https://www.python.org/downloads/)
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)
    -   Linux: Search your repositories for python-tk / tkinter
    -   Windows: Official Distribution
    -   MacOS: Official Distribution / `brew install python-tk` (Homebrew)


<a id="orgb8c03e1"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py / main-gui.py
```


<a id="orga45d3ce"></a>

### Windows

```sh
python -m venv ./venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py / main-gui.py
```


<a id="org07b766e"></a>

### MacOS

Using the shell, the Linux instructions should work perfectly


<a id="org0adc5ed"></a>

## Specifications


<a id="orgeb9ea08"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;"9-digit ID"=0249?
            "\n"
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgd6a42cc"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgab15916"></a>

### Application

-   Dependencies

```sh
openpyxl
pandas
tk
```

-   `main-gui.py` is a GUI application (additionally requires `ttkthemes`).
    -   Feel free to remove that dependency for `main.py`, the CLI app.
-   Takes in `input.xlsx`, with the first-row as categories.
    -   Should have no duplicate ID and names.
-   Filter input for scanner and manual input automatically.
-   `tkinter` popups can be dismissed quickly with `<RET>`.