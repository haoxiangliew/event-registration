- [[event-registration](https://github.com/haoxiangliew/event-registration)](#orge98b1c8)
  - [Installation](#org816962e)
    - [Prerequisites](#org51281bb)
    - [Linux](#org9e57bde)
    - [Windows](#orgcafe6e4)
    - [MacOS](#org082d6cb)
  - [Specifications](#orgcafd44d)
    - [Scanner](#orgb0811fa)
    - [IDs](#orgfb24464)
    - [Application](#orgf674a9c)



<a id="orge98b1c8"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org816962e"></a>

## Installation


<a id="org51281bb"></a>

### Prerequisites

-   Python 3+
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)
    -   Linux: Search your repositories for python-tk / tkinter
    -   Windows: Official Distribution
    -   MacOS: Official Distribution / `brew install python-tk` (Homebrew)


<a id="org9e57bde"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgcafe6e4"></a>

### Windows

Using Python's shell, the Linux instructions should work perfectly


<a id="org082d6cb"></a>

### MacOS

Same as above


<a id="orgcafd44d"></a>

## Specifications


<a id="orgb0811fa"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgfb24464"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgf674a9c"></a>

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