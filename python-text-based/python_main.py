from sys import version_info

if(version_info[0] < 3):
    import python_2
    python2
else:
    import python_3
    python3
