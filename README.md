# Bioinformatics Tools (Pipelines)

This repository contains tools and data types for [Janis](https://github.com/PMCC-BioinformaticsCore/janis) 
directly related to the bioinformatics field.

Refer to the [documentation](https://janis.readthedocs.io/en/latest/tools/bioinformatics/index.html) for a full list of tools.

## Data types

The data types are a way of encapsulating information about the file (including secondary files), and it allows clarity
when connecting inputs and steps together (as you know a BAM file should be connected to BAM input).


This documentation will be updated with a full (_generated_) list of data types, however for now here's an approximate list (nested means inherited):


### Nested types
If a type is nested

### Non-exhaustive of bioinformatics data types


## Testing

I'm not sure how to unit tests these tools, they're mostly definitions and as long as the syntax is fine, it's hard 
to logically test them without functionally running them with test data.

As Janis contains unit tests, there should be sufficient coverage for the base of the command tools.

There are plans to build a module to functionally test these tools (with some test data), 
however that will probably be a little while away

## Documentation

[![Documentation Status](https://readthedocs.org/projects/janis/badge/?version=latest)](https://janis.readthedocs.io/en/latest/?badge=latest)

Documentation is generated on [Janis](https://github.com/PMCC-BioinformaticsCore/janis). 
To generate new documentation you will need to: 
1. Commit your changes here,
2. Update the submodule pointer on Janis,
3. Checkout Janis (recursively),
4. Run the regenerate script `janis/docs/regeneratedocumentation.py`,
5. Commit these changes and the documentation will autobuild on ReadTheDocs.