from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

workspace = Path('/Users/a1/Documents/ChatGPT/agent')
case = workspace / 'demo' / 'masif'
output = workspace / 'AI4S_MaSIF_Product_Demo.zip'
selected = [workspace / name for name in ['AI4S_AGENT_FRAMEWORK_V2.md', 'INFRASTRUCTURE_NATIVE_AGENT_ARCHITECTURE.md', 'CONTEXT_HANDOFF.md']]
selected.append(workspace / 'sources' / 'grok-bot-0.18-harness-static-analysis.md')
selected += [case / name for name in ['AI4S_DETAILED_DESIGN.md', '00_DEMO_INTRO.md', '01_INFRA_ARCHITECTURE.md', '02_UX_PHILOSOPHY.md', '03_MASIF_DEMO_CASE.md', 'demo-fixtures.json', 'sources/guide-extracted.txt', 'app/index.html', 'app/README.md', 'app/design-qa.md']]
for folder in [case / 'diagrams', case / 'app' / 'assets', case / 'app' / 'pages']:
    selected += sorted(p for p in folder.iterdir() if p.is_file() and p.suffix in ['.png', '.svg', '.md'])
for p in selected:
    if p.is_symlink() or not p.is_file() or not p.resolve().is_relative_to(workspace):
        raise RuntimeError(f'Invalid package file: {p}')
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for p in selected:
        archive.write(p, Path('ai4s-demo') / p.relative_to(workspace))
    archive.writestr('ai4s-demo/START_HERE.md', '# AI4S MaSIF 产品展示包\n\n先读 demo/masif/AI4S_DETAILED_DESIGN.md。演示路径见 demo/masif/00_DEMO_INTRO.md。\n\n可交互页面：demo/masif/app/index.html。请保留assets相对位置。\n\n两张视觉架构图位于demo/masif/diagrams，四页UI位于demo/masif/app/pages。\n\n团队报告结果与界面编排分别留有来源；当前HTML不提交真实科研作业。\n')
print(f'{output}\n{output.stat().st_size} bytes\n{len(selected)} files')
