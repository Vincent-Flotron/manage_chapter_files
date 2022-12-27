import os
import re
import sys

# Get the main folder and overview file from command line arguments
main_folder = "Chapitres"
overview_file = "chapitres_overview.md"
if len(sys.argv) > 1:
    main_folder = sys.argv[1]
    overview_file = sys.argv[2]

# Open the overview file and extract the titles and resumes
titles = []
resumes = []
with open(overview_file, 'r') as f:
    for line in f:
        match_title = re.search(r'\d+\t\[([^\]]+?):', line)
        match_resume = re.search(r':([^\]:]+?)\]', line)
        if match_title:
            titles.append(match_title.group(1))
        if match_title:
            resumes.append(match_resume.group(1))

if len(resumes) != len(titles):
    print('nb titles and resumes are not the same! Nb titles={}, nb resumes=[]'.format(len(titles), len(resumes)))

# Get a list of all the files in the main folder
filenames = os.listdir(main_folder)

# Sort the filenames so they are processed in order
filenames.sort()

# Parse each file
for filename in filenames:
    # Only process files that match the pattern "Chapitre\d+.md"
    if re.match(r'Chapitre\d+\.md', filename):
        filepath = os.path.join(main_folder, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        # Get the index of the current file (from the filename)
        index = int(filename.split('.')[0].split('Chapitre')[1]) - 1
        
        # Insert resume by modifying the second and third line of the file
        if index < len(titles):
            lines[1] = "## {}\n".format(titles[index])

            resume_line = '{}'.format(resumes[index].strip())

            # Add or modify the resume title, the second line
            if len(lines) < 3:
                lines.append('### Resume')
            else:
                lines[2] = '### Resume'

            # Add or modify the resume part, the third line
            if len(lines) < 4:
                lines.append('\n{}'.format(resume_line))
            else:
                lines[3] = '\n' + resume_line

            # Add the fourth line
            if len(lines) < 5:
                lines.append('\n### Content\n')
            else:
                lines[4] = '\n### Content\n'
        
            # Write the modified lines back to the file
            with open(filepath, 'w') as f:
                f.writelines(lines)

print("Processed {} files in {}".format(len(titles), main_folder))
