"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""




class Strings:
    
    def __init__(self, list_of_string):
        self.list_of_string=list_of_string
        self.True_or_False=self.check_strings(list_of_string)

    def check_strings(self, listofstrings):
        for string in listofstrings :
            first_arg, second_arg = string[0], string[1]
            first, second = len(first_arg), len(second_arg)
            if first>=second :
                result=first_arg[first-second:]
                if result!= second_arg:
                   return False
                    
            else :
                return False
        return True
    
 


if __name__ == '__main__':
    fixed_tests_False = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs")
        ]
    fixed_tests_True = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails")
        ]

    fixed_tests_True=Strings(fixed_tests_True)
    print(f"fixed_tests_True is : {fixed_tests_True.True_or_False}")

    fixed_tests_False=Strings(fixed_tests_False)
    print(f"fixed_tests_False is : {fixed_tests_False.True_or_False}")