pjv - Python JSON Validator
===========================

PJV helps validating and find erroneous line in JSON file.

Installation
------------

By using pip::

    pip install pjv

Example
-------

Given sample.json file content::

  {"scores":
      {"hvn": "9"},
      {"nvh": "6"},
  }

Use pjv to validate it::

  $ pjv sample.json
  Error: Expecting property name: line 3 column 5 (char 33)
  2     {"hvn": "9"},
  3     {"nvh": "6"}, <----- this or maybe the line above is informal, such as redundant or missing `,`. See http://json.org for JSON format.
  4 }

Authors
-------

Viet Hung Nguyen <hvn@familug.org>

Contribution
------------

All contribution are greatly welcome :+1:
