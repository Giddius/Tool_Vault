

## Title

```md
# <p align="center">{{ name }}</p>
```

---

## collapsible List

```md
<details><summary>{{ collapsible_list_title }}</summary>

{% for list_item in collapsible_list}
- {{ list_item }}
{% endfor %}
</details>
```

---
## Images

```md
![alt text](https://github.com/JarateKing/Github-Markdown-Snippets/blob/master/dev/example.png)
![alt text](dev/example.png)
```

---

## Image size

```md
<img width="10" height="10" src="https://placehold.it/15/ff0000/000000?text=+">
<img width="50" height="50" src="https://placehold.it/15/ff0000/000000?text=+">
```

---

## Captioned Image

```md
<table><tbody><tr>
<td>

<p align="center">
<img src="{{ image_url }}">
</p>

<p align="center"><sub>{{ image_caption }}</sub></p>
</td>
</tr></tbody></table>
```

---


## Table of Contents

```md
<table><tbody><tr>
<td><details><summary>Table of Contents</summary>
{% for index, key, value in enumerate(contents.items()) %}
{{index}}. [{{ key }](#{{ value })
</details></td>
</tr></tbody></table>
```

### With Subitems

TODO: figure templating out

```md
<table><tbody><tr>
<td><details><summary>Table of Contents</summary>

1. [Category 1](#html)
   1. [Subcategory 1](#tags)
   2. [Subcategory 2](#attributes)
2. [Category 2](#text)
3. [Category 3](#alignments)
</details></td>
</tr></tbody></table>
```

---

## Hotkey Styling

```md
<kbd>Text</kbd>
```

---

## Subscripts

```md
text<sub>subscript</sub>
```

---

## Superscripts

```md
text<sup>superscript</sup>
```

---

## Split Page

```md
<table><tbody><tr>
<td width="50%">Left Text</td>
<td width="50%">Right Text</td>
<td></td></tr></tbody></table>
```

---

## Triple Alignment

Note: this only works well for single words, and when the left and right aligned texts are approximately the same length (such as with "prev" and "next", for example). The percents can be fiddled with otherwise, but is less likely to work.

```md
<table><tbody><tr>
<td>Left Aligned</td>
<td  width="50%"></td>
<td>Center Aligned</td>
<td  width="50%"></td>
<td>Right Aligned</td>
</tr></tbody></table>
```

---

## Surround By Box

```md
<table><tbody><tr>
<td>Text to surround box with</td>
</tr></tbody></table>
```

```md
<table border="1"><tbody><tr>
<td width="100%">Text to surround box with</td>
<td></td></tr></tbody></table>
```

---
