"""
Copies/starts a blank Vue project in a folder of your choosing, and then runs
it locally.

Run this file like so:
% python newvue.py your_project_name your_destination_folder_path
"""


import argparse
import os
import shutil


def main():
    parser = argparse.ArgumentParser(description="Initialize a Vue app")

    parser.add_argument("name", type=str, help="Name of the new Vue app folder")

    parser.add_argument("destination", type=str, 
                        help="Path to the destination folder")

    args = parser.parse_args()

    try:
        if not os.path.isdir(args.destination):
            print(f"Destination folder '{args.destination}' does not exist.")
            return
        
        app_path = os.path.join(args.destination, args.name)

        shutil.copytree("./copy_base_vue_app", app_path)

        os.chdir(app_path)

        os.system("npm install && npm run dev")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
