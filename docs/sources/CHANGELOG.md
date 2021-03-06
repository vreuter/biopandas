# Release Notes ![](img/logos/3eiy_120.png)

The CHANGELOG for the current development version is available at
[https://github.com/rasbt/biopandas/blob/master/docs/sources/CHANGELOG.md](https://github.com/rasbt/biopandas/blob/master/docs/sources/CHANGELOG.md).

### 0.2.0 (2017-04-02)

##### Downloads

- [Source code (zip)](https://github.com/rasbt/biopandas/releases/tag/v0.2.0)
- [Source code (tar.gz)](https://github.com/rasbt/biopandas/releases/tag/v0.2.0.tar.gz)

##### New Features

- Added an `amino3to1` method to `PandasPdb` data frames to convert 3-amino acid letter codes to 1-letter codes.
- Added a `distance` method to `PandasPdb` data frames to compute the Euclidean distance between atoms and a reference point.
- Added the `PandasMol2` class for working with Tripos MOL2 files in pandas DataFrames.


##### Changes

- `PandasPDB` was renamed to `PandasPdb`.
- Raises a warning if `PandasPdb` is written to PDB and ATOM and HETAM section contains unexpected columns; these columns will now be skipped.

##### Bug Fixes

- -


### 0.1.5 (2016-11-19)

##### Downloads

- [Source code (zip)](https://github.com/rasbt/biopandas/releases/tag/v0.1.5)
- [Source code (tar.gz)](https://github.com/rasbt/biopandas/releases/tag/v0.1.5.tar.gz)

##### New Features

- Added an `impute_element` method to `PandasPDB` objects to infer the Element Symbol from the Atom Name column.
- Added two new selection types for `PandasPDB` ATOM and HETATM coordinate sections: `'heavy'` and `'carbon'`.

##### Changes

- Include test data in the PyPI package; add install_requires for pandas.
- The `'hydrogen'` atom selection in `PandasPDB` methods is now based on the element type instead of the atom name.
- By default, the RMSD is now computed on all atoms unless a specific selection is defined.

##### Bug Fixes

- -



### 0.1.4 (2015-11-24)

##### Downloads

- [Source code (zip)](https://github.com/rasbt/biopandas/releases/tag/v0.1.4)
- [Source code (tar.gz)](https://github.com/rasbt/biopandas/releases/tag/v0.1.4.tar.gz)

##### New Features

-

##### Changes

- Needed to bump the version number due to a bug in the PyPI setup.py script.
- Support for the old pandas sorting syntax (`DataFrame.sort` vs `DataFrame.sort_values`) incl. DeprecationWarning.

##### Bug Fixes

-



### 0.1.3 (2015-11-23)

##### New Features

-

##### Changes

-

##### Bug Fixes

- Exception handling in tests if PDB goes down (which just happened).
- Added a separate ANISOU engine to handle those records correctly.




### 0.1.2 (2015-11-23)

- First Release.
