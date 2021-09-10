from app import create_app
from flask_script import Manager,Server

# if __name__=='__main__':
#     app.run()

#create app instance
app=create_app('development')

manager =Manager(app)
manager.add_command('server',Server)
#We then create a command line argument to tell us how to run our application.
manager.add_command('server',Server)

#decorator to create a new command.
@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=='__main__':
    manager.run()

