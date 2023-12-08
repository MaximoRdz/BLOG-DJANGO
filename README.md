### TODO
- [ ] article images upload to media/article-name folder 
### Database Model Example (Normalized)

#### Blog Table

| id  | title | body |
|-----|-------|------|
| 1   | ...   | ...  |
| 2   | ...   | ...  |
| ... | ...   | ...  |

#### Images Table

| id  | blog_id (foreign key) | image_url | description |
|-----|-----------------------|-----------|-------------|
| 1   | 1                     | ...       | ...         |
| 2   | 1                     | ...       | ...         |
| 3   | 2                     | ...       | ...         |
| ... | ...                   | ...       | ...         |

This Markdown formatting represents the structure of the tables: the Blog Table and the Images Table. You can copy and paste this into your markdown editor or use it in your documentation to display the tables accordingly.
Link 
[Daring Fireball: Markdown Syntax Documentation](https://daringfireball.net/projects/markdown/syntax#img)