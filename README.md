# manage_chapter_files
It's a set of scripts that create a chapter structure like this:
```
|
|_chapters
|  |_chapter1.md
|  |_chapter2.md
|  |_chapterN.md
|
|_chapters_overview.md
```

1. Run the **make_chapter_overview.py** to create the file **chapters_overview.md**.
2. Fill this file following its template.
3. Run the **make_chapter_files.py** to create the files chapter1.md to chapterN.md.
4. Run the **set_titles.py** to fill the chapters files following the file **chapters_overview.md**.
