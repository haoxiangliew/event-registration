- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org8660349)
  - [Installation](#org6b40b75)
    - [Prerequisites](#orgd4fbd8a)
    - [Linux](#orgf9c9234)
    - [Windows](#orge4ffd1f)
    - [MacOS](#orge809ecd)
  - [Specifications](#orga554bd4)
    - [Scanner](#orgf1552aa)
    - [IDs](#orgf4467c8)
    - [Application](#org071dbac)



<a id="org8660349"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org6b40b75"></a>

## Installation


<a id="orgd4fbd8a"></a>

### Prerequisites

-   [Python 3+](https://www.python.org/downloads/)
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)
    -   Linux: Search your repositories for python-tk / tkinter
    -   Windows: Official Distribution
    -   MacOS: Official Distribution / `brew install python-tk` (Homebrew)


<a id="orgf9c9234"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main-gui.py / main.py
```


<a id="orge4ffd1f"></a>

### Windows

```sh
python -m venv ./venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main-gui.py / main.py
```


<a id="orge809ecd"></a>

### MacOS

Using the shell, the Linux instructions should work perfectly


<a id="orga554bd4"></a>

## Specifications


<a id="orgf1552aa"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;"9-digit ID"=0249?
            "\n"
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgf4467c8"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="org071dbac"></a>

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