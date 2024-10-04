import os
from typing import Any

from jinja2 import Environment, FileSystemLoader

from vipassana.s_n_goenka._10_day_vipassana_course.generate_pages import generate_pages, set_relative_path_to_file, days


dir_path = os.path.dirname(__file__)
# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader(dir_path))

templates_to_render = [
    ["template_index.html", "index.html"],
]

set_relative_path_to_file(dir_path)

for template, output_file_path in templates_to_render:
    template = env.get_template(template)
    with open(output_file_path, "w") as file:
        data: Any = {
            "is_index": True,
            "links": days,
        }
        file.write(template.render(data))

generate_pages(env)

print("Static site generated successfully.")
