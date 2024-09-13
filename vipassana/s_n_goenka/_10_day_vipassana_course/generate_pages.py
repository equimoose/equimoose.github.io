from dataclasses import dataclass
import os

from jinja2 import Environment


dir_path = os.path.dirname(__file__)


@dataclass
class Day:
    name: str
    youtube_url: str
    relative_path_to_file: str = ""

    def build_file_name_absolute(self) -> str:
        day_name = self.name.lower().replace(" ", "_")
        return f"{dir_path}/{day_name}_english.html"

    def set_relative_path_to_file(self, root_dir_path: str):
        day_name = self.name.lower().replace(" ", "_")
        relative_path = dir_path.replace(root_dir_path, "")
        self.relative_path_to_file = f"{relative_path}/{day_name}_english.html"

    def title(self) -> str:
        return f"10 Day Vipassana Course - {self.name} (English)"

    def transcribed_discourse_url(self) -> str:
        name = self.name.replace(" ", "%20")
        return f"https://raw.githubusercontent.com/equimoose/meditation/main/vipassana/S.N.Goenka/10%20Day%20Vipassana%20Course%20-%20{name}%20%20(English).txt"


days: list[Day] = [
    Day(
        name="Day 1",
        youtube_url="https://www.youtube.com/watch?v=cz7QHNvNFfA&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=1",
        # youtube_url="https://www.youtube.com/embed/cz7QHNvNFfA?si=xDJr0WBwd4tmdIxG&amp;start=2624",
    ),
    Day(
        name="Day 2",
        youtube_url="https://www.youtube.com/watch?v=cYG5VvHry7c&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=2",
    ),
    Day(
        name="Day 3",
        youtube_url="https://www.youtube.com/watch?v=rXXnSK2a47w&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=3",
    ),
    Day(
        name="Day 4",
        youtube_url="https://www.youtube.com/watch?v=UvKl0Wpwbn0&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=4",
    ),
    Day(
        name="Day 5",
        youtube_url="https://www.youtube.com/watch?v=dB0TB7tQoYY&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=5",
    ),
    Day(
        name="Day 6",
        youtube_url="https://www.youtube.com/watch?v=Yxp0mZeK2zk&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=6",
    ),
    Day(
        name="Day 7",
        youtube_url="https://www.youtube.com/watch?v=u4twJT1RfiM&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=7",
    ),
    Day(
        name="Day 8",
        youtube_url="https://www.youtube.com/watch?v=Us5Iq302eNU&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=8",
    ),
    Day(
        name="Day 9",
        youtube_url="https://www.youtube.com/watch?v=OeCO_EQ0vN8&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=9",
    ),
    Day(
        name="Day 10",
        youtube_url="https://www.youtube.com/watch?v=NzrQ2HMFOuo&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=10",
    ),
    Day(
        name="Last Day",
        youtube_url="https://www.youtube.com/watch?v=aeqCeU8Abng&list=PLPJVlVRVmhc4Z01fD57jbzycm9I6W054x&index=11",
    ),
]


def set_relative_path_to_file(root_dir_path: str):
    for day in days:
        day.set_relative_path_to_file(root_dir_path)


def generate_pages(env: Environment):
    current_search_path = str(env.loader.searchpath[0]) # type: ignore
    relative_path = dir_path.replace(current_search_path, "")

    for i, day in enumerate(days):
        template = env.get_template(f".{relative_path}/template_day_english.html")

        previous_day = None if i == 0 else days[i - 1]
        next_day = None if i == len(days) - 1 else days[i + 1]

        with open(day.build_file_name_absolute(), "w") as file:
            data = {
                "title": day.title(),
                "youtube_video_url": day.youtube_url,
                "transcribed_discourse_url": day.transcribed_discourse_url(),
                "previous_page_url": previous_day.relative_path_to_file if previous_day else "",
                "next_page_url": next_day.relative_path_to_file if next_day else "",
            }
            file.write(template.render(data))
