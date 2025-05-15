# AmberOS 10 Text Engine

hi, spaced here, writing this so yall know how to do stuff

## Rendering Pipeline
### Creating or Updating text
we have a custom format used so the text engine can read and write stuff properly:.
```
content|x|y|color|brightness|alignment|id
```
throw this into `TextEngine.RenderQueue`.


<sub> note: dont try to serch the render queue for the text you just rendered; text engine WILL catch it, analyze it, and delete it before you can. </sub>

### Pcoressing Text
Relatively simple order:
 1. **Check if it already exists in the render cache.** we probably don't need to re-render if we already know it exists. also used for detecting new text.
 2. Assuming its not in the render cache, **Decompile it and check if the ID exists.** If an attribute changes in text, the initial check isn't gonna catch it. do a quick sanity check here to make sure it's not just a changed attribute. *This means comparing the request data with other items in the cache.*
 4. **If an attribte actually changed or it's new text, render it.**

## Variables you'll probably be confused by
 - `tempdecompcache1` - This is used for the comparisons, as described in the pipeline
