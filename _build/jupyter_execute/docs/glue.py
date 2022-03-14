#!/usr/bin/env python
# coding: utf-8

# (glue)=
# 
# # Insert variables into pages with `glue`
# 
# You often wish to run analyses in one notebook and insert them into your
# documents text elsewhere. For example, if you'd like to include a figure,
# or if you want to cite a statistic that you have run.
# 
# The **`glue` submodule** allows you to add a key to variables in a notebook,
# then display those variables in your book by referencing the key.
# 
# This page describes how to add keys to variables in notebooks, and how to insert them
# into your book's content in a variety of ways.[^download]
# 
# [^download]: This notebook can be downloaded as
#             **{nb-download}`glue.ipynb`** and {download}`glue.md`

# (glue/gluing)=
# 
# ## Gluing variables in your notebook
# 
# You can use `myst_nb.glue()` to assign value of a variable to
# a key of your choice. `glue` will store all of the information that is normally used to **display**
# that variable (ie, whatever happens when you display the variable by putting it at the end of a cell).
# Choose a key that you will remember, as you will use it later.
# 
# The following code glues a variable inside the notebook:

# In[1]:


from myst_nb import glue
<<<<<<< Updated upstream
a = "my variable!"
glue("my_variable", a)


# You can then insert it into your text like so: {glue:}`my_variable`.
# 
# That was accomplished with the following code: `` {glue:}`my_variable` ``.
# ```
# {glue:}`my_variable`
=======
a = "Batch1"
glue("my_variable", a)


# ```md
# example markdown block {glue:}`my_variable`
# ```
# 
# Some code here {glue:}`my_variable`+more code
# 
# You can then insert it into your text like so: {glue:}`my_variable`.
# 
# That was accomplished with the following code: `` {glue:}`my_variable` ``.
# 
# ```
# inside a code block {glue:}`my_variable`
>>>>>>> Stashed changes
# ```

# In[2]:


<<<<<<< Updated upstream
{glue:}`my_variable`
=======
inside a {code-cell} {glue:}`my_variable`
>>>>>>> Stashed changes


# In[ ]:


<<<<<<< Updated upstream
{glue:}`my_variable`


# {glue:code}`my_variable`
=======
inside an ipython {code-cell} {glue:}`my_variable`

>>>>>>> Stashed changes
