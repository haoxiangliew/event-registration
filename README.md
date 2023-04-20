- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org6889541)
  - [Installation](#orgc95615f)
    - [Prerequisites](#orga79f1ae)
    - [Linux](#org7eee04e)
    - [Windows](#org85681e9)
    - [MacOS](#org6b56557)
  - [Specifications](#orgd154535)
    - [Scanner](#org4040211)
    - [IDs](#orgd3662e5)
    - [Application](#org5b70b51)



<a id="org6889541"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="orgc95615f"></a>

## Installation


<a id="orga79f1ae"></a>

### Prerequisites

-   [Python 3+](https://www.python.org/downloads/)
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)
    -   Linux: Search your repositories for python-tk / tkinter
    -   Windows: Official Distribution
    -   MacOS: Official Distribution / `brew install python-tk` (Homebrew)


<a id="org7eee04e"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


<a id="org85681e9"></a>

### Windows

```sh
python -m venv ./venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```


<a id="org6b56557"></a>

### MacOS

Using the shell, the Linux instructions should work perfectly


<a id="orgd154535"></a>

## Specifications


<a id="org4040211"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;"9-digit ID"=0249?
            "\n"
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgd3662e5"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="org5b70b51"></a>

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