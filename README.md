# pyepoch
A simple python-based command-line utility to convert time or date stamps to epoch and back.

#### Usage
`pyepoch` is installed as a command-line utility accessible as `epoch` from the command-line.

You can use it to convert time or date string formats to epoch timestamps (with milliseconds):

```
-$ epoch '2018/1/1'
1514764800000

```

or if you specify, in seconds:
```text
-$ epoch '2018/1/1' -s
1514764800
```

You can specify a timestamp as exact and detailed as you want it to. Additionally you can always convert back the epoch timestamp to an iso formatted date string:

```
-$ epoch 1514764800000
2018-01-01T00:00:00
```

if your epoch input is in seconds you can add a `-s` flag, the tool can't determine this automatically.

#### Bugs
Feel free to report issues, this 'utility' was build out of ease as I got frustrated with manual conversion of timestamps and strings the whole time.