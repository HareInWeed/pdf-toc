# ToC

ToC file consists of entries and commands. Each entry and commands occupies exactly one line in toc file. Each entry represents a bookmark. Commands, on the other hands, control how ToC file is interpreted and how bookmarks are generated.

There is an example in [Lorem Ipsum_toc.txt](/tests/test_files/Lorem%20Ipsum_toc.txt)

## Entry

All entries matches the regex below

```regex
^( *)(.+) (\d+)\s*$
```

- The match group 1 (which is indent of the line) will determine the level of the bookmark. With default indent 4, Every 4 space means 1 more level.
- The match group 2 is the content of the bookmark
- The match group 3 is the page number of the bookmark

## Command

All commands matches the regex below

```regex
^>>>>.+$
```

Thus any command must start with `>>>>`, and there shouldn't be any space character before that.

Every command can only affect the entries after it.

### Offset

Sometimes all the difference between the page numbers in your ToC data and the pdf file might happen to be the same value (which is quite common when you are dealing with an OCR file). That is where offset value come in handy. With an offset, you can increase or decrease the page number every entry for a certain value (offset), to make the ToC match the right page.

The initial offset is 0, so if you don't change the offset, page numbers of entries won't change.

#### SetOffset

set the offset

```plaintext
>>>> offset = 10
```

#### changeOffset

change current offset by a certain value

```plaintext
>>>> +10
```

for example, after these two commands:

```plaintext
>>>> +10
>>>> -7
```

the offset will be 3

### Indent

The indent of every entries will determine the level of the bookmark. You can use command to specify a new indent instead of default 4.

For example, after this command

```
>>>> indent = 2
```

the indent will be 2.

Note every command only affects subsequent entries. So if there are entries before it, the indent will remain at 4.