# cookiecutter-cwd-poc

A Proof of Concept of putting the cookiecutter's rendered template in a current working directory instead of a nested directory named using 'project_slug' variable

## Implementation details

Note that a cookiecutter project root directory is named `{{ 'cookiecutter' }}` and not `{{ cookiecutter.project_slug }}` or `{{ cookiecutter.project_name }}` etc. By doing this, you can avoid specifying the project root name in your `cookiecutter.json` and prompting the user to provide a name for a project root directory. Since for this specific project, the root directory is deleted after all the rendered files are copied to the parent directory, there is no need for prompting the user to provide a name for a folder that would be deleted in a second.

There is no officially supported way of setting a constant name for a cookiecutter's project directory name. By specification, it should contain any runtime variable name injected into Jinja2 template syntax, for example: `{{ cookiecutter.project_name }}`. That also forces you to declare `project_name` in your `cookiecutter.json`, and you cannot skip that part and set `project_name` somehow at runtime using `pre_prompt` or `pre_gen_project` hooks.

But, after checking the `cookiecutter` package implementation details, I have discovered that there are the following restrictions for the project root directory name:

1. It should contain a Jinja2 template variable opening brackets: `{{`
2. It should contain the word `cookiecutter` in it
3. It should contain a Jinja2 template variable closing brackets: `}}`

With this implementation, you can potentially use any arbitrary variable name for your project root like `{{ cookiecutter.project_slug }}`, `{{ cookiecutter.project_name }}`, etc. But, that also makes it possible to use `{{ 'cookiecutter' }}` as a directory name. When rendering, `{{ 'cookiecutter' }}` would be evaluated to just plain text `cookiecutter`, allowing you to have a constant project root directory name.
