- [[event-registration](https://github.com/haoxiangliew/event-registration)](#orgcefca26)
  - [Installation](#org08bec4f)
    - [Linux](#orga429fa6)
    - [Windows](#orgd186d26)
  - [Specifications](#orgd34d56d)
    - [Scanner](#org30658c1)
    - [IDs](#orgc9cedd3)
    - [Application](#orgea209c9)



<a id="orgcefca26"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org08bec4f"></a>

## Installation


<a id="orga429fa6"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgd186d26"></a>

### Windows

-   TODO
-   Or use WSL


<a id="orgd34d56d"></a>

## Specifications


<a id="org30658c1"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;<"9-digit ID">=0249?
            
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgc9cedd3"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgea209c9"></a>

### Application

1.  Dependencies

    ```sh
    openpyxl
    pandas
    tkinter
    ```
    
    -   Takes in `input.xlsx`, with the first-row as categories.
        -   Should have no duplicate ID and names.
    -   Filter input for scanner and manual input automatically.
    -   `tkinter` popups can be dismissed quickly with `<RET>`.