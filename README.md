- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org05f21e5)
  - [Installation](#orgb688707)
    - [Prerequisites](#orgaa82d29)
    - [Linux](#org1fe6d1a)
    - [Windows](#orga1d04a2)
  - [Specifications](#orga100706)
    - [Scanner](#orge18e323)
    - [IDs](#org55a5a6f)
    - [Application](#org00de9af)



<a id="org05f21e5"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="orgb688707"></a>

## Installation


<a id="orgaa82d29"></a>

### Prerequisites

-   Python 3+
-   Make sure Python is configured for [TKinter](https://tkdocs.com/tutorial/install.html)


<a id="org1fe6d1a"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


<a id="orga1d04a2"></a>

### Windows

Using Python's shell, the Linux instructions should work perfectly


<a id="orga100706"></a>

## Specifications


<a id="orge18e323"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="org55a5a6f"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="org00de9af"></a>

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