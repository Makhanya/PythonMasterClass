"""
    Unit Testing
    
        *Test smallest parts of an application in isolation(e.g units)
        *Good candidates for unit testing: individual classes,
            modules or functions
        *Bad candidates for unit testing: an entire application, dependencies
            across sevaral classes or modules 

    unittest
        *Python comes with a built-in module called unittest
        *You can write unit tests encapsulated as classes that 
            inherit from unittest.TestCase
    unittest Example

        *activities.py
            def eat(food, is_healthy):
                pass
            def nap(num_hours):
                pass


        Commenting Tests
            test.py
            class SomeTests(unittest.TestCase):
                def first_test(self):
                    ""testing a thing"" 
                    self.assertEqual(thing(), "something")

                def second_test(self):
                    ""testing another thing""
                    self.assertEqual(another_thing(), "something else")
    """