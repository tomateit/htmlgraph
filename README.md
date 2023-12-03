# HTMLGraph

Print out text nodes from html page graph.
Useful for detemplation and parsing.

## Example

```html
<html>
<body>
<p>
    Level 1 Root 1
    <p>
        Level 2 Node 1
    </p>
    Level 1 Root 2
    <p>
        Level 2 Node 2
    </p>
    <p>
        Level 2 Root 2
        <p>
            Level 3 Node 1
        </p>
    </p>
    <p>
        Level 2 Root 3 <b>Subsection<i>Subsubsection</i>Subsection</b> Level 2 Root 4
    </p>
</p>
</body>
</html>

```

Turns into 
```
Root
├── Level 1 Root 1
│   └── Level 2 Node 1
└── Level 1 Root 2
    ├── Level 2 Node 2
    ├── Level 2 Root 2
    │   └── Level 3 Node 1
    ├── Level 2 Root 3
    │   ├── Subsection
    │   │   └── Subsubsection
    │   └── Subsection
    └── Level 2 Root 4

```
