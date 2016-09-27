# Driver Downloader

## Installation
```bash
pip install requirements.txt
python setup.py install
```

## Usage
THIS SECTION IS TO COME. THIS REPOSITORY IS NOT READY YET - COME BACK LATER

### Implamentation
1. Grab webpage
2. Use Regex to parse the information from HTML => Parsed data (gathered from plugin)
3. Download said files
4. Handle downloaded files (IE: Extracting them all) (from plugin, but provide libraries (ALA 		`extractEXE.py`))
5. Move to unfurl process to minimize the effects of horrible Windows Path

- - -

### Python Regex Implamentability

`.*there` => ``$& Corbin`

`==`

`re.sub(r'.*there', r'\g<0>, Corbin', "Hi there, how are you?")`

You’re putting an capture group around everything, and then using `\g<0>` which is Python’s syntax for `$1` in the things that you’re more used to to put it in.

- - -

### Capture Groups

To help understand what a capture group is, consider the following text:

```
http://stackoverflow.com/
http://stackoverflow.com/questions/tagged/regex
```

Now, if I apply the regex below over it...

```
(http|ftp)://([^/\r\n]+)(/[^\r\n]*)?
```

... I would get the following result:

```
Match "http://stackoverflow.com/"
     Group 1: "http"
     Group 2: "stackoverflow.com"
     Group 3: "/"

Match "http://stackoverflow.com/questions/tagged/regex"
     Group 1: "http"
     Group 2: "stackoverflow.com"
     Group 3: "/questions/tagged/regex"
```

But I don't care about the protocol -- I just want the host and path of the URL. So, I change the regex to include the non-capturing group `(?:)`.

```
(?:http|ftp)://([^/\r\n]+)(/[^\r\n]*)?
```

Now, my result looks like this:

```
Match "http://stackoverflow.com/"
     Group 1: "stackoverflow.com"
     Group 2: "/"

Match "http://stackoverflow.com/questions/tagged/regex"
     Group 1: "stackoverflow.com"
     Group 2: "/questions/tagged/regex"
```

See? The first group has not been captured. The parser uses it to match the text, but ignores it later, in the final result.

_[The explaination above was ripped from a StackOverflow question](http://stackoverflow.com/questions/3512471/what-is-a-non-capturing-group)_

- - -

### `\g<0>` Explaination

To explain what `\g<0>` more directly means inside of the Python Regex:

|        Context of reference to group “quote”            |                      Ways to reference it             |
|                    --------                             |                             --------                  |
| in a string passed to the `repl` argument of `re.sub()` | <ul><li>`\g<quote>`</li><li>`\g<1>`</li><li>`\1`</li> |

_[Stright from Python 3 documentation](https://docs.python.org/3/library/re.html)_

- - -

# Need To Document About Plugin System

#### References:
- http://docs.pylonsproject.org/projects/pylons-webframework/en/latest/advanced_pylons/entry_points_and_plugins.html

- - -

# TODO
- [ ] Better error handling for `wget` function
- [ ] Properly document Plugin system
- [x] Proper requirements.txt
- [ ] Option to delete or rename existing file
- [ ] Continue to add "ALT" until no longer possible
- [ ] Add option to rename duplications manually
- [ ] Use docopt for command line functionality
- [x] Implament plugin support (Lenovo plugin already grabs `drivers[]` properly)
- [ ] Fix strings with `,` in the name (in Lenovo plugin)
- [ ] Pass arguments (URL, namely) to plugin
- [ ] Automatically parse URL argument and run respective plugin
- [ ] Handle many downloads of drivers
- [ ] Split off different instances of driver downloads to proper directory tree
- [ ] Turn all regex stuff into some sort of library for easy lifting for others