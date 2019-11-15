if __name__ == "__main__":
    def printv(variables, sep =''):
    ''' print variables names with their values
        example: x = 1, y = 10; vprint(x,y>10)
        prints the following:
        x = 1
        y>10 = False'''

    def vprint(variables, sep ='\n'):
    vars = variables.split(',')
    for var in vars:
      print(var.strip(), '=', repr(eval(var)), end = sep)
