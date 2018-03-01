# get last modified sublime-project file:
vscode_project_file=$(ls --sort=t *.code-workspace | head -1)
code ${vscode_project_file}
# code-insiders ${vscode_project_file}