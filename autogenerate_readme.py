import glob

def generate_readme(f):

    f.write("Directory list:\n")

    for d_ in sorted(glob.glob('*/')):
        f.write("- {}\n".format(d_))

def run(readme_name='README.md'):

    with open(readme_name, 'w') as f:
        generate_readme(f)

if __name__ == "__main__":
    run()
    