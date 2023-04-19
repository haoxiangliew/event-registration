- [[event-registration](https://github.com/haoxiangliew/event-registration)](#orgf3c0500)
  - [Specifications](#orga926d4f)
    - [Scanner](#org6b461f8)
    - [IDs](#orgcae1dd5)
    - [Application](#orgb9b7292)
  - [Installation](#orgb4960e4)



<a id="orgf3c0500"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.


<a id="orga926d4f"></a>

## Specifications


<a id="org6b461f8"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;<"9-digit ID">=0249?
            
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgcae1dd5"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgb9b7292"></a>

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


<a id="orgb4960e4"></a>

## Installation

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```