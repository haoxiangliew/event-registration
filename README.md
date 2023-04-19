- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org3f11ae5)
  - [Installation](#org7cef0c3)
    - [Linux](#orgd6cdeef)
    - [Windows](#orgec78992)
  - [Specifications](#org3d9b343)
    - [Scanner](#orgf8b7c9f)
    - [IDs](#org23ebe69)
    - [Application](#org3bb26c9)



<a id="org3f11ae5"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org7cef0c3"></a>

## Installation


<a id="orgd6cdeef"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgec78992"></a>

### Windows

Using Python's shell, the Linux instructions should work perfectly


<a id="org3d9b343"></a>

## Specifications


<a id="orgf8b7c9f"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="org23ebe69"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="org3bb26c9"></a>

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