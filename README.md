- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org09c580a)
  - [Installation](#org2bf55e7)
    - [Linux](#orga5de071)
    - [Windows](#orgffc2346)
  - [Specifications](#org799ffd3)
    - [Scanner](#orga216c0c)
    - [IDs](#orge8a2585)
    - [Application](#orgac2aa6b)



<a id="org09c580a"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org2bf55e7"></a>

## Installation


<a id="orga5de071"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgffc2346"></a>

### Windows

-   TODO
-   Or use WSL


<a id="org799ffd3"></a>

## Specifications


<a id="orga216c0c"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orge8a2585"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgac2aa6b"></a>

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