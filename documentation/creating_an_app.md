# Creating an App 

Lets look at the ideal app structure - content app is the use case for apps we build
but as we extend this we will add more details.

An app follows the same design as django-admin startapp

You will create two new python directories in this application

```python
> blocks
> components
```

- Blocks are for secondary content on a page
- Components are the primary content to be rendered. 

```python
# A component VIEW will have this following structure
"""
If the App is called content the app would be Content 
the view would be Single or the name of the file that is being requested.
The Type is equal to component

eg.) ContentSingleCompoent

if this was a block section it would be Content{What}Block:
"""

class AppViewType:
    def __init__(self):
        pass
    
    def render(self, context):
        """
        The goal of this is to be amazing       
        """     
```

The goal behind this project is to allow rapid development and remove urls and a few other things that will
allow for rapid development of applications... create one template allow for rapid expansion
will see how this goes. 