import os
import shutil
from jinja2 import Environment, FileSystemLoader
import yaml

with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

output_dir = 'docs'
os.makedirs(output_dir, exist_ok=True)

env = Environment(loader=FileSystemLoader('themes/custom'))
template = env.get_template('index.html')

output_html = template.render(config=config)
with open(os.path.join(output_dir, 'index.html'), 'w') as fh:
    fh.write(output_html)

assets_source = os.path.join('themes', config['theme'], 'assets')
assets_dest = os.path.join(output_dir, 'assets')
if os.path.exists(assets_source):
    shutil.copytree(assets_source, assets_dest, dirs_exist_ok=True)

print("Site generated successfully.")