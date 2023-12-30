import os

problems = [o for o in os.scandir() if (o.is_dir()) and (o.name[0]!='.')]

def touch_yaml(problem):
    os.system(f"touch {problem.path+'/problem.yaml'}")

def validator_to_checker(problem):
    print(problem)
    with open(problem.path+'/problem.yaml', 'r') as f:
        old = f.read()
        new = old.replace('validator', 'checker')
    with open(problem.path+'/problem.yaml', 'w') as f:
        f.write(new)

# Change all occurences of "validator" to "checker"
for p in problems:
    touch_yaml(p)
    validator_to_checker(p)

# print (list(os.scandir()))