# Swish Application Config File

The following is just an outline of how I would like to see applications get installed -- this may change dramatically upon alpha 0.5.0 release

# Example Project Folder Structure

This is the content application that allows you to write blog post - it is used as the primary example throughout the enteire development of the Swish system

```
- content
```

- This is the apps.py file that your django project creates.
- Maybe it should be in a swish.py file so the system can load it? 

```python
class AppConfig():

    def swish(self):
        
        app = dict()    
        app['name'] = 'Name of Application'
        app['slug'] = 'a-unique-non-conflicting-name'
        app['version'] = '1.0.0'  # The Current Version of APP
        
        return app
```