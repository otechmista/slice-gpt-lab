# Mermaid Diagrams

These files contain Mermaid diagrams using the `.mf` extension requested for the project.

## Files

- `training_flow.mf`: training from dataset to checkpoint.
- `inference_flow.mf`: prompt to assistant answer.
- `attention_flow.mf`: causal self-attention.
- `context_tokens_flow.mf`: chat messages to tokens and context window.
- `checkpoint_flow.mf`: checkpoint save and load.

## Rendering Note

Some editors render Mermaid automatically only inside Markdown files. If your editor does not render `.mf`, paste the file contents into a Mermaid renderer or wrap it in a Markdown code block:

````markdown
```mermaid
flowchart TD
    A --> B
```
````

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [File-by-File Lessons](../14_file_by_file_lessons.md) connects every source file to a learning goal.

Next: return to [Course Guide](../00_course_guide.md) when you want to run the project again or choose a chapter to revisit.

<!-- COURSE_THREAD_END -->
