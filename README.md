# Tree Based Data Structure
Algorithm in Python that generates a tree-based data structure (dictionary) from a list of lists of data.

![Tree image](/img/tree.png)

From data stored in a list of lists, generate a hierarchical tree-based data structure (a dictionary). The lists can have different number of elements. The "final" elements (leaves) will always be stored in a list (even if it is an empty list or a single element list).

The algorithm obtains, for example, [2] from [1].

[1]
```python
data = [
         ['living_being'     , 'animal'    , 'fish'          , 'bream'         ], 
         ['living_being'     , 'animal'    , 'fish'          , 'bass'          ], 
         ['living_being'     , 'plant'      , 'pine'          , 'pinnus_pinnea'], 
         ['living_being'     , 'bacteria'  , 'lactobacillus'                   ], 
         ['living_being'     , 'plant'      , 'oak'           , 'quercus_ilex' ], 
         ['living_being'     , 'animal'    , 'mollusk'       , 'snail'         ], 
         ['artificial_object', 'vehicle'   , 'car'                             ], 
         ['artificial_object', 'vehicle'   , 'moto'                            ], 
         ['artificial_object', 'instrument', 'guitar'                          ], 
         ['natural_object'                                                     ],
       ]
```
[2]
```python
result = {

    'living_being': {

        'animal': {
            'fish':    ['bream', 'bass'], 
            'mollusk': ['snail']
        }, 

        'plant': {
            'pine':  ['pinnus_pinnea'], 
            'oak':   ['quercus_ilex']
        }, 

        'bacteria': ['lactobacillus']
    }, 

    'artificial_object': {
        'vehicle':    ['car', 'moto'], 
        'instrument': ['guitar']
    }, 

    'natural_object': []

}
```
