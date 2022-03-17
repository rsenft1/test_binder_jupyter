---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(glue)=

# Insert variables into pages with `glue`

You often wish to run analyses in one notebook and insert them into your
documents text elsewhere. For example, if you'd like to include a figure,
or if you want to cite a statistic that you have run.

The **`glue` submodule** allows you to add a key to variables in a notebook,
then display those variables in your book by referencing the key.

This page describes how to add keys to variables in notebooks, and how to insert them
into your book's content in a variety of ways.[^download]

[^download]: This notebook can be downloaded as
            **{nb-download}`glue.ipynb`** and {download}`glue.md`

+++

(glue/gluing)=

## Gluing variables in your notebook

You can use `myst_nb.glue()` to assign value of a variable to
a key of your choice. `glue` will store all of the information that is normally used to **display**
that variable (ie, whatever happens when you display the variable by putting it at the end of a cell).
Choose a key that you will remember, as you will use it later.

The following code glues a variable inside the notebook:

```{code-cell} ipython3
from myst_nb import glue
a = "Batch1"
glue("my_variable", a)

```

```md
example markdown block {glue:}`my_variable`
```

Test out remove-input:

```{code-cell} ipython3
%store -r variablepgOne

print(f"some code {variablepgOne}")
```

Test out remove-input with glue:

```{code-cell} ipython3
:tags: [remove-input]

print(f"some code {b}")
```

```{code-cell} ipython3
:tags: [remove-input]

print(f"some code {c}")
```
Test out remove-input with variable deined elsewhere:
```{code-cell} ipython3
:tags: [remove-input]

print(f"some code {variablefromanotherpage}")
```

Some code here {glue:}`my_variable`+more code

You can then insert it into your text like so: {glue:}`my_variable`.

That was accomplished with the following code: `` {glue:}`my_variable` ``.

```
inside a code block {glue:}`my_variable`
```
```{code-cell}
inside a {code-cell} {glue:}`my_variable`
```
```{code-cell} ipython3
inside an ipython {code-cell} {glue:}`my_variable`
```
