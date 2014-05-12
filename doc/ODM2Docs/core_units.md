ODM2 Core: Units
================

The ODM2 **Units** entity contains units of measure.  Units are described by a name, a type (from a controlled vocabulary), and a common abbreviation. Units are used to specify the units of measure for the data values within a Result. Units are separate from Variables and are specified at the Result level. In ODM2, multiple Results may exist for the same Variable, but specified with different Units. Units are a controlled vocabulary in ODM2. The Units entity is also linked to other entities within the ODM2 schema and its extensions where Units information is needed (e.g., in the Results schema where Units are specified for X, Y, and Z locations of spatial offsets, etc.)
