import os
import sys

# Get the main folder and number of files from command line arguments
main_folder = "Chapitres"
strt_index = 1
end_index = 30
if len(sys.argv) > 1:
    main_folder = sys.argv[1]
    strt_index = int(sys.argv[2])
    end_index = int(sys.argv[3])

# Create the main folder if it doesn't already exist
if not os.path.exists(main_folder):
    os.makedirs(main_folder)

# Create the files
for i in range(strt_index, end_index+1):
    filename = "Chapitre{}.md".format(i)
    filepath = os.path.join(main_folder, filename)
    with open(filepath, 'w') as f:
        f.write("# Chapitre {}\n## ".format(i))

print("Created {} files in {}".format(end_index, main_folder))
