- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org456ef46)
  - [Installation](#orgd09eb68)
    - [Prerequisites](#orga9971f3)
    - [Linux](#org7774733)
    - [Windows](#org915e3c7)
    - [MacOS](#orgf12b857)
  - [Specifications](#org70e5574)
    - [Scanner](#orgc2daa0b)
    - [IDs](#org37dbf37)
    - [Application](#orgba89501)



<a id="org456ef46"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="orgd09eb68"></a>

## Installation


<a id="orga9971f3"></a>

### Prerequisites

-   [Python 3+](https://www.python.org/downloads/)
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)
    -   Linux: Search your repositories for python-tk / tkinter
    -   Windows: Official Distribution
    -   MacOS: Official Distribution / `brew install python-tk` (Homebrew)


<a id="org7774733"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


<a id="org915e3c7"></a>

### Windows

Using Python's shell, the Linux instructions should work perfectly


<a id="orgf12b857"></a>

### MacOS

Same as above


<a id="org70e5574"></a>

## Specifications


<a id="orgc2daa0b"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="org37dbf37"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgba89501"></a>

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