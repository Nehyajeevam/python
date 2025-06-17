enames=['rahul','sonia','priyaka']
def changecase(enames):
    return enames.upper()


new_names=list(map(changecase,enames))

print(enames)
print(new_names)