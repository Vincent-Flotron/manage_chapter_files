import os

def create_chapters_overview(chapter_overview_path="", chapter_path="chapters", start_chapter_nb=1, end_chapter_nb=30):
  if not chapter_overview_path:
    chapter_overview_path = "chapters_overview.md"

  with open(chapter_overview_path, "w") as f:
    for i in range(start_chapter_nb, end_chapter_nb+1):
      f.write(f"{i}.\t[Write_title_here: write_resume_part_here.]({os.path.join(chapter_path, 'Chapitre' + str(i) + '.md')})\n")

  print(f"Created chapters overview file: {os.path.abspath(chapter_overview_path)}")

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument("--chapter_overview_path", default="")
  parser.add_argument("--chapter_path", default="chapters")
  parser.add_argument("--start_chapter_nb", type=int, default=1)
  parser.add_argument("--end_chapter_nb", type=int, default=30)
  args = parser.parse_args()

  create_chapters_overview(**vars(args))
